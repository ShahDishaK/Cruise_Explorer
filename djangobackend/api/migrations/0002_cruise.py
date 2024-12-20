# Generated by Django 5.1 on 2024-08-16 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cruise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=100)),
                ('origin', models.CharField(max_length=100)),
                ('departure', models.CharField(max_length=100)),
                ('visiting', models.CharField(max_length=1000)),
                ('nights', models.IntegerField()),
                ('decks', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('country', models.CharField(max_length=100)),
                ('continent', models.CharField(max_length=100)),
                ('image', models.ImageField(default='', upload_to='cruise/images')),
            ],
        ),
    ]
