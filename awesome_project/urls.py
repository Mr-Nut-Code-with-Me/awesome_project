from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.frontpage, name='frontpage'),
    path('about/', views.aboutpage, name='aboutpage')
]
