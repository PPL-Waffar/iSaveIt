# Generated by Django 3.2.7 on 2022-10-08 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_payment_user_payment'),
        ('pocket', '0002_alter_pocket_pocket_name'),
        ('transaction', '0002_transaction_transaction_pocket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='transaction_type_payment',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='transaction_type_transaction',
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_payment_type',
            field=models.ForeignKey(default='NULL', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='payment.payment'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_transaction_type',
            field=models.CharField(choices=[('Expense', 'Expense'), ('Income', 'Income')], default='Expense', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_payment_name',
            field=models.CharField(blank=True, max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_pocket',
            field=models.ForeignKey(default='NULL', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='pocket.pocket'),
        ),
    ]
