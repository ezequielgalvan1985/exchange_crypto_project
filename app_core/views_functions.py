from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import WalletSerializer, WalletCreateDtoSerializer


#WALLETS
@api_view(['POST'])
def wallet_create(request):
    if request.method == 'POST':
        #obtener datos del dto
        serializer = WalletCreateDtoSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)