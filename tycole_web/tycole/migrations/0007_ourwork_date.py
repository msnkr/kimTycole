# Generated by Django 4.0.4 on 2022-06-07 12:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tycole', '0006_remove_ourwork_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourwork',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
