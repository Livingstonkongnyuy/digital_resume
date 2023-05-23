# Generated by Django 4.2 on 2023-05-20 00:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='date_created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
