# Generated by Django 4.1.7 on 2023-03-21 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='itemname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.CharField(max_length=20, null=True),
        ),
    ]