# Generated by Django 2.1.5 on 2019-01-21 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll_test_app', '0002_auto_20190121_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='pub_date',
        ),
    ]