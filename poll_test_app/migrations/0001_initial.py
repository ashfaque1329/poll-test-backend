# Generated by Django 2.1.5 on 2019-01-21 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('slug_option', models.SlugField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Options',
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('slug_poll', models.SlugField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Polls',
            },
        ),
        migrations.AddField(
            model_name='option',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll_test_app.Poll'),
        ),
    ]
