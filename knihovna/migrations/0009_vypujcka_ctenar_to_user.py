from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.text import slugify


def forwards_assign_readers(apps, schema_editor):
    vypujcka_model = apps.get_model('knihovna', 'Vypujcka')
    group_model = apps.get_model('auth', 'Group')
    user_app_label, user_model_name = settings.AUTH_USER_MODEL.split('.')
    user_model = apps.get_model(user_app_label, user_model_name)

    readers_group, _ = group_model.objects.get_or_create(name='readers')

    def build_unique_username(full_name, fallback_seed):
        base = slugify(full_name) or f'reader-{fallback_seed}'
        candidate = base
        index = 1
        while user_model.objects.filter(username=candidate).exists():
            candidate = f'{base}-{index}'
            index += 1
        return candidate

    for loan in vypujcka_model.objects.all():
        full_name = (loan.ctenar or '').strip()
        name_parts = full_name.split(maxsplit=1)
        first_name = name_parts[0] if name_parts else ''
        last_name = name_parts[1] if len(name_parts) > 1 else ''

        user = None
        if first_name or last_name:
            user = user_model.objects.filter(first_name=first_name, last_name=last_name).first()

        if user is None:
            username = build_unique_username(full_name, loan.pk)
            user = user_model.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
            )

        user.groups.add(readers_group)
        loan.ctenar_user_id = user.pk
        loan.save(update_fields=['ctenar_user'])

    fallback_user = user_model.objects.filter(groups__name='readers').first()
    if fallback_user is None:
        username = build_unique_username('reader-default', 'default')
        fallback_user = user_model.objects.create(username=username)
        fallback_user.groups.add(readers_group)

    vypujcka_model.objects.filter(ctenar_user__isnull=True).update(ctenar_user_id=fallback_user.pk)


class Migration(migrations.Migration):

    dependencies = [
        ('knihovna', '0008_alter_recenze_recenzent'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='vypujcka',
            name='ctenar_user',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='vypujcky',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Čtenář',
            ),
        ),
        migrations.RunPython(forwards_assign_readers, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name='vypujcka',
            name='ctenar',
        ),
        migrations.RenameField(
            model_name='vypujcka',
            old_name='ctenar_user',
            new_name='ctenar',
        ),
        migrations.AlterField(
            model_name='vypujcka',
            name='ctenar',
            field=models.ForeignKey(
                help_text='Vyberte čtenáře (uživatele), ideálně ze skupiny readers.',
                limit_choices_to={'groups__name': 'readers'},
                on_delete=django.db.models.deletion.CASCADE,
                related_name='vypujcky',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Čtenář',
            ),
        ),
    ]
