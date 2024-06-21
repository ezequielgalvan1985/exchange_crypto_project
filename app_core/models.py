from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre      = models.CharField(max_length=25, blank=True)
    apellido    = models.CharField(max_length=25, blank=True)
    calle       = models.CharField(max_length=50, blank=True)
    nro         = models.CharField(max_length=10, blank=True)
    piso        = models.CharField(max_length=10, blank=True)
    telefono    = models.CharField(max_length=25, blank=True)
    contacto    = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.nombre


class WalletContract(models.Model):
    address      = models.CharField(max_length=50, blank=False)
    chain_id     = models.IntegerField()
    reserved    = models.BooleanField()
    def __str__(self):
        return self.address

class Wallet(models.Model):
    balance         = models.IntegerField(blank=True, default=0)
    address         = models.CharField(max_length=50, blank=False)
    coin            = models.CharField(max_length=5, blank=False)
    chain_id        = models.IntegerField()
    #wallet_contract = models.ForeignKey(WalletContract,on_delete=models.CASCADE)
    transactions = models.CharField(max_length=50)

    def __str__(self):
        return self.address



class Transaction(models.Model):
    nature     = models.IntegerField(blank=True, default=0)
    tx_hash    = models.CharField(max_length=50)
    amount    = models.DecimalField(decimal_places=2,max_digits=10,max_length=1000000)
    to = models.CharField(max_length=50)
    confirmations = models.IntegerField(blank=True,default=0)
    status = models.IntegerField()
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.tx_hash

class WalletContract(models.Model):
    address      = models.CharField(max_length=50, blank=False)
    reserved      = models.BooleanField()
    chain_id = models.IntegerField()
    def __str__(self):
        return self.address
