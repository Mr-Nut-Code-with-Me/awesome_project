from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', views.frontpage, name='frontpage'),
    path('about/', views.aboutpage, name='aboutpage'),
]
