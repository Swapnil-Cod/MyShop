# Generated by Django 4.1.7 on 2023-04-07 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0012_checkout_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='paymentsignature',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]