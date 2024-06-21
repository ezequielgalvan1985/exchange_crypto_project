from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Wallet, WalletContract


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class WalletSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'


class WalletContractSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WalletContract
        fields = '__all__'



class WalletCreateDtoSerializer(serializers.Serializer):
    chain_id = serializers.IntegerField()
    coin     = serializers.CharField(max_length=5)
