# Generated by Django 2.2.7 on 2020-03-30 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demail', models.CharField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('doctor_name', models.CharField(max_length=100)),
            ],
        ),
    ]
