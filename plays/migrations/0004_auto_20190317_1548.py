# Generated by Django 2.1.7 on 2019-03-17 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plays', '0003_auto_20190316_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewing',
            name='play_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views', to='plays.Play'),
        ),
    ]
