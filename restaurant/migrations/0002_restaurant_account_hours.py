# Generated by Django 4.0.3 on 2022-05-05 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant_account',
            name='hours',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]