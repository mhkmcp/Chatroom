from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('/', include("chat.urls", namespace="chat")),
    path('admin/', admin.site.urls),
]
