# Generated by Django 4.1.1 on 2022-09-21 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pocket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('pay_name', models.CharField(blank=True, max_length=250, primary_key=True, serialize=False)),
                ('pay_amount', models.BigIntegerField(default=False)),
                ('pay_date', models.DateTimeField(auto_now=True)),
                ('payment_choice', models.CharField(choices=[('debit card', 'debit card'), ('cash', 'cash'), ('e-wallet', 'e-wallet')], default='cash', max_length=200)),
                ('pay_categories', models.ForeignKey(default='NULL', on_delete=django.db.models.deletion.SET_DEFAULT, to='pocket.pocket')),
            ],
        ),
    ]