# Generated by Django 4.1.3 on 2022-11-15 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_alter_person_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='miesiac_urodzenia',
            field=models.IntegerField(choices=[(1, 'Styczeń'), (2, 'Luty'), (3, 'Marzec'), (4, 'Kwiecień'), (5, 'Maj'), (6, 'Czerwiec'), (7, 'Lipiec'), (8, 'Sierpień'), (9, 'Wrzesień'), (10, 'Październik'), (11, 'Listopad'), (12, 'Grudzień')]),
        ),
    ]
