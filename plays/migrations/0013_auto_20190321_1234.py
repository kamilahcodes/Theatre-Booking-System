# Generated by Django 2.1.7 on 2019-03-21 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plays', '0012_auto_20190321_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='a name', max_length=100)),
                ('play', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plays.Play')),
            ],
        ),
        migrations.AlterField(
            model_name='seat',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AddField(
            model_name='reservation',
            name='seat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plays.Seat'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='view',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plays.Viewing'),
        ),
    ]
