# Generated by Django 5.1.5 on 2025-01-24 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmweb', '0004_alter_dodatkoweinfo_gatunek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Drama'), (3, 'Sci-fi'), (0, 'Inne'), (2, 'Komedia'), (1, 'Horro')], default=0),
        ),
    ]
