# Generated by Django 4.0.4 on 2022-06-03 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tycole', '0002_alter_requestcontact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestcontact',
            name='number',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
