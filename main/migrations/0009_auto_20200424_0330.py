# Generated by Django 3.0.5 on 2020-04-23 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200424_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='imageName1',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='main',
            name='imageUrl1',
            field=models.TextField(default=' '),
        ),
    ]