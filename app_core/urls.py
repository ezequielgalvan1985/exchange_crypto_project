from django.urls import include, path
from rest_framework import routers
from . import views, views_functions

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'wallets', views.WalletViewSet)
router.register(r'wallet-contract', views.WalletContractViewSet)
#router.register(r'wallets-create', views.WalletList.as_view())
urlpatterns = [
    path('', include(router.urls)),
    path('wallet-create/', views_functions.wallet_create)
]