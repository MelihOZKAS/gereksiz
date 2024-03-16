from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post, PostKategori

class TeknolojiHaberleriFeed(Feed):
    title = "Teknoloji Haberleri"
    link = "/feeds/teknoloji/"
    description = "En son teknoloji haberleri."

    def items(self):
        PostKategorisi = PostKategori.objects.get(short_title="Teknoloji")
        return Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=PostKategorisi).order_by('-olusturma_tarihi')[:20]
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.meta_description
    def item_link(self, item):
        return reverse('post-getir', args=[item.slug])
    def item_pubdate(self, item):
        return item.olusturma_tarihi
    def item_author_name(self, item):
        return item.yazar


class BilimHaberleriFeed(Feed):
    title = "Bilim Haberleri"
    link = "/feeds/bilim/"
    description = "En son bilim haberleri."

    def items(self):
        PostKategorisi = PostKategori.objects.get(short_title="Bilim")
        return Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=PostKategorisi).order_by('-olusturma_tarihi')[:20]
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.meta_description
    def item_link(self, item):
        return reverse('post-getir', args=[item.slug])
    def item_pubdate(self, item):
        return item.olusturma_tarihi
    def item_author_name(self, item):
        return item.yazar


class OtomobilHaberleriFeed(Feed):
    title = "Otomobil Haberleri"
    link = "/feeds/otomobil/"
    description = "En son otomobil haberleri."

    def items(self):
        PostKategorisi = PostKategori.objects.get(short_title="Otomobil")
        return Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=PostKategorisi).order_by('-olusturma_tarihi')[:20]
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.meta_description
    def item_link(self, item):
        return reverse('post-getir', args=[item.slug])
    def item_pubdate(self, item):
        return item.olusturma_tarihi
    def item_author_name(self, item):
        return item.yazar

class OyunHaberleriFeed(Feed):
    title = "Oyun Haberleri"
    link = "/feeds/oyun/"
    description = "En son oyun haberleri."

    def items(self):
        PostKategorisi = PostKategori.objects.get(short_title="Oyun")
        return Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=PostKategorisi).order_by('-olusturma_tarihi')[:20]
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.meta_description
    def item_link(self, item):
        return reverse('post-getir', args=[item.slug])
    def item_pubdate(self, item):
        return item.olusturma_tarihi
    def item_author_name(self, item):
        return item.yazar

class TelefonHaberleriFeed(Feed):
    title = "Telefon Haberleri"
    link = "/feeds/telefon/"
    description = "En son telefon haberleri."

    def items(self):
        PostKategorisi = PostKategori.objects.get(short_title="Telefon")
        return Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=PostKategorisi).order_by('-olusturma_tarihi')[:20]
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.meta_description
    def item_link(self, item):
        return reverse('post-getir', args=[item.slug])
    def item_pubdate(self, item):
        return item.olusturma_tarihi
    def item_author_name(self, item):
        return item.yazar


class MainHaberleriFeed(Feed):
    title = "En son teknoloji Haberleri"
    link = "/feeds/"
    description = "Dünyadan anlık teknoloji, bilim, oyun ve otomobil haberleri"

    def items(self):
        return Post.objects.filter(aktif=True, status="Yayinda").order_by('-olusturma_tarihi')[:50]
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.meta_description
    def item_link(self, item):
        return reverse('post-getir', args=[item.slug])
    def item_pubdate(self, item):
        return item.olusturma_tarihi
    def item_author_name(self, item):
        return item.yazar