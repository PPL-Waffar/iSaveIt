# Generated by Django 4.1.1 on 2022-12-23 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pocket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pocket',
            name='pocket_default',
            field=models.BigIntegerField(default=0),
        ),
    ]
