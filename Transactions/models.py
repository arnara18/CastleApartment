from django.db import models
from django.contrib.auth.models import User
from Properties.models import Properties


# Make validation
# Look into built in validators


# Create your models here.
class CreditCard(models.Model):
    cc_number = models.CharField(max_length=19)
    cc_month = models.CharField(max_length=2)
    cc_year = models.CharField(max_length=2)
    cc_code = models.CharField(max_length=3)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Transactions(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    transaction_date = models.DateField(auto_now_add=True, blank=True)
    property = models.ForeignKey(Properties, on_delete=models.DO_NOTHING)
