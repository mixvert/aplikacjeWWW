# Generated by Django 4.1.2 on 2022-11-03 15:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_team_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='country',
            field=models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
