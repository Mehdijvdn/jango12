# Generated by Django 5.0.2 on 2024-02-21 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='visits',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
