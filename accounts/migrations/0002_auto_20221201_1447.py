# Generated by Django 3.2.13 on 2022-12-01 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_music_channel',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_music_title',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]