# Generated by Django 2.0.2 on 2018-06-19 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20180616_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.TextField(default=None),
        ),
    ]