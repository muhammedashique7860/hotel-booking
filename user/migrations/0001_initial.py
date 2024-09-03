# Generated by Django 4.0.5 on 2022-06-24 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminapp', '0002_alter_addroom_status'),
        ('account', '0002_alter_customerdetails_adhar_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.DateField()),
                ('checkout', models.DateField()),
                ('amount', models.FloatField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.customerdetails')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.addroom')),
            ],
        ),
    ]
