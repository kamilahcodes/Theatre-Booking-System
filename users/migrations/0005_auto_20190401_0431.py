# Generated by Django 2.1.7 on 2019-04-01 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190312_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='agency_name',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
