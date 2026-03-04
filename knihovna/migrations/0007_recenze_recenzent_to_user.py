from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.text import slugify


def forwards_assign_users(apps, schema_editor):
    recenze_model = apps.get_model('knihovna', 'Recenze')
    autor_model = apps.get_model('knihovna', 'Autor')
    user_app_label, user_model_name = settings.AUTH_USER_MODEL.split('.')
    user_model = apps.get_model(user_app_label, user_model_name)

    def ensure_unique_username(base_username):
        candidate = base_username or 'recenzent'
        index = 1
        while user_model.objects.filter(username=candidate).exists():
            candidate = f"{base_username or 'recenzent'}-{index}"
            index += 1
        return candidate

    for recenze in recenze_model.objects.select_related('recenzent').all():
        autor = recenze.recenzent
        if autor is None:
            continue

        existing_user = user_model.objects.filter(first_name=autor.jmeno, last_name=autor.prijmeni).first()
        if existing_user is None:
            username_base = slugify(f'{autor.jmeno}-{autor.prijmeni}')
            username = ensure_unique_username(username_base)
            existing_user = user_model.objects.create(
                username=username,
                first_name=autor.jmeno,
                last_name=autor.prijmeni,
            )

        recenze.recenzent_user_id = existing_user.pk
        recenze.save(update_fields=['recenzent_user'])

    fallback_user = user_model.objects.first()
    if fallback_user is None:
        fallback_user = user_model.objects.create(username='recenzent-default')

    recenze_model.objects.filter(recenzent_user__isnull=True).update(recenzent_user_id=fallback_user.pk)


class Migration(migrations.Migration):

    dependencies = [
        ('knihovna', '0006_vypujcka'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='recenze',
            name='recenzent_user',
            field=models.ForeignKey(
                blank=True,
                help_text='Vyberte uživatele, který recenzi napsal.',
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='recenze',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Recenzent',
            ),
        ),
        migrations.RunPython(forwards_assign_users, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name='recenze',
            name='recenzent',
        ),
        migrations.RenameField(
            model_name='recenze',
            old_name='recenzent_user',
            new_name='recenzent',
        ),
        migrations.AlterField(
            model_name='recenze',
            name='recenzent',
            field=models.ForeignKey(
                help_text='Vyberte uživatele, který recenzi napsal.',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='recenze',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Recenzent',
            ),
        ),
    ]
