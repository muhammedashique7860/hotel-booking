# Generated by Django 4.0.5 on 2022-06-15 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetails',
            name='adhar',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='phnno',
            field=models.BigIntegerField(),
        ),
    ]
