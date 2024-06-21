from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Wallet, WalletContract
from .serializers import GroupSerializer, UserSerializer, WalletSerializer, WalletContractSerializer, \
    WalletCreateDtoSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all().order_by('coin')
    serializer_class = WalletSerializer
    #permission_classes = [permissions.IsAuthenticated]


class WalletContractViewSet(viewsets.ModelViewSet):
    queryset = WalletContract.objects.all().order_by('address')
    serializer_class = WalletContractSerializer
