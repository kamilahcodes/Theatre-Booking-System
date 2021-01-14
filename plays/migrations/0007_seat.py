# Generated by Django 2.1.7 on 2019-03-19 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plays', '0006_auto_20190319_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='0', max_length=100, unique=True)),
                ('seat_band', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], default=None, max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('vacant', models.BooleanField(default=False)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plays.Viewing')),
            ],
        ),
    ]