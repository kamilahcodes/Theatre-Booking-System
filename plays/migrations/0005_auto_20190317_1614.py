# Generated by Django 2.1.7 on 2019-03-17 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plays', '0004_auto_20190317_1548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='viewing',
            old_name='play_id',
            new_name='play_name',
        ),
    ]
