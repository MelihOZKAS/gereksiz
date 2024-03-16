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