# Generated by Django 4.0.4 on 2022-05-16 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursuri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumeCurs', models.CharField(max_length=100)),
                ('ProfCurs', models.CharField(max_length=100)),
                ('DescriereCurs', models.CharField(max_length=300)),
                ('active', models.BooleanField(default=1)),
            ],
        ),
    ]
