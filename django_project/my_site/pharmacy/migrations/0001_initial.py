# Generated by Django 4.1.4 on 2023-01-08 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio_buyer', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='MedicineNomenclature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('prescription', models.BooleanField(default=False)),
                ('dosage', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MedicinesGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ReleaseForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio_employee', models.CharField(max_length=60)),
                ('salary', models.IntegerField()),
                ('employment_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SalesRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('cost', models.FloatField()),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pharmacy.buyers')),
                ('medicine', models.ManyToManyField(blank=True, to='pharmacy.medicinenomenclature')),
            ],
        ),
        migrations.AddField(
            model_name='medicinenomenclature',
            name='medicines_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pharmacy.medicinesgroup'),
        ),
        migrations.AddField(
            model_name='medicinenomenclature',
            name='release_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pharmacy.releaseform'),
        ),
    ]
