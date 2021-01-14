# Generated by Django 2.1.7 on 2019-03-27 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_shipping'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='discount',
            field=models.ManyToManyField(blank=True, to='cart.Discount'),
        ),
        migrations.AddField(
            model_name='cart',
            name='discountvalue',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AddField(
            model_name='cart',
            name='playstotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AddField(
            model_name='cart',
            name='seattotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AddField(
            model_name='cart',
            name='shipping',
            field=models.ManyToManyField(blank=True, to='cart.Shipping'),
        ),
        migrations.AddField(
            model_name='cart',
            name='shippingtotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='name',
            field=models.CharField(choices=[('Standard Shipping', 'Standard Shipping'), ('First Class', 'First Class'), ('Pick up', 'Pick up')], default=None, max_length=100, null=True),
        ),
    ]
