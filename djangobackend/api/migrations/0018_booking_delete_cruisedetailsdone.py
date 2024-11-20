# Generated by Django 5.1 on 2024-09-07 14:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_cruisedetailsdone'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(max_length=100)),
                ('room_number', models.IntegerField()),
                ('date_booked', models.DateTimeField(auto_now_add=True)),
                ('cruise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cruisedetailfinal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='CruiseDetailsDone',
        ),
    ]