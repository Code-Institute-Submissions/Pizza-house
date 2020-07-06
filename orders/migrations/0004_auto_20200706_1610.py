# Generated by Django 3.0.7 on 2020-07-06 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_merge_20200701_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartorder',
            name='order_state',
        ),
        migrations.AddField(
            model_name='cartorder',
            name='cart_state',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('PROCCESSING', 'Proccessing'), ('DELIVERING', 'Delivering')], default='PENDING', max_length=32),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order_item_state',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('PROCCESSING', 'Proccessing'), ('DELIVERING', 'Delivering')], default='PENDING', max_length=32),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.DeleteModel(
            name='CartOrderState',
        ),
        migrations.DeleteModel(
            name='OrderItemState',
        ),
    ]