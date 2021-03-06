# Generated by Django 3.1.7 on 2021-02-19 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('FarmsApp', '0007_auto_20210219_1451'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harvest_wet_weight', models.FloatField()),
                ('harvest_dry_weight', models.FloatField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='harvest_created_by', to=settings.AUTH_USER_MODEL)),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='harvest', to='FarmsApp.farm')),
                ('modified_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='harvest_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HarvestPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('belongs_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='harvest_photo', to='HarvestsApp.harvest')),
                ('created_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='harvest_photo_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='harvest_photo_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
