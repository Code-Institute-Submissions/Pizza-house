# Generated by Django 3.0 on 2020-07-26 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200715_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='extra',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='food',
        ),
        migrations.DeleteModel(
            name='CartOrder',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
        migrations.DeleteModel(
            name='Payments',
        ),
    ]
