from django.db import models


class MedicineNomenclature(models.Model):
    title = models.CharField(null=False, max_length=50)
    release_form = models.ForeignKey("ReleaseForm", on_delete=models.PROTECT, null=False)
    medicines_group = models.ForeignKey("MedicinesGroup", on_delete=models.PROTECT, null=False)
    prescription = models.BooleanField(default=False)
    dosage = models.IntegerField()
    price = models.FloatField(null=False)


class ReleaseForm(models.Model):
    title = models.CharField(null=False, max_length=30)


class MedicinesGroup(models.Model):
    models.CharField(null=False, max_length=50)


class Staff(models.Model):
    fio_employee = models.CharField(null=False, max_length=60)
    salary = models.IntegerField(null=False)
    employment_date = models.DateField(null=False)


class Buyers(models.Model):
    fio_buyer = models.CharField(null=False, max_length=60)
    email = models.CharField(null=False, max_length=30)
    phone_number = models.CharField(null=False, max_length=12)


class SalesRegistration(models.Model):
    medicine = models.ForeignKey("MedicineNomenclature", on_delete=models.PROTECT, null=False)
    count = models.IntegerField(null=False)
    buyer = models.ForeignKey("Buyers", on_delete=models.PROTECT)
    cost = models.FloatField(null=False)

