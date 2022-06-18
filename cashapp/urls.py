from django.urls import include, re_path
from rest_framework import routers
from .views import CashAppListPayments

app_name = 'cashapp_api'

router = routers.DefaultRouter()

urlpatterns = (
    re_path(r'^v1/', include(router.urls)),
    # DEV: https://localhost:4000/v1/cashapp/payments/list
    re_path(r'^v1/cashapp/payments/list/', CashAppListPayments.as_view(), name='cashapp-list-payments'),
)
