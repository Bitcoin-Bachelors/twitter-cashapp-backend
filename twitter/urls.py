from django.urls import include, re_path
from rest_framework import routers
from .views import TwitterDirectMessageListView, TwitterDirectMessageGetView, TwitterDirectMessageRemoveView, TwitterDirectMessageSendView

app_name = 'api'

router = routers.DefaultRouter()

urlpatterns = (
    re_path(r'^v1/', include(router.urls)),
    # DEV: https://localhost:4000/v1/twitter/direct_message/list/
    re_path(r'^v1/twitter/direct_message/list/', TwitterDirectMessageListView.as_view(), name='twitter-direct-message-list'),
    # DEV: https://localhost:4000/v1/twitter/direct_message/get/
    re_path(r'^v1/twitter/direct_message/get/', TwitterDirectMessageGetView.as_view(), name='twitter-direct-message-get'),
    # DEV: https://localhost:4000/v1/twitter/direct_message/send/
    re_path(r'^v1/twitter/direct_message/send/', TwitterDirectMessageSendView.as_view(), name='twitter-direct-message-send'),
    # DEV: https://localhost:4000/v1/twitter/direct_message/remove/
    re_path(r'^v1/twitter/direct_message/remove/', TwitterDirectMessageRemoveView.as_view(), name='twitter-direct-message-remove'),
)
