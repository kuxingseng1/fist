# Generated by Django 3.0.8 on 2020-09-27 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rookie', '0002_auto_20200927_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custom',
            name='birth',
        ),
    ]