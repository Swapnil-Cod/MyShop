# Generated by Django 4.1.7 on 2023-03-03 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
