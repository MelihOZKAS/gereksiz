from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.sitemaps.views import index, sitemap
from blog.views import *
from .sitemaps import *
from .feed import *

sitemaps = {
    'TeknolojiHaberleri': teknolojihaberleri,
    'BilimHaberleri': bilimhaberleri,
    'OtomobilHaberleri': otomobilhaberleri,
    'OyunHaberleri': oyunhaberleri,
    'TelefonHaberleri': telefonaberleri,
    'DiziFilm': dizifilm,
}

def handler404(request, *args, **argv):
    response = render(request, 'yeni-404.html')
    response.status_code = 404
    return response

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path('sitemap.xml', index, {'sitemaps': sitemaps}),
    path('sitemap-<section>.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt", robots_txt, name="robots"),
    #path('feeds', MainHaberleriFeed(), name='feeds_main'),
    path('feeds/teknoloji/', TeknolojiHaberleriFeed(), name='teknoloji_feed'),
    path('feeds/bilim/', BilimHaberleriFeed(), name='bilim_feed'),
    path('feeds/otomobil/', OtomobilHaberleriFeed(), name='otomobil_feed'),
    path('feeds/oyun/', OyunHaberleriFeed(), name='oyun_feed'),
    path('feeds/telefon/', TelefonHaberleriFeed(), name='telefon_feed'),
    path('feeds/diziler-ve-filmler/', DiziFilmFeed(), name='dizi_feed'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
