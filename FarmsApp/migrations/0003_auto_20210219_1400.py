# Generated by Django 3.1.7 on 2021-02-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarmsApp', '0002_auto_20210219_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='farm_size_units',
            field=models.CharField(choices=[(1, 'Acres'), (2, 'Hectares'), (3, 'Meter Squared')], default=1, max_length=20),
        ),
    ]