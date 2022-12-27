# Generated by Django 4.1.1 on 2022-12-27 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pocket', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_name', models.CharField(max_length=50)),
                ('expense_amount', models.BigIntegerField(default=False)),
                ('expense_date', models.DateField()),
                ('expense_type', models.CharField(choices=[('Lend Money', 'Lend Money'), ('Debt', 'Debt')], default='Lend Money', max_length=200, null=True)),
                ('expense_person', models.CharField(max_length=50)),
                ('expense_payment_choice', models.CharField(choices=[('debit card', 'debit card'), ('cash', 'cash'), ('e-wallet', 'e-wallet')], default='cash', max_length=200, null=True)),
                ('expense_pocket', models.ForeignKey(default='NULL', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='pocket.pocket')),
                ('user_expense', models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
