# Generated by Django 2.2.5 on 2019-09-13 17:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ts', '0004_auto_20190913_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='Ticket_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
