# Generated by Django 2.1.7 on 2019-03-21 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plays', '0010_seat_auditorium'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='auditorium',
        ),
        migrations.RemoveField(
            model_name='viewing',
            name='auditorium',
        ),
        migrations.AddField(
            model_name='seat',
            name='viewing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='plays.Viewing'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='price',
            field=models.DecimalField(choices=[('30.00', '30.00'), ('20.00', '20.00'), ('10.00', '10.00')], decimal_places=2, max_digits=20),
        ),
        migrations.DeleteModel(
            name='Auditorium',
        ),
    ]
