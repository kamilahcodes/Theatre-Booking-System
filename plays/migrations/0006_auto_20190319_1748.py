# Generated by Django 2.1.7 on 2019-03-19 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plays', '0005_auto_20190317_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewing',
            name='play_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plays.Play'),
        ),
    ]