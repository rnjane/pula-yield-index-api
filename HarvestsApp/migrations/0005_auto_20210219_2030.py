# Generated by Django 3.1.7 on 2021-02-19 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FarmsApp', '0007_auto_20210219_1451'),
        ('HarvestsApp', '0004_auto_20210219_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harvest',
            name='farm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='harvest', to='FarmsApp.farm'),
        ),
    ]
