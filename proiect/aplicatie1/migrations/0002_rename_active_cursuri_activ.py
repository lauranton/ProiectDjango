# Generated by Django 4.0.4 on 2022-05-16 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cursuri',
            old_name='active',
            new_name='activ',
        ),
    ]
