from django.test import TestCase
from .models import Bond
from django.test import Client
from django.contrib.auth.models import User

class BondTest(TestCase):
    c = Client()

    def test_api(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        logged_in = self.c.login(username='testuser', password='12345')
        assert logged_in

        data = {
            "isin": "FR0000131104",
            "size": 100000000,
            "currency": "EUR",
            "maturity": "2025-02-28",
            "lei": "R0MUWSFPU8MPRO8K5P83"
            }
        response = self.c.post('/bonds/', data)
        print(response.status_code)
        assert response.status_code == 201

        bond = Bond.objects.get(lei='R0MUWSFPU8MPRO8K5P83')
        assert bond.legal_name == "BNP+PARIBAS"
