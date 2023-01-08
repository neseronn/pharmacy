from django.contrib import admin
from django.urls import path, include

from pharmacy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('api/v1/medicine_nomenclature/',
         MedicineNomenclatureAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/medicine_nomenclature/<int:pk>/',
         MedicineNomenclatureAPIView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('api/v1/release_form/',
         ReleaseFormAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/release_form/<int:pk>/',
         ReleaseFormAPIView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('api/v1/medicines_group/',
         MedicinesGroupAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/medicines_group/<int:pk>/',
         MedicinesGroupAPIView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('api/v1/staff/',
         StaffAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/staff/<int:pk>/',
         StaffAPIView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('api/v1/buyers/',
         BuyersAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/buyers/<int:pk>/',
         BuyersAPIView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('api/v1/sales_registration/',
         SalesRegistrationAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/sales_registration/<int:pk>/',
         SalesRegistrationAPIView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
