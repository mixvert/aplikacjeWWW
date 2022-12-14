# Generated by Django 4.1.2 on 2022-10-27 15:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_osoba'),
    ]

    operations = [
        migrations.AddField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='osoba',
            name='miesiac_urodzenia',
            field=models.CharField(choices=[('1', 'Styczeń'), ('2', 'Luty'), ('3', 'Marzec'), ('4', 'Kwiecień'), ('5', 'Maj'), ('6', 'Czerwiec'), ('7', 'Lipiec'), ('8', 'Sierpień'), ('9', 'Wrzesień'), ('10', 'Październik'), ('11', 'Listopad'), ('12', 'Grudzień')], default=1, max_length=2),
        ),
    ]
