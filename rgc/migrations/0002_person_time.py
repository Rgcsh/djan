# Generated by Django 2.0.8 on 2018-09-17 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rgc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]