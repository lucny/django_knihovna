# Generated by Django 4.0.2 on 2022-03-30 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knihovna', '0002_autor_vydavatelstvi_kniha_autori'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='narozeni',
            field=models.DateField(blank=True, null=True, verbose_name='Datum narození'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='umrti',
            field=models.DateField(blank=True, null=True, verbose_name='Datum úmrtí'),
        ),
    ]
