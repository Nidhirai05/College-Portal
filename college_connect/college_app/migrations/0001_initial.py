# Generated by Django 5.0.7 on 2024-08-07 07:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.CharField(max_length=100)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
