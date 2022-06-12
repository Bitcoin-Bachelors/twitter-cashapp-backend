from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("twitter.urls")),
    path('', include("auth.urls")),
    path('', include("cashapp.urls"))
]
