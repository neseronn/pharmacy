from rest_framework import serializers

from pharmacy.models import *


class MedicineNomenclatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineNomenclature
        fields = '__all__'


class ReleaseFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReleaseForm
        fields = '__all__'


class MedicinesGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicinesGroup
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class BuyersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyers
        fields = '__all__'


class SalesRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesRegistration
        fields = '__all__'
