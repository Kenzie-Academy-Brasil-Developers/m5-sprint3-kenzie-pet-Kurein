# Generated by Django 4.0.6 on 2022-07-08 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0003_animal_characteristics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='group',
        ),
    ]
