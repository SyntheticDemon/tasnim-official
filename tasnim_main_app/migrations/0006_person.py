# Generated by Django 3.2.7 on 2021-10-07 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasnim_main_app', '0005_auto_20211007_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(max_length=200, verbose_name='نام شخص')),
                ('card_numbers', models.TextField()),
                ('total_donations', models.IntegerField(default=0)),
            ],
        ),
    ]
