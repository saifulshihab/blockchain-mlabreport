# Generated by Django 2.2.7 on 2020-03-27 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='has_pid',
            field=models.BooleanField(default=False),
        ),
    ]
