# Generated by Django 4.2.2 on 2023-06-16 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='recomendado',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
