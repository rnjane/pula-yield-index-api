# Generated by Django 3.1.7 on 2021-02-19 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarmersApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='farmer',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
