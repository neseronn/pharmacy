from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from pharmacy.serializers import *


class MedicineNomenclatureAPIView(ModelViewSet):
    queryset = MedicineNomenclature.objects.all()
    serializer_class = MedicineNomenclatureSerializer


class ReleaseFormAPIView(ModelViewSet):
    queryset = ReleaseForm.objects.all()
    serializer_class = ReleaseFormSerializer


class MedicinesGroupAPIView(ModelViewSet):
    queryset = MedicinesGroup.objects.all()
    serializer_class = MedicinesGroupSerializer


class StaffAPIView(ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class BuyersAPIView(ModelViewSet):
    queryset = Buyers.objects.all()
    serializer_class = BuyersSerializer


class SalesRegistrationAPIView(ModelViewSet):
    queryset = SalesRegistration.objects.all()
    serializer_class = SalesRegistrationSerializer
