# Generated by Django 5.1 on 2024-08-18 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_cruise_cost_alter_cruise_decks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cruisedetailfinal',
            name='InteriorRoomsCost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cruisedetailfinal',
            name='oceanviewRoomsCost',
            field=models.IntegerField(default=0),
        ),
    ]
