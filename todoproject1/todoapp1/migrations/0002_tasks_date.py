# Generated by Django 5.0.1 on 2024-01-28 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='date',
            field=models.DateField(default='29-01-2024'),
            preserve_default=False,
        ),
    ]
