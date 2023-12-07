from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import *

class teknolojihaberleri(Sitemap):
    changefreq = "daily"
    priority = 1.0
    protocol = 'https'

    def items(self):
        PostKategorisi = PostKategori.objects.get(short_title="Teknoloji")
        return Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=PostKategorisi)

    def lastmod(self, obj):
        return obj.guncelleme_tarihi

    def location(self, obj):
        return reverse('post-getir', args=[obj.slug])

class bilimhaberleri(Sitemap):
    changefreq = "daily"
    priority = 1.0
    protocol = 'https'

    def items(self):
        PostKategorisi = PostKategori.objects.get(short_title="Bilim")
        return Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=PostKategorisi)

    def lastmod(self, obj):
        return obj.guncelleme_tarihi

    def location(self, obj):
        return reverse('post-getir', args=[obj.slug])


class otomobilhaberleri(Sitemap):
    changefreq = "daily"
    priority = 1.0
    protocol = 'https'

    def items(self):
        PostKategorisi = PostKategori.objects.get(short_title="Otomobil")
        return Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=PostKategorisi)

    def lastmod(self, obj):
        return obj.guncelleme_tarihi

    def location(self, obj):
        return reverse('post-getir', args=[obj.slug])

class oyunhaberleri(Sitemap):
    changefreq = "daily"
    priority = 1.0
    protocol = 'https'

    def items(self):
        PostKategorisi = PostKategori.objects.get(short_title="Oyun")
        return Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=PostKategorisi)

    def lastmod(self, obj):
        return obj.guncelleme_tarihi

    def location(self, obj):
        return reverse('post-getir', args=[obj.slug])