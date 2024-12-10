# Generated by Django 5.1 on 2024-10-28 07:04

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cec', '0002_survey_deadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='deadline',
        ),
        migrations.AddField(
            model_name='survey',
            name='opening',
            field=models.DateField(default=datetime.datetime(2024, 1, 1, 0, 0)),
        ),
        migrations.AlterField(
            model_name='entry',
            name='end',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='entry',
            name='start',
            field=models.CharField(max_length=1000),
        ),
        migrations.CreateModel(
            name='OperatorEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='excel')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cec.survey')),
            ],
        ),
    ]