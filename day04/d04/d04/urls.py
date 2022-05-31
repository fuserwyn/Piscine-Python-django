from django.urls import include
from django.contrib import admin
from django.urls import path
from ex00.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ex00/', include('ex00.urls')),
    path('ex01/', include('ex01.urls')),
path('ex02/', include('ex02.urls')),
]