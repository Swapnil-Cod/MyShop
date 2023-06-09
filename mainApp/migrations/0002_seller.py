# Generated by Django 4.1.7 on 2023-03-02 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('addressline1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('addressline2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('addressline3', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pin', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('city', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('state', models.CharField(blank=True, default=None, max_length=20, null=True)),
            ],
        ),
    ]
