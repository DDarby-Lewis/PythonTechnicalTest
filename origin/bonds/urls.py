from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', BondList.as_view(), name="bond_list"),
    path('<str:pk>/', BondDetail.as_view(), name="bond_detail")
]
