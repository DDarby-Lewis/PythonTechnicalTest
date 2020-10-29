from django.db import models
from django.contrib.auth.models import User

class Bond(models.Model):
    user =models.ForeignKey(User, related_name='bonds', on_delete=models.CASCADE)
    isin = models.CharField(max_length=20)
    size = models.IntegerField()
    maturity = models.DateField(auto_now=False, auto_now_add=False)
    currency = models.CharField(max_length=5)
    lei = models.CharField(max_length=20)
    legal_name = models.CharField(max_length=20, blank=True, null=True)
    