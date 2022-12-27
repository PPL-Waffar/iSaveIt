# Generated by Django 4.1.1 on 2022-12-27 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsletter_title', models.TextField(default='', max_length=100)),
                ('newsletter_text', models.TextField(default='', max_length=10000)),
                ('newsletter_picture', models.ImageField(blank=True, null=True, upload_to='newsletter/pictures/')),
                ('newsletter_category', models.CharField(choices=[('tips', 'tips'), ('news', 'news')], default='tips', max_length=10)),
            ],
        ),
    ]
