# Generated by Django 5.0.7 on 2024-08-07 07:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='guest', max_length=45, null=True)),
                ('email', models.EmailField(max_length=50)),
                ('rating', models.CharField(default='5', max_length=5)),
                ('remarks', models.TextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
