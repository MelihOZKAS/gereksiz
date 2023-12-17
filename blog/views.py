from django.shortcuts import render, HttpResponse, get_object_or_404, reverse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET
from django.views import View
from django.http import JsonResponse
import json





def create_unique_title_slug(title):
    slug = slugify(title)
    unique_slug = slug
    unique_title = title
    num = 1
    while Kontrol.objects.filter(slug=unique_slug).exists() or Kontrol.objects.filter(title=unique_title).exists():
        unique_slug = '{}-{}'.format(slug, num)
        unique_title = '{} {}'.format(title, num)
        num += 1
    return unique_title, unique_slug
def home(request):
    title = "En Son Teknoloji, Bilim, Oyun ve Otomobil Haberleri"
    description = "En son teknoloji haberlerini, ürün incelemelerini, teknoloji trendlerini ve daha fazlasını sunar. Teknoloji dünyasındaki en son gelişmeleri kaçırmayın yuksektekloji.com"
    keywords = "teknoloji, haberler, incelemeler, gadgetlar, bilim, inovasyon, AI, VR, AR, mobil teknoloji, bilgisayarlar, yazılım, donanım, otomobil, oyuni bilim"
    yazar = "Yüksek Teknoloji"


    Banner = Post.objects.filter(aktif=True, status="Yayinda", banner=True).order_by(
        '-olusturma_tarihi')[:8]

    TeknolojiKategori = get_object_or_404(PostKategori, short_title="Teknoloji")
    TrendTeknoji8 = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=TeknolojiKategori, editor=True).order_by(
        '-olusturma_tarihi')[:8]
    HomeTeknolojiSol = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=TeknolojiKategori).order_by(
        '-olusturma_tarihi')[:3]
    HomeTeknolojiSag = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=TeknolojiKategori).order_by(
        '-olusturma_tarihi')[3:6]

    BilimKategori = get_object_or_404(PostKategori, short_title="Bilim")
    TrendBilim8 = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=BilimKategori, editor=True).order_by(
        '-olusturma_tarihi')[:8]
    HomeBilimSol = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=BilimKategori).order_by(
        '-olusturma_tarihi')[:3]
    HomeBilimSag = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=BilimKategori).order_by(
        '-olusturma_tarihi')[3:6]

    OtoKategori = get_object_or_404(PostKategori, short_title="Otomobil")
    TrendOto8 = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=OtoKategori, editor=True).order_by(
        '-olusturma_tarihi')[:8]
    HomeOtoSol = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=OtoKategori).order_by(
        '-olusturma_tarihi')[:3]
    HomeOtoSag = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=OtoKategori).order_by(
        '-olusturma_tarihi')[3:6]

    OyunKategori = get_object_or_404(PostKategori, short_title="Oyun")
    TrendOyun8 = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=OyunKategori, editor=True).order_by(
        '-olusturma_tarihi')[:8]
    HomeOyunSol = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=OyunKategori).order_by(
        '-olusturma_tarihi')[:3]
    HomeOyunSag = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=OyunKategori).order_by(
        '-olusturma_tarihi')[3:6]

    context = {
        'title': title,
        'description': description,
        'keywords': keywords,
        'yazar': yazar,

        'Banner': Banner,

        'TrendTeknoji8': TrendTeknoji8,
        'HomeTeknolojiSol': HomeTeknolojiSol,
        'HomeTeknolojiSag': HomeTeknolojiSag,

        'TrendBilim8': TrendBilim8,
        'HomeBilimSol': HomeBilimSol,
        'HomeBilimSag': HomeBilimSag,

        'TrendOto8': TrendOto8,
        'HomeOtoSol': HomeOtoSol,
        'HomeOtoSag': HomeOtoSag,

        'TrendOyun8': TrendOyun8,
        'HomeOyunSol': HomeOyunSol,
        'HomeOyunSag': HomeOyunSag,

    }
    return render(request, 'Hepsi/home.html', context)


def KategoriHome(request):
    if request.resolver_match.url_name == 'teknoloji':
        # Teknoloji haberleri için kod
        Post_Kategorisi = get_object_or_404(PostKategori, short_title="Teknoloji")
        TumPost = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=Post_Kategorisi).order_by(
            '-olusturma_tarihi')

    elif request.resolver_match.url_name == 'bilim':
        # Bilim haberleri için kod
        Post_Kategorisi = get_object_or_404(PostKategori, short_title="Bilim")
        TumPost = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=Post_Kategorisi).order_by(
            '-olusturma_tarihi')

    elif request.resolver_match.url_name == 'otomobil':
        # Otomobil haberleri için kod
        Post_Kategorisi = get_object_or_404(PostKategori, short_title="Otomobil")
        TumPost = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=Post_Kategorisi).order_by(
            '-olusturma_tarihi')

    elif request.resolver_match.url_name == 'oyun':
        # Oyun haberleri için kod
        Post_Kategorisi = get_object_or_404(PostKategori, short_title="Oyun")
        TumPost = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=Post_Kategorisi).order_by(
            '-olusturma_tarihi')



    populer = Post.objects.filter(aktif=True, status="Yayinda", banner=True).order_by('-olusturma_tarihi')[:8]
    editor = Post.objects.filter(aktif=True, status="Yayinda", editor=True).order_by('-olusturma_tarihi')[:8]
    enson = Post.objects.filter(aktif=True, status="Yayinda").order_by('-olusturma_tarihi')[:8]

    title = Post_Kategorisi.Title
    description = Post_Kategorisi.description
    keywords = Post_Kategorisi.keywords

    paginator = Paginator(TumPost, 10)  # 10 içerik göstermek için
    page_number = request.GET.get('sayfa')
    TumPost = paginator.get_page(page_number)

    if page_number is None:
        title = f"{title}"
        description = f"{description}"
    else:
        title = f"{title} - {page_number}"
        description = f"{description} - Sayfa {page_number}"

    context = {
        'title': title,
        'description': description,
        'keywords': keywords,
        'Post_Kategorisi': Post_Kategorisi,
        'TumPost': TumPost,
        'populer': populer,
        'editor': editor,
        'enson': enson,

    }
    return render(request, 'Hepsi/blog-list.html', context)
    # return render(request, 'Hepsi/home.html', context)


# YouTube video URL'sinden video ID'sini çıkaran bir regex deseni
def get_youtube_id(url):
    # YouTube video URL'sinden video ID'sini çıkaran bir regex deseni
    link = url.replace("https://www.youtube.com/embed/","")
    youtube_id = link.split("?")
    return youtube_id[0] if youtube_id else None

def Enderun(request, post_slug):
    PostEndrun = get_object_or_404(Post, aktif=True, status="Yayinda", slug=post_slug)

    PostEndrun.okunma_sayisi += 1
    PostEndrun.save()

    populer = Post.objects.filter(aktif=True, status="Yayinda", banner=True).order_by(
        '-olusturma_tarihi')[:8]
    editor = Post.objects.filter(aktif=True, status="Yayinda", editor=True).order_by(
        '-olusturma_tarihi')[:8]
    enson = Post.objects.filter(aktif=True, status="Yayinda").order_by('-olusturma_tarihi')[:8]

    title = PostEndrun.title
    description = PostEndrun.meta_description
    keywords = PostEndrun.keywords

    thumbnail_url = None

    if PostEndrun.youtube:
        youtube_id = get_youtube_id(PostEndrun.youtube)
        thumbnail_url = f"https://img.youtube.com/vi/{youtube_id}/0.jpg"

    #
    context = {
        'title': title,
        'description': description,
        'keywords': keywords,
        'icerik': PostEndrun,
        'populer': populer,
        'editor': editor,
        'enson': enson,
        'thumbnail_url': thumbnail_url,
    }
    return render(request, 'Hepsi/enderun.html', context)


def iletisim(request):
    print("girdim")

    title = "İletişim - YüksekTeknoloji.com Haberin Adresi | Bize Ulaşın"
    description = "Explore KidsStoriesHub.com for captivating bedtime stories. Dive into a world of imagination and learning with our vast collection of stories for children."
    keywords = "Teknoloji haberleri, Oyuncu haberleri, otomobil haberleri, oyun haberleri"
    h1 = "YüksekTeknoloji.com İletişim Bize Ulaşın"

    if request.method == 'POST':
        print("girdim2")
        name = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('title')
        icerik = request.POST.get('icerik')

        iletisim = iletisimmodel(name=name, email=email, title=title, icerik=icerik)
        iletisim.save()
        return HttpResponse(
            'Başarılı ! - İletişim istediğinizi Kaydettik. <a href="{}" class="btn btn-success">Ana Sayfaya Dönmek için Tıklayın.</a>'.format(
                reverse('home')))
        # Burada başarılı form gönderimi sonrası yapılacak işlemler yer alabilir.

    context = {
        'title': title,
        'description': description,
        'keywords': keywords,
        'h1': h1,
    }
    return render(request, 'Hepsi/iletisim.html', context)


def hakkinda(request):
    title = "Hakkımızda YüksekTeknoloji.com | Türkiye’nin Öncü Teknoloji Platformu"
    description = "YüksekTeknoloji.com, Türkiye’nin en güncel teknoloji haberlerini, incelemelerini ve analizlerini sunan öncü bir platformdur. Teknoloji haberlerinin yeni adresi"
    keywords = "Teknoloji haberleri, araba haberleri, otomobil haberleri, oyun haberleri"
    h1 = "YüksekTeknoloji.com Hakkında: Türkiye’nin Öncü Teknoloji Haberleri Platformu"
    context = {
        'title': title,
        'description': description,
        'keywords': keywords,
        'h1': h1,
    }
    return render(request, 'Hepsi/hakkinda.html', context)


def cerez(request):
    title = "Çerez Politikası YüksekTeknoloji.com | Gizlilik ve Çerezler"
    description = "YüksekTeknoloji.com çerez politikası. Web sitemizdeki deneyiminizi geliştirmek için çerezleri nasıl kullandığımızı öğrenin.Yeni en son teknoloji haberleri"
    keywords =  "Teknolojik haberler, araba fiyatları haberleri, otomobil haberleri, oyun haberleri"
    h1 = "YüksekTeknoloji.com Çerez Politikası Gizliliğinize Saygı Duyuyoruz"
    context = {
        'title': title,
        'description': description,
        'keywords': keywords,
        'h1': h1,
    }
    return render(request, 'Hepsi/cerez.html', context)


def gizlilik(request):
    title = "Gizlilik YüksekTeknoloji.com | Bilgilerinizin Korunması"
    description = "YüksekTeknoloji.com gizlilik politikası Kişisel bilgilerinizin nasıl korunduğunu ve kullanıldığını öğrenin. Kullanıcılarımızın gizliliği bizim için en önemlidir"
    keywords = "Gizlilik Politikası, YüksekTeknoloji.com, Kişisel Bilgiler, Veri Koruma, Kullanıcı Gizliliği"
    h1 = "YüksekTeknoloji.com Gizlilik Politikası: Kişisel Bilgileriniz Güvende"
    context = {
        'title': title,
        'description': description,
        'keywords': keywords,
        'h1': h1,
    }
    return render(request, 'Hepsi/gizlilik.html', context)


def kullanim(request):
    title = "Kullanım Koşulları YüksekTeknoloji.com | Kullanım Şartları"
    description = "Kullanım koşulları. Sitemizi kullanırken şartlara uymanız gerektiğini öğrenin. Kullanıcılarımızın güvenliği ve memnuniyeti bizim için önemlidir. Teknoloji"
    keywords = "Kullanım Koşulları, YüksekTeknoloji.com, Web Site Kullanımı, Güvenlik, Kullanıcı Memnuniyeti"
    h1 = "YüksekTeknoloji.com Kullanım Koşulları: Web Sitemizi Güvenle Kullanın"
    context = {
        'title': title,
        'description': description,
        'keywords': keywords,
        'h1': h1,
    }
    return render(request, 'Hepsi/kullanim.html', context)


@require_GET
def robots_txt(request):
    return HttpResponse(robots_txt_content, content_type="text/plain")


robots_txt_content = """
User-agent: *
Allow: /
Sitemap: https://www.yuksekteknoloji.com/sitemap.xml
"""


class StoryPreviewView(View):
    def get(self, request, *args, **kwargs):
        story = Kontrol.objects.get(slug=kwargs['slug'])

        # Veritabanından bilgileri çek
        title = story.title
        h1 = story.h1
        keywords = story.keywords
        description = story.meta_description

        # İçeriği oluştur
        content = f"Title: {title}\n\n <br> H1: {h1}\n\n <br> Keywords: {keywords}\n\n <br> Description: {description}\n\n <br> {story.icerik}"

        return HttpResponse(content)


@csrf_exempt
def post_add(request):
    if request.method == 'POST':
        # Gelen POST isteğindeki değerleri alın
        title = request.POST.get('title')
        h1 = request.POST.get('h1')
        Post_Turu = request.POST.get('Post_Turu')
        icerik = request.POST.get('icerik')
        meta_description = request.POST.get('meta_description')
        key = request.POST.get('keywords')
        Kaynak_Linki = request.POST.get('Kaynak_Linki')

        Post_Turu_Gelen = PostKategori.objects.get(short_title=Post_Turu)

        title, slug = create_unique_title_slug(title)
        siir_masal = Kontrol(title=title,  slug=slug, h1=h1, Post_Turu=Post_Turu_Gelen, icerik=icerik,keywords=key , meta_description=meta_description, Akibeti="Beklemede", Kaynak_Linki=Kaynak_Linki)
        siir_masal.save()
        if siir_masal.id is None:
            return HttpResponse("Post kaydedilemedi.")
        else:
            return HttpResponse("Post başarıyla kaydedildi. ID: " + str(siir_masal.id))

@csrf_exempt
def real_post_add(request):
    if request.method == 'POST':
        # Gelen POST isteğindeki değerleri alın
        title = request.POST.get('title')
        hiddenTitle = request.POST.get('hiddenTitle')
        h1 = request.POST.get('h1')
        hiddenH1 = request.POST.get('hiddenH1')
        Post_Turu = request.POST.get('Post_Turu')
        icerik = request.POST.get('icerik')
        meta_description = request.POST.get('meta_description')
        hiddenKeys = request.POST.get('hiddenKeys')
        Kaynak_Linki = request.POST.get('Kaynak_Linki')
        info = request.POST.get('info')
        GelenID = request.POST.get('GelenID')

        Post_Turu_Gelen = PostKategori.objects.get(short_title=Post_Turu)

        title, slug = create_unique_title_slug(title)
        siir_masal = Post(title=title, hiddenTitle=hiddenTitle,  slug=slug, h1=h1, hiddenH1=hiddenH1, Post_Turu=Post_Turu_Gelen, icerik=icerik, info=info, hiddenKeys=hiddenKeys, meta_description=meta_description, Kaynak_Linki=Kaynak_Linki)
        siir_masal.save()

        Kontrol.objects.filter(id=GelenID).update(Akibeti="Tamamlandi")

        if siir_masal.id is None:
            return HttpResponse("Post kaydedilemedi.")
        else:
            return HttpResponse("Şükürler Olsun Post başarıyla kaydedildi. ID: " + str(siir_masal.id))



@csrf_exempt
def mahsulyakala(request):
    if request.method == 'POST':
        if request.headers.get('Content-Type') == 'application/json':
            data = json.loads(request.body)
            for item in data:
                Main_Link = item.get('Main_Link')
                Post_Link = item.get('Post_Link')
                mahsulkayit = Mahsul(Tarla_Link=Main_Link, Mahsul_Link=Post_Link, Akibeti='Beklemede')
                mahsulkayit.save()
            return JsonResponse({"message": "Başarılı"})
        else:
            return JsonResponse({"error": "Geçersiz Content-Type başlığı"}, status=400)
    else:
        return JsonResponse({"method": request.method, "headers": dict(request.headers)})


@csrf_exempt
def mahsullistesicek(request):
    if request.method == 'POST':
        tarla_link = request.POST.get('Tarla_Link')
        mahsul_list = Mahsul.objects.filter(Tarla_Link=tarla_link).order_by('-olusturma_tarihi')[:50]
        mahsul_links = "|".join([mahsul.Mahsul_Link for mahsul in mahsul_list])
        return HttpResponse(mahsul_links)
    else:
        return HttpResponse("Geçersiz istek", status=400)




@csrf_exempt
def mahsulcek(request):
    if request.method == 'POST':
        tarla_link = request.POST.get('Tarla_Link')
        mahsul_cek = Mahsul.objects.filter(Tarla_Link=tarla_link, Akibeti="Beklemede").order_by('olusturma_tarihi').first()
        if mahsul_cek is not None:
            mahsul_cek.Akibeti = "Tamamlandi"
            mahsul_cek.save()
            return HttpResponse(mahsul_cek.Mahsul_Link)
        else:
            return HttpResponse("Mahsul bulunamadı", status=404)
    else:
        return HttpResponse("Geçersiz istek", status=400)



@csrf_exempt
def ilerizekacek(request):
    if request.method == 'POST':
        mahsul_cek = Kontrol.objects.filter(Akibeti="Hazirla").order_by('olusturma_tarihi').first()
        if mahsul_cek is not None:
            mahsul_cek.Akibeti = "Yolda"
            mahsul_cek.save()
            Sonucu = f"{mahsul_cek.pk}|{mahsul_cek.title}|{mahsul_cek.h1}|{mahsul_cek.Post_Turu}|{mahsul_cek.meta_description}|{mahsul_cek.keywords}|{mahsul_cek.icerik}|{mahsul_cek.Kaynak_Linki}"
            return HttpResponse(Sonucu)
        else:
            return HttpResponse("Mahsul bulunamadı", status=404)
    else:
        return HttpResponse("Geçersiz istek", status=400)