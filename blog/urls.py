from django.urls import path
from . import views

urlpatterns = [
    path('<slug:category>/<slug:slug>/', views.detailview, name="detailpage"),
    path('<slug:slug>/', views.categoryview, name="categorypage")
]
