# Generated by Django 4.1.3 on 2022-11-15 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_person_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls.team', verbose_name='Drużyna'),
        ),
    ]
