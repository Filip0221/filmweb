# Generated by Django 5.1.5 on 2025-01-24 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmweb', '0006_alter_dodatkoweinfo_gatunek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Drama'), (2, 'Komedia'), (1, 'Horro'), (0, 'Inne'), (3, 'Sci-fi')], default=0),
        ),
    ]
