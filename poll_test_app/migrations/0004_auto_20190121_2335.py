# Generated by Django 2.1.5 on 2019-01-21 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll_test_app', '0003_remove_poll_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='option',
            old_name='option',
            new_name='poll',
        ),
    ]
