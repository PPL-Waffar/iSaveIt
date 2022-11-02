# Generated by Django 3.2.7 on 2022-11-02 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_title', models.CharField(blank=True, max_length=250, primary_key=True, serialize=False)),
                ('feedback_feature', models.CharField(choices=[('payment', 'payment'), ('pocket', 'pocket'), ('transaction', 'transaction'), ('expense', 'expense'), ('financialreport', 'financialreport'), ('transaction', 'transaction')], default='payment', max_length=200, null=True)),
                ('feedback_textbox', models.TextField()),
                ('user_feedback', models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
