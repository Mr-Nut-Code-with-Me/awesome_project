from django.contrib import admin
from django.urls import path, include
from core import views


from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from .sitemaps import CategorySitemap, PostSitemap


sitemaps = {'category': CategorySitemap, 'post': PostSitemap}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('admin/', admin.site.urls),
    path('', views.frontpage, name='frontpage'),
    path('about/', views.aboutpage, name='aboutpage'),
    path('', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
