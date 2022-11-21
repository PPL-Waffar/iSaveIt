# Generated by Django 4.1.1 on 2022-11-20 19:37

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
                ('newsletter_text', models.TextField(default='', max_length=10000)),
                ('newsletter_picture', models.ImageField(default='default.jpg', upload_to='newsletter_pictures')),
                ('newsletter_category', models.CharField(default='', max_length=100)),
            ],
        ),
    ]