from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.newHome, name="home"),
    path('tinymce/', include('tinymce.urls')),
    # path("", views.home, name="home"),

    # path("teknoloji-haberleri/", views.KategoriHome, name="teknoloji"),
    # path("bilim-haberleri/", views.KategoriHome, name="bilim"),
    # path("cep-telefonu-haberleri/", views.KategoriHome, name="telefon"),
    # path("otomobil-haberleri/", views.KategoriHome, name="otomobil"),
    # path("oyun-haberleri/", views.KategoriHome, name="oyun"),
    # path("en-iyi-diziler-ve-filmler/", views.KategoriHome, name="dizi"),

    path("teknoloji-haberleri/", views.YeniKategoriHome, name="yeniteknoloji"),
    path("bilim-haberleri/", views.YeniKategoriHome, name="yenibilim"),
    path("cep-telefonu-haberleri/", views.YeniKategoriHome, name="yenitelefon"),
    path("otomobil-haberleri/", views.YeniKategoriHome, name="yeniotomobil"),
    path("oyun-haberleri/", views.YeniKategoriHome, name="yenioyun"),
    path("en-iyi-diziler-ve-filmler/", views.YeniKategoriHome, name="yenidizi"),
    path("haber/", views.YeniKategoriHome, name="haber"),
    path("pinterest-cek/", views.pinterest_var_mi, name="pinterestcek"),
    # path("newhome/", views.newHome, name="newHome"),
    # path("random/", views.create_random_post, name="random"),
    path("iletisim/", views.iletisim, name="iletisim"),
    path("hakkimizda/", views.hakkinda, name="hakkimizda"),
    path("cerez-politikasi/", views.cerez, name="cerez"),
    path("gizlilik-politikasi/", views.gizlilik, name="gizlilik-politikasi"),
    path("kullanim-sartlari/", views.kullanim, name="kullanim-sartlari"),
    path('story-preview/<slug:slug>/', views.StoryPreviewView.as_view(), name='story_preview'),
    path("add-post/", views.post_add),
    path("real-add-post/", views.real_post_add),  # Burası nerede hatırlayamadım

    path("mahsul-yakala/", views.mahsulyakala),
    path("mahsul-listesi-cek/", views.mahsullistesicek),
    path("mahsul-cek/", views.mahsulcek),
    path("ilerizeka-cek/", views.ilerizekacek),
    path("karepost-cek/", views.karepostcek),
    path("gonder-wp-tg/", views.send_Telegrampost),
    path("oto-paylas/", views.Oto_Paylas),
    path("index-ver/", views.indexing_var_mi, name="indexver"),
    path("facebook-cek/", views.facebook_var_mi, name="facebookcek"),
    path("linkedin-cek/", views.linkedin_var_mi, name="linkedincek"),
    path("twitter-cek/", views.twitter_var_mi, name="twittercek"),
    path("Ads.txt/", views.ads, name="ads"),
    path("ads.txt/", views.ads, name="ads"),
    path("ads.txt", views.ads, name="ads"),
    path("sill.txt/", views.delete_duplicates),

    path("farkli-haber/", views.fadilEnderun),
    path('amp/<str:post_slug>/', views.EnderunAMP, name='post-getir-amp'),  # Blog Git
    path('<str:post_slug>/', views.YeniEnderun, name='post-getir'),  # Blog Git
    # path('<str:post_slug>/', views.Enderun, name='eski-post-getir'),#Blog Git

]
