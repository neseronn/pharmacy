from django.db import models


class MedicineNomenclature(models.Model):
    title = models.CharField(null=False, max_length=50)
    release_form = models.ForeignKey("ReleaseForm", on_delete=models.PROTECT, null=False)
    medicines_group = models.ForeignKey("MedicinesGroup", on_delete=models.PROTECT, null=False)
    prescription = models.BooleanField(default=False)
    dosage = models.IntegerField()
    price = models.FloatField(null=False)

    def __str__(self):
        return self.title


class ReleaseForm(models.Model):
    title = models.CharField(null=False, max_length=30)

    def __str__(self):
        return self.title


class MedicinesGroup(models.Model):
    group_name = models.CharField(null=False, max_length=50)

    def __str__(self):
        return self.group_name


class Staff(models.Model):
    fio_employee = models.CharField(null=False, max_length=60)
    salary = models.IntegerField(null=False)
    employment_date = models.DateField(null=False)

    def __str__(self):
        return self.fio_employee


class Buyers(models.Model):
    fio_buyer = models.CharField(null=False, max_length=60)
    email = models.CharField(null=False, max_length=30)
    phone_number = models.CharField(null=False, max_length=12)

    def __str__(self):
        return self.fio_buyer


class SalesRegistration(models.Model):
    medicine = models.ManyToManyField(MedicineNomenclature, blank=True)     # ??
    count = models.IntegerField(null=False)
    buyer = models.ForeignKey("Buyers", on_delete=models.PROTECT)
    cost = models.FloatField(null=False)

