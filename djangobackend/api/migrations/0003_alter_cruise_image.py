# Generated by Django 5.1 on 2024-08-17 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_cruise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cruise',
            name='image',
            field=models.ImageField(default='', upload_to='cruise'),
        ),
    ]
