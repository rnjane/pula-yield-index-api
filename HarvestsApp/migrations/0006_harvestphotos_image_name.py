# Generated by Django 3.1.7 on 2021-02-24 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HarvestsApp', '0005_auto_20210219_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='harvestphotos',
            name='image_name',
            field=models.CharField(default='old image', max_length=30),
            preserve_default=False,
        ),
    ]
