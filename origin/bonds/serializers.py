from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Bond
import requests
import urllib

# add serialisers here

class BondSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')
    def create(self, validated_data):
        if 'legal_name' not in validated_data:
            url = "https://leilookup.gleif.org/api/v2/leirecords?lei="+validated_data['lei']
            legal_name = requests.get(url).json()[0]['Entity']['LegalName']['$']
            validated_data['legal_name'] = urllib.parse.quote_plus(legal_name)
        return super().create(validated_data)

    class Meta:
        model = Bond
        fields = ('isin', 'size', 'maturity', 'currency', 'lei', 'legal_name') 
