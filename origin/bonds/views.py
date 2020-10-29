from rest_framework import generics
from rest_framework.response import Response
from rest_framework import authentication, permissions

from django_filters import rest_framework as filters
import django_filters

from .models import Bond
from .serializers import BondSerializer
from .permissions import IsOwner

class BondFilter(filters.FilterSet):
    class Meta:
        model = Bond
        fields = ['legal_name', 'isin', 'lei']

class BondList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = BondSerializer
    filterset_class = BondFilter
    def get_queryset(self):
        return self.request.user.bonds
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BondDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    queryset = Bond.objects.all()
    serializer_class = BondSerializer
    filterset_class = BondFilter
