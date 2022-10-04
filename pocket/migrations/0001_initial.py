# Generated by Django 4.1.1 on 2022-09-21 16:39

from django.db import models
from user.models import *
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pocket',
            fields=[
                ('pocket_name', models.CharField(blank=True, default='Pocket', max_length=50, primary_key=True)),
                ('pocket_budget', models.BigIntegerField(default=False)),
                ('pocket_balance', models.BigIntegerField(default=0)),
                ('user_pocket', models.ForeignKey(default='', on_delete=models.deletion.RESTRICT, to='user.Account')),
            ],
        ),
    ]
