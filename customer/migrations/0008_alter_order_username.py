# Generated by Django 4.0.3 on 2022-04-29 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_remove_orderitem_restaurantid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='username',
            field=models.ForeignKey(default='user', null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.customer_account'),
        ),
    ]
