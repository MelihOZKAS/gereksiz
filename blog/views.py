from django.shortcuts import render, HttpResponse, get_object_or_404, reverse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET
from django.views import View
from django.http import JsonResponse
import json
import requests
from django.utils.html import strip_tags
from html import unescape
import random
from django.utils import timezone
from django.db.models import Q, Count
import environ
import re
from django.db import IntegrityError

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()


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
    description = "En son teknoloji haberlerini, ürün incelemelerini, teknoloji trendlerini ve daha fazlasını sunar. Teknoloji dünyasındaki en son gelişmeleri kaçırmayın"
    keywords = "teknoloji, haberler, incelemeler, gadgetlar, bilim, inovasyon, AI, VR, AR, mobil teknoloji, bilgisayarlar, yazılım, donanım, otomobil, oyuni bilim"
    yazar = "Yüksek Teknoloji"

    Banner = Post.objects.filter(aktif=True, status="Yayinda", banner=True).order_by(
        '-olusturma_tarihi')[:8]

    TeknolojiKategori = get_object_or_404(PostKategori, short_title="Teknoloji")
    TrendTeknoji8 = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=TeknolojiKategori,
                                        editor=True).order_by(
        '-olusturma_tarihi')[:8]
    HomeTeknolojiSol = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=TeknolojiKategori).order_by(
        '-olusturma_tarihi')[:3]
    HomeTeknolojiSag = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=TeknolojiKategori).order_by(
        '-olusturma_tarihi')[3:6]

    TelefonKategori = get_object_or_404(PostKategori, short_title="Telefon")
    TrendTelefon8 = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=TelefonKategori, editor=True).order_by(
        '-olusturma_tarihi')[:8]
    HomeTelefonSol = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=TelefonKategori).order_by(
        '-olusturma_tarihi')[:3]
    HomeTelefonSag = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=TelefonKategori).order_by(
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

        'TrendTelefon8': TrendTelefon8,
        'HomeTelefonSol': HomeTelefonSol,
        'HomeTelefonSag': HomeTelefonSag,

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


def newHome(request):
    title = "En Son Teknoloji, Bilim, Oyun ve Otomobil Haberleri"
    description = "En son teknoloji haberlerini, ürün incelemelerini, teknoloji trendlerini ve daha fazlasını sunar. Teknoloji dünyasındaki en son gelişmeleri kaçırmayın"
    keywords = "teknoloji, haberler, incelemeler, gadgetlar, bilim, inovasyon, AI, VR, AR, mobil teknoloji, bilgisayarlar, yazılım, donanım, otomobil, oyuni bilim"
    yazar = "Yüksek Teknoloji"

    Banner = Post.objects.filter(aktif=True, status="Yayinda").order_by(
        '-olusturma_tarihi')[:4]
    Trend = Post.objects.filter(aktif=True, status="Yayinda", editor=True).order_by(
        '-olusturma_tarihi')[:4]
    sideHaber = Post.objects.filter(aktif=True, status="Yayinda", banner=True).order_by(
        '-olusturma_tarihi')[:8]

    enson410 = Post.objects.filter(aktif=True, status="Yayinda").order_by(
        '-olusturma_tarihi')[4:10]

    enson1013 = Post.objects.filter(aktif=True, status="Yayinda").order_by(
        '-olusturma_tarihi')[10:13]
    enson1316 = Post.objects.filter(aktif=True, status="Yayinda").order_by(
        '-olusturma_tarihi')[13:16]

    context = {
        'title': title,
        'description': description,
        'keywords': keywords,
        'yazar': yazar,
        'Banner': Banner,
        'Trend': Trend,
        'enson410': enson410,
        'enson1013': enson1013,
        'enson1316': enson1316,
        'sideHaber': sideHaber,
    }
    return render(request, 'YeniTema/newhome.html', context)


def KategoriHome(request):
    if request.resolver_match.url_name == 'teknoloji':
        # Teknoloji haberleri için kod
        Post_Kategorisi = get_object_or_404(PostKategori, short_title="Teknoloji")
        TumPost = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=Post_Kategorisi).order_by(
            '-olusturma_tarihi')[:80]

    elif request.resolver_match.url_name == 'bilim':
        # Bilim haberleri için kod
        Post_Kategorisi = get_object_or_404(PostKategori, short_title="Bilim")
        TumPost = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=Post_Kategorisi).order_by(
            '-olusturma_tarihi')[:80]

    elif request.resolver_match.url_name == 'otomobil':
        # Otomobil haberleri için kod
        Post_Kategorisi = get_object_or_404(PostKategori, short_title="Otomobil")
        TumPost = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=Post_Kategorisi).order_by(
            '-olusturma_tarihi')[:80]

    elif request.resolver_match.url_name == 'oyun':
        # Oyun haberleri için kod
        Post_Kategorisi = get_object_or_404(PostKategori, short_title="Oyun")
        TumPost = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=Post_Kategorisi).order_by(
            '-olusturma_tarihi')[:80]
    elif request.resolver_match.url_name == 'telefon':
        # Oyun haberleri için kod
        Post_Kategorisi = get_object_or_404(PostKategori, short_title="Telefon")
        TumPost = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=Post_Kategorisi).order_by(
            '-olusturma_tarihi')[:80]
    elif request.resolver_match.url_name == 'dizi':
        # Oyun haberleri için kod
        Post_Kategorisi = get_object_or_404(PostKategori, short_title="Dizi")
        TumPost = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=Post_Kategorisi).order_by(
            '-olusturma_tarihi')[:80]
    elif request.resolver_match.url_name == 'haber':
        # Oyun haberleri için kod
        Post_Kategorisi = get_object_or_404(PostKategori, short_title="Haber")
        TumPost = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=Post_Kategorisi).order_by(
            '-olusturma_tarihi')[:80]


    populer = Post.objects.filter(aktif=True, status="Yayinda", banner=True).order_by('-olusturma_tarihi')[:8]
    editor = Post.objects.filter(aktif=True, status="Yayinda", editor=True).order_by('-olusturma_tarihi')[:8]
    enson = Post.objects.filter(aktif=True, status="Yayinda").order_by('-olusturma_tarihi')[:8]

    title = Post_Kategorisi.Title
    H1 = Post_Kategorisi.H1
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
        'H1': H1,
        'description': description,
        'keywords': keywords,
        'Post_Kategorisi': Post_Kategorisi,
        'TumPost': TumPost,
        'populer': populer,
        'editor': editor,
        'enson': enson,

    }
    return render(request, 'Hepsi/blog-list.html', context)


def YeniKategoriHome(request):
    if request.resolver_match.url_name == 'yeniteknoloji':
        # Teknoloji haberleri için kod
        Post_Kategorisi = get_object_or_404(PostKategori, short_title="Teknoloji")
        TumPost = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=Post_Kategorisi).order_by(
            '-olusturma_tarihi')[:80]

    elif request.resolver_match.url_name == 'yenibilim':
        # Bilim haberleri için kod
        Post_Kategorisi = get_object_or_404(PostKategori, short_title="Bilim")
        TumPost = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=Post_Kategorisi).order_by(
            '-olusturma_tarihi')[:80]

    elif request.resolver_match.url_name == 'yeniotomobil':
        # Otomobil haberleri için kod
        Post_Kategorisi = get_object_or_404(PostKategori, short_title="Otomobil")
        TumPost = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=Post_Kategorisi).order_by(
            '-olusturma_tarihi')[:80]

    elif request.resolver_match.url_name == 'yenioyun':
        # Oyun haberleri için kod
        Post_Kategorisi = get_object_or_404(PostKategori, short_title="Oyun")
        TumPost = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=Post_Kategorisi).order_by(
            '-olusturma_tarihi')[:80]
    elif request.resolver_match.url_name == 'yenitelefon':
        # Oyun haberleri için kod
        Post_Kategorisi = get_object_or_404(PostKategori, short_title="Telefon")
        TumPost = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=Post_Kategorisi).order_by(
            '-olusturma_tarihi')[:80]
    elif request.resolver_match.url_name == 'yenidizi':
        # Oyun haberleri için kod
        Post_Kategorisi = get_object_or_404(PostKategori, short_title="Dizi")
        TumPost = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=Post_Kategorisi).order_by(
            '-olusturma_tarihi')[:80]
    elif request.resolver_match.url_name == 'haber':
        # Oyun haberleri için kod
        Post_Kategorisi = get_object_or_404(PostKategori, short_title="Haber")
        TumPost = Post.objects.filter(aktif=True, status="Yayinda", Post_Turu=Post_Kategorisi).order_by(
            '-olusturma_tarihi')[:80]

    populer = Post.objects.filter(aktif=True, status="Yayinda", banner=True).order_by('-olusturma_tarihi')[:8]
    editor = Post.objects.filter(aktif=True, status="Yayinda", editor=True).order_by('-olusturma_tarihi')[:8]
    enson = Post.objects.filter(aktif=True, status="Yayinda").order_by('-olusturma_tarihi')[:8]

    sideHaber = Post.objects.filter(aktif=True, status="Yayinda", banner=True).order_by(
        '-olusturma_tarihi')[:8]

    title = Post_Kategorisi.Title
    H1 = Post_Kategorisi.H1
    description = Post_Kategorisi.description
    keywords = Post_Kategorisi.keywords

    paginator = Paginator(TumPost, 11)  # 11 içerik göstermek için
    page_number = request.GET.get('sayfa')
    TumPost = paginator.get_page(page_number)

    if page_number is None:
        title = f"{title}"
        description = f"{description}"
    else:
        title = f"{title} - {page_number}"
        description = f"{description} - Sayfa {page_number}"
        H1 = f"{H1} - Sayfa {page_number}"

    context = {
        'title': title,  # OK
        'H1': H1,  # OK
        'description': description,  # OK
        'keywords': keywords,  # OK
        'Post_Kategorisi': Post_Kategorisi,
        'TumPost': TumPost,  # OK
        'populer': populer,
        'editor': editor,
        'enson': enson,
        'sideHaber': sideHaber,  # OK

    }
    return render(request, 'YeniTema/yeni-list.html', context)


# YouTube video URL'sinden video ID'sini çıkaran bir regex deseni
def get_youtube_id(url):
    # YouTube video URL'sinden video ID'sini çıkaran bir regex deseni
    link = url.replace("https://www.youtube.com/embed/", "")
    youtube_id = link.split("?")
    return youtube_id[0] if youtube_id else None


def Enderun(request, post_slug):
    PostEndrun = get_object_or_404(Post, aktif=True, status="Yayinda", slug=post_slug)

    PostEndrun.okunma_sayisi += 1
    PostEndrun.save(
        update_fields=['okunma_sayisi', 'SosyalDik', 'SosyalKare', 'indexing', 'editor', 'banner', 'facebook',
                       'twitter', 'Video'])

    populer = Post.objects.filter(aktif=True, status="Yayinda", banner=True).order_by(
        '-olusturma_tarihi')[:8]
    editor = Post.objects.filter(aktif=True, status="Yayinda", editor=True).order_by(
        '-olusturma_tarihi')[:8]
    enson = Post.objects.filter(aktif=True, status="Yayinda").order_by('-olusturma_tarihi')[:8]

    title = PostEndrun.title
    H1 = PostEndrun.h1
    description = PostEndrun.meta_description
    keywords = PostEndrun.keywords
    yazar = PostEndrun.yazar
    noFollows = PostEndrun.Kaynak_NoFollow.split("|") if PostEndrun.Kaynak_NoFollow else []
    Follows = PostEndrun.Kaynak_Follow.split("|") if PostEndrun.Kaynak_Follow else []

    # twitterwidget = PostEndrun.twitterwidget

    thumbnail_url = None

    if PostEndrun.youtube:
        youtube_id = get_youtube_id(PostEndrun.youtube)
        thumbnail_url = f"https://img.youtube.com/vi/{youtube_id}/0.jpg"

    contents = [PostEndrun.icerik, PostEndrun.icerik2, PostEndrun.icerik3]
    articleBody = ' '.join(filter(None, contents))

    resimler = []
    if PostEndrun.resim:
        resimler.append(PostEndrun.resim.url)
    if PostEndrun.resim2:
        resimler.append(PostEndrun.resim2.url)
    if PostEndrun.resim3:
        resimler.append(PostEndrun.resim3.url)
    if PostEndrun.resim4:
        resimler.append(PostEndrun.resim4.url)
    if not resimler:  # Eğer resimler listesi boşsa
        resimler.append("https://teknolojibucket.s3.amazonaws.com/static/assets/logo/logo.webp")

    context = {
        'title': title,
        'H1': H1,
        'description': description,
        'keywords': keywords,
        'yazar': yazar,
        'icerik': PostEndrun,
        'populer': populer,
        'editor': editor,
        'enson': enson,
        'noFollows': noFollows,
        'Follows': Follows,
        'thumbnail_url': thumbnail_url,
        'resimler': resimler,
        'articleBody': articleBody,
    }
    return render(request, 'Hepsi/enderun.html', context)


def YeniEnderun(request, post_slug):
    PostEndrun = get_object_or_404(Post, aktif=True, status="Yayinda", slug=post_slug)

    PostEndrun.okunma_sayisi += 1
    PostEndrun.save(
        update_fields=['okunma_sayisi', 'SosyalDik', 'SosyalKare', 'indexing', 'editor', 'banner', 'facebook',
                       'twitter', 'Video'])

    populer = Post.objects.filter(aktif=True, status="Yayinda", banner=True).order_by(
        '-olusturma_tarihi')[:3]

    sideHaber = Post.objects.filter(aktif=True, status="Yayinda", banner=True).order_by(
        '-olusturma_tarihi')[:8]

    noFollows = PostEndrun.Kaynak_NoFollow.split("|") if PostEndrun.Kaynak_NoFollow else []
    Follows = PostEndrun.Kaynak_Follow.split("|") if PostEndrun.Kaynak_Follow else []

    thumbnail_url = None

    if PostEndrun.youtube:
        youtube_id = get_youtube_id(PostEndrun.youtube)
        thumbnail_url = f"https://img.youtube.com/vi/{youtube_id}/0.jpg"

    contents = [PostEndrun.icerik, PostEndrun.icerik2, PostEndrun.icerik3]
    articleBody = ' '.join(filter(None, contents))

    resimler = []
    if PostEndrun.resim:
        resimler.append(PostEndrun.resim.url)
    if PostEndrun.resim2:
        resimler.append(PostEndrun.resim2.url)
    if PostEndrun.resim3:
        resimler.append(PostEndrun.resim3.url)
    if PostEndrun.resim4:
        resimler.append(PostEndrun.resim4.url)
    if not resimler:  # Eğer resimler listesi boşsa
        resimler.append("https://teknolojibucket.s3.amazonaws.com/static/assets/logo/logo.webp")

    context = {
        'icerik': PostEndrun,
        'populer': populer,
        'sideHaber': sideHaber,
        'noFollows': noFollows,
        'Follows': Follows,
        'thumbnail_url': thumbnail_url,
        'resimler': resimler,
        'articleBody': articleBody,
    }
    return render(request, 'YeniTema/yeni-enderun.html', context)


def get_tweet_id(html_content):
    # Twitter linkini bul
    match = re.search(r'https://twitter.com/(\w+)/status/(\d+)\?ref_src', html_content)

    # Eşleşme varsa, tweet ID'sini çek
    if match:
        tweet_id = match.group(2)
        return tweet_id

    return None


def extract_youtube_id(url):
    if url:
        return url.split('/')[-1].split('?')[0]
    return None


def EnderunAMP(request, post_slug):
    PostEndrun = get_object_or_404(Post, aktif=True, status="Yayinda", slug=post_slug)

    PostEndrun.okunma_sayisi += 1
    PostEndrun.save(
        update_fields=['okunma_sayisi', 'SosyalDik', 'SosyalKare', 'indexing', 'editor', 'banner', 'facebook',
                       'twitter', 'Video'])

    enson = Post.objects.filter(aktif=True, status="Yayinda").order_by('-olusturma_tarihi')[:10]

    title = PostEndrun.title
    H1 = PostEndrun.h1
    description = PostEndrun.meta_description
    keywords = PostEndrun.keywords
    yazar = PostEndrun.yazar
    noFollows = PostEndrun.Kaynak_NoFollow.split("|") if PostEndrun.Kaynak_NoFollow else []
    Follows = PostEndrun.Kaynak_Follow.split("|") if PostEndrun.Kaynak_Follow else []

    youtubeid1 = extract_youtube_id(PostEndrun.youtube)
    youtubeid2 = extract_youtube_id(PostEndrun.youtube2)
    youtubeid3 = extract_youtube_id(PostEndrun.youtube3)
    tweet_id1 = get_tweet_id(str(PostEndrun.twitterwidget))
    tweet_id2 = get_tweet_id(str(PostEndrun.twitterwidget2))

    thumbnail_url = None

    if PostEndrun.youtube:
        youtube_id = get_youtube_id(PostEndrun.youtube)
        thumbnail_url = f"https://img.youtube.com/vi/{youtube_id}/0.jpg"

    context = {
        'title': title,
        'H1': H1,
        'description': description,
        'keywords': keywords,
        'yazar': yazar,
        'icerik': PostEndrun,
        'enson': enson,
        'noFollows': noFollows,
        'Follows': Follows,
        'thumbnail_url': thumbnail_url,
        'youtubeid1': youtubeid1,
        'youtubeid2': youtubeid2,
        'youtubeid3': youtubeid3,
        'tweet_id1': tweet_id1,
        'tweet_id2': tweet_id2,
    }
    return render(request, 'amp/AMP-enderun.amp.html', context)


@csrf_exempt
def fadilEnderun(request):
    url = "http://185.92.2.178:4444/fadil.php"
    response = requests.get(url)

    PostEndrun = Post.objects.filter(aktif=True, status="Yayinda").order_by('-olusturma_tarihi').first()

    PostEndrun.okunma_sayisi += 1
    PostEndrun.save(
        update_fields=['okunma_sayisi', 'SosyalDik', 'SosyalKare', 'indexing', 'editor', 'banner', 'facebook',
                       'twitter', 'Video'])

    populer = Post.objects.filter(aktif=True, status="Yayinda", banner=True).order_by(
        '-olusturma_tarihi')[:3]

    sideHaber = Post.objects.filter(aktif=True, status="Yayinda", banner=True).order_by(
        '-olusturma_tarihi')[:8]

    noFollows = PostEndrun.Kaynak_NoFollow.split("|") if PostEndrun.Kaynak_NoFollow else []
    Follows = PostEndrun.Kaynak_Follow.split("|") if PostEndrun.Kaynak_Follow else []

    thumbnail_url = None

    if PostEndrun.youtube:
        youtube_id = get_youtube_id(PostEndrun.youtube)
        thumbnail_url = f"https://img.youtube.com/vi/{youtube_id}/0.jpg"

    contents = [PostEndrun.icerik, PostEndrun.icerik2, PostEndrun.icerik3]
    articleBody = ' '.join(filter(None, contents))

    resimler = []
    if PostEndrun.resim:
        resimler.append(PostEndrun.resim.url)
    if PostEndrun.resim2:
        resimler.append(PostEndrun.resim2.url)
    if PostEndrun.resim3:
        resimler.append(PostEndrun.resim3.url)
    if PostEndrun.resim4:
        resimler.append(PostEndrun.resim4.url)
    if not resimler:  # Eğer resimler listesi boşsa
        resimler.append("https://teknolojibucket.s3.amazonaws.com/static/assets/logo/logo.webp")

    context = {
        'icerik': PostEndrun,
        'populer': populer,
        'sideHaber': sideHaber,
        'noFollows': noFollows,
        'Follows': Follows,
        'thumbnail_url': thumbnail_url,
        'resimler': resimler,
        'articleBody': articleBody,
    }
    return render(request, 'YeniTema/yeni-enderun.html', context)


def iletisim(request):
    title = "İletişim - YüksekTeknoloji.com Haberin Adresi | Bize Ulaşın"
    description = "Dünyadan ve Türkiyeden tüm gelişmeler teknolojik içerikler burada <3"
    keywords = "Teknoloji haberleri, Oyuncu haberleri, otomobil haberleri, oyun haberleri"
    h1 = "YüksekTeknoloji.com İletişim Bize Ulaşın"

    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': f"{env('RECAPTCHA_PRIVATE_KEY')}",
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        if result['success']:
            name = request.POST.get('name')
            email = request.POST.get('email')
            title = request.POST.get('title')
            icerik = request.POST.get('icerik')

            iletisim = iletisimmodel(name=name, email=email, title=title, icerik=icerik, )
            iletisim.save()
            return HttpResponse(
                'Başarılı ! - İletişim istediğinizi Kaydettik. <a href="{}" class="btn btn-success">Ana Sayfaya Dönmek için Tıklayın.</a>'.format(
                    reverse('home')))
        # Burada başarılı form gönderimi sonrası yapılacak işlemler yer alabilir.
        else:
            return HttpResponse(
                'Hatalı Güvenlik Doğrulaması! - Tekrar Deneyin!. <a href="{}" class="btn btn-success">Tekrar denemek için Tıklayın.</a>'.format(
                    reverse('iletisim')))

    context = {
        'title': title,
        'description': description,
        'keywords': keywords,
        'h1': h1,
    }
    return render(request, 'YeniTema/yeni-iletisim.html', context)


def hakkinda(request):
    title = "Hakkımızda YüksekTeknoloji.com | Türkiye’nin Öncü Teknoloji Platformu"
    description = "YüksekTeknoloji.com, Türkiyenin güncel teknoloji haberlerini incelemelerini ve analizlerini sunan öncü bir platformdur. Teknoloji haberlerinin yeni adresi"
    keywords = "Teknoloji haberleri, araba haberleri, otomobil haberleri, oyun haberleri"
    h1 = "YüksekTeknoloji.com Hakkında: Türkiye’nin Öncü Teknoloji Haberleri Platformu"
    context = {
        'title': title,
        'description': description,
        'keywords': keywords,
        'h1': h1,
    }
    return render(request, 'YeniTema/hakkimizda.html', context)


def cerez(request):
    title = "Çerez Politikası YüksekTeknoloji.com | Gizlilik ve Çerezler"
    description = "YüksekTeknoloji.com çerez politikası. Web sitemizdeki deneyiminizi geliştirmek için çerezleri nasıl kullandığımızı öğrenin.Yeni en son teknoloji haberleri"
    keywords = "Teknolojik haberler, araba fiyatları haberleri, otomobil haberleri, oyun haberleri"
    h1 = "YüksekTeknoloji.com Çerez Politikası Gizliliğinize Saygı Duyuyoruz"
    context = {
        'title': title,
        'description': description,
        'keywords': keywords,
        'h1': h1,
    }
    return render(request, 'YeniTema/cerez.html', context)


def gizlilik(request):
    title = "Gizlilik YüksekTeknoloji.com | Bilgilerinizin Korunması"
    description = "YüksekTeknoloji.com gizlilik politikası Kişisel bilgilerinizin nasıl korunduğunu ve kullanıldığını öğrenin. Gizliliğiniz bizim için en önemlidir."
    keywords = "Gizlilik Politikası, YüksekTeknoloji.com, Kişisel Bilgiler, Veri Koruma, Kullanıcı Gizliliği"
    h1 = "YüksekTeknoloji.com Gizlilik Politikası: Kişisel Bilgileriniz Güvende"
    context = {
        'title': title,
        'description': description,
        'keywords': keywords,
        'h1': h1,
    }
    return render(request, 'YeniTema/gizlilik.html', context)


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
    return render(request, 'YeniTema/kullanim.html', context)


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
        story = Post.objects.get(slug=kwargs['slug'])

        # Veritabanından bilgileri çek
        title = story.title
        h1 = story.h1
        keywords = story.keywords
        description = story.meta_description

        # İçeriği oluştur
        content = f"Title: {title}\n\n <br> H1: {h1}\n\n <br> Keywords: {keywords}\n\n <br> Description: {description}\n\n <br> {story.yenicerik1}"

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
        siir_masal = Kontrol(title=title, slug=slug, h1=h1, Post_Turu=Post_Turu_Gelen, icerik=icerik, keywords=key,
                             meta_description=meta_description, Akibeti="Beklemede", Kaynak_Linki=Kaynak_Linki)
        siir_masal.save()
        if siir_masal.id is None:
            return HttpResponse("Post kaydedilemedi.")
        else:
            return HttpResponse("Post başarıyla kaydedildi. ID: " + str(siir_masal.id))


@csrf_exempt
def real_post_add(request):
    if request.method == 'POST':
        # Gelen POST isteğindeki değerleri alın
        ZekaOzet = request.POST.get('ZekaOzet')
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
        siir_masal = Post(ozet=ZekaOzet, title=title, hiddenTitle=hiddenTitle, slug=slug, h1=h1, hiddenH1=hiddenH1,
                          Post_Turu=Post_Turu_Gelen, yenicerik1=icerik, info=info, hiddenKeys=hiddenKeys,
                          meta_description=meta_description, Kaynak_Linki=Kaynak_Linki)
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
                try:
                    mahsulkayit = Mahsul(Tarla_Link=Main_Link, Mahsul_Link=Post_Link, Akibeti='Beklemede')
                    mahsulkayit.save()
                except IntegrityError:
                    continue  # Bu satırı ekledim.
            return JsonResponse({"message": "Başarılı"})
        else:
            return JsonResponse({"error": "Geçersiz Content-Type başlığı"}, status=400)
    else:
        return JsonResponse({"method": request.method, "headers": dict(request.headers)})


@csrf_exempt
def mahsullistesicek(request):
    if request.method == 'POST':
        tarla_link = request.POST.get('Tarla_Link')
        mahsul_list = Mahsul.objects.filter(Tarla_Link=tarla_link).order_by('-olusturma_tarihi')[:150]
        mahsul_links = "|".join([mahsul.Mahsul_Link for mahsul in mahsul_list])
        return HttpResponse(mahsul_links)
    else:
        return HttpResponse("Geçersiz istek", status=400)


@csrf_exempt
def mahsulcek(request):
    if request.method == 'POST':
        tarla_link = request.POST.get('Tarla_Link')
        mahsul_cek = Mahsul.objects.filter(Tarla_Link=tarla_link, Akibeti="Beklemede").order_by(
            'olusturma_tarihi').first()
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
        mahsul_cek = Kontrol.objects.filter(Akibeti="Hazirla").order_by('-olusturma_tarihi').first()
        if mahsul_cek is not None:
            mahsul_cek.Akibeti = "Yolda"
            mahsul_cek.save()
            Sonucu = f"{mahsul_cek.pk}|={mahsul_cek.title}|={mahsul_cek.h1}|={mahsul_cek.Post_Turu}|={mahsul_cek.meta_description}|={mahsul_cek.keywords}|={mahsul_cek.icerik}|={mahsul_cek.Kaynak_Linki}"
            return HttpResponse(Sonucu)
        else:
            return HttpResponse("Mahsul bulunamadı")
    else:
        return HttpResponse("Geçersiz istek", status=400)


@csrf_exempt
def karepostcek(request):
    if request.method == 'POST':
        mahsul_cek = Post.objects.filter(aktif=True, status="Yayinda", SosyalKare=True).order_by(
            'olusturma_tarihi').first()
        if mahsul_cek is not None:
            # HTML etiketlerini kaldır
            mahsul_cek.SosyalKare = False
            mahsul_cek.save(
                update_fields=['okunma_sayisi', 'SosyalDik', 'SosyalKare', 'indexing', 'editor', 'banner', 'facebook',
                               'twitter', 'Video'])
            title = strip_tags(mahsul_cek.title)
            icerik = unescape(strip_tags(mahsul_cek.ozet))
            Sonucu = f"{mahsul_cek.pk}|={title}|={icerik}|={mahsul_cek.resim}"
            return HttpResponse(Sonucu)
        else:
            return HttpResponse("Oluşturulacak Kare içerik bulunamadı", status=404)
    else:
        return HttpResponse("Geçersiz istek", status=400)


def send_Telegrampost(request):
    GelenPost = Post.objects.filter(aktif=True, status="Yayinda", TelegramSend=True).order_by(
        'olusturma_tarihi').first()

    if GelenPost:
        GelenPost.TelegramSend = False
        GelenPost.save(
            update_fields=['okunma_sayisi', 'SosyalDik', 'SosyalKare', 'indexing', 'editor', 'banner', 'facebook',
                           'twitter', 'Video'])
        title = GelenPost.title  # Postun başlığını al
        slug = GelenPost.slug  # Postun slug'ını al
        # İlgi çekici bir mesaj oluştur
        message = f"🎉 Yeni bir teknoloji haberi geldi: {title}! 🎉\n\n🔗 Detayları görmek için: https://yuksekteknoloji.com/{slug}\n\n🚀 YuksekTeknoloji.com - Teknoloji dünyasının kalbi burada atıyor! 🚀"
        # Telegram API'sini kullanarak mesajı gönder
        telegram_url = f"https://api.telegram.org/bot{env('Telegram_Token')}/sendMessage?chat_id={env('tlg_chat_id')}&text={message}"
        r = requests.get(telegram_url)
        return HttpResponse(r.text)
    else:
        return HttpResponse("Post yok")


def Oto_Paylas(request):
    post = Post.objects.filter(Q(status="oto") & (Q(yayin_tarihi__lte=timezone.now()) | Q(yayin_tarihi=None))).first()

    if post is not None:
        post.status = "Yayinda"
        post.hiddenTitle = ""
        post.hiddenH1 = ""
        post.hiddenKeys = ""
        post.info = ""
        post.aktif = True
        post.indexing = True  # indekslendi olarak işaretle
        post.olusturma_tarihi = timezone.now()  # eklenme tarihini güncelle
        post.save()
        return HttpResponse(f'Şükürler Olsun "{post.title}" Paylaşıldı.')
    else:
        return HttpResponse('Paylaşılacak Post Bulunamadı.')


@csrf_exempt
def indexing_var_mi(request):
    post = Post.objects.filter(indexing=True, aktif=True, status="Yayinda").order_by('-guncelleme_tarihi').first()
    if post is not None:
        # post'un indexing durumunu False yapayı unutmamak lazımmm dimi.
        post.indexing = False
        post.save(update_fields=['okunma_sayisi', 'SosyalDik', 'SosyalKare', 'indexing', 'editor', 'banner', 'facebook',
                                 'twitter', 'Video'])
        return HttpResponse(f"https://www.yuksekteknoloji.com/{post.slug}/")
        # return HttpResponse(f"https://www.kidsstorieshub.com/kids-bedtime-story/{post.slug}/")
    else:
        return HttpResponse("post bulunamadı.")


@csrf_exempt
def facebook_var_mi(request):
    post = Post.objects.filter(facebook=True, aktif=True, status="Yayinda").order_by('-guncelleme_tarihi').first()
    if post is not None:
        # post'un indexing durumunu False yapayı unutmamak lazımmm dimi.
        post.facebook = False
        icerik = unescape(strip_tags(post.ozet))
        if not icerik:
            icerik = "Haberin devamı için tıklayın!"
        post.save(update_fields=['okunma_sayisi', 'SosyalDik', 'SosyalKare', 'indexing', 'editor', 'banner', 'facebook',
                                 'twitter', 'Video'])
        return HttpResponse(f"https://www.yuksekteknoloji.com/{post.slug}/!={icerik}")
        # return HttpResponse(f"https://www.kidsstorieshub.com/kids-bedtime-story/{post.slug}/")
    else:
        return HttpResponse("post bulunamadı.")

@csrf_exempt
def linkedin_var_mi(request):
    post = Post.objects.filter(linkedin=True, aktif=True, status="Yayinda").order_by('-guncelleme_tarihi').first()
    if post is not None:
        # post'un indexing durumunu False yapayı unutmamak lazımmm dimi.
        post.linkedin = False
        icerik = unescape(strip_tags(post.h1))
        if not icerik:
            icerik = "Haberin devamı için tıklayın!"
        post.save(update_fields=['okunma_sayisi', 'SosyalDik', 'SosyalKare', 'indexing', 'editor', 'banner', 'facebook',
                                 'twitter', 'Video','linkedin', 'pinterest'])
        return HttpResponse(f"https://www.yuksekteknoloji.com/{post.slug}/!={icerik}")
    else:
        return HttpResponse("post bulunamadı.")
@csrf_exempt
def twitter_var_mi(request):
    post = Post.objects.filter(twitter=True, aktif=True, status="Yayinda").order_by('-guncelleme_tarihi').first()
    if post is not None:
        # post'un indexing durumunu False yapayı unutmamak lazımmm dimi.
        post.twitter = False
        icerik = post.h1
        kategorisi = post.Post_Turu
        hashtag = "#" + kategorisi.short_title if kategorisi.short_title else ""
        if not icerik:
            icerik = "Haberin devamı için tıklayın!"
        post.save(update_fields=['okunma_sayisi', 'SosyalDik', 'SosyalKare', 'indexing', 'editor', 'banner', 'facebook',
                                 'twitter', 'Video'])
        return HttpResponse(
            f"https://www.yuksekteknoloji.com/{post.slug}/!={icerik} {hashtag} Haberin devamı için lütfen tıklayın!")
    else:
        return HttpResponse("Paylaşılacak Twitter içerik bulunamadı")


@require_GET
def ads(request):
    return HttpResponse(ads_content, content_type="text/plain")


ads_content = """google.com, pub-7065951693101615, DIRECT, f08c47fec0942fa0"""


def delete_duplicates(request):
    # Mahsul_Link alanına göre grupla ve birden fazla olanları al
    duplicate_rows = Mahsul.objects.values('Mahsul_Link').annotate(link_count=Count('Mahsul_Link')).filter(
        link_count__gt=1)

    deleted_links = []  # Silinen linkleri saklamak için bir liste oluştur

    for row in duplicate_rows:
        # Her grup için, ilk örneği hariç tüm örnekleri sil
        duplicates = Mahsul.objects.filter(Mahsul_Link=row['Mahsul_Link']).exclude(
            id=Mahsul.objects.filter(Mahsul_Link=row['Mahsul_Link']).first().id)
        deleted_links.extend([obj.Mahsul_Link for obj in duplicates])  # Silinen linkleri listeye ekle
        duplicates.delete()

    # Silinen linkleri HttpResponse ile döndür
    response = "\n".join(deleted_links)
    return HttpResponse(response, content_type='text/plain')


@csrf_exempt
def pinterest_var_mi(request):
    post = Post.objects.filter(pinterest=True, aktif=True, status="Yayinda").first()
    if post is not None:
        # post'un facebook durumunu False yapayı unutmamak lazımmm dimi.
        post.pinterest = False
        icerik = post.title
        if not icerik:
            icerik = "Teknoloji Haberleri"
        post.save(update_fields=['okunma_sayisi', 'banner', 'editor', 'indexing', 'facebook', 'twitter',
                                 'pinterest'])
        return HttpResponse(
            f"https://www.yuksekteknoloji.com/{post.slug}/!={post.h1}. Daha fazla bebek ismi için bizi takip edin!={post.title}!={post.Post_Turu.short_title}!={post.resim.url}")
    else:
        return HttpResponse("post bulunamadı.")
