from django.urls import include, re_path
from rest_framework import routers
from .views import InitiateTwitterAuth, TwitterAuthCallback, TwitterLogOut, InitiateCashAppAuth, CashAppAuthCallback

app_name = 'auth'

router = routers.DefaultRouter()

urlpatterns = (
    re_path(r'^v1/', include(router.urls)),
    # DEV: https://localhost:4000/v1/auth/twitter/authorize/ & https://localhost:4000/v1/auth/twitter/callback/
    re_path(r'^v1/auth/twitter/authorize/', InitiateTwitterAuth.as_view(), name='twitter-auth-authorize'),
    re_path(r'^v1/auth/twitter/callback/', TwitterAuthCallback.as_view(), name='twitter-auth-callback'),

    # DEV: https://localhost:4000/v1/auth/cashapp/authorize/
    re_path(r'^v1/auth/cashapp/authorize/', InitiateCashAppAuth.as_view(), name='cashapp-auth-authorize'),
    re_path(r'^v1/auth/cashapp/callback/', CashAppAuthCallback.as_view(), name='cashapp-auth-callback'),

    # DEV: https://localhost:4000/v1/auth/logout
    re_path(r'^v1/auth/logout/', TwitterLogOut.as_view(), name='twitter-auth-logout'),
)
