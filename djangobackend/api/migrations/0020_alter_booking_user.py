# Generated by Django 5.1 on 2024-09-09 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_remove_booking_date_booked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.EmailField(default='', max_length=254),
        ),
    ]