# Generated by Django 5.1 on 2024-11-02 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cec', '0010_remove_operatorreport_acbe_operatorreport_acae_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='operatorreport',
            name='Month',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='operatorreport',
            name='Year',
            field=models.IntegerField(default=2001),
        ),
    ]
