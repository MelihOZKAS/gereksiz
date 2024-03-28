from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("teknoloji-haberleri/", views.KategoriHome, name="teknoloji"),
    path("bilim-haberleri/", views.KategoriHome, name="bilim"),
    path("cep-telefonu-haberleri/", views.KategoriHome, name="telefon"),
    path("otomobil-haberleri/", views.KategoriHome, name="otomobil"),
    path("oyun-haberleri/", views.KategoriHome, name="oyun"),
    #path("random/", views.create_random_post, name="random"),
    path("iletisim/", views.iletisim, name="iletisim"),
    path("hakkimizda/", views.hakkinda, name="hakkimizda"),
    path("cerez-politikasi/", views.cerez, name="cerez"),
    path("gizlilik-politikasi/", views.gizlilik, name="gizlilik-politikasi"),
    path("kullanim-sartlari/", views.kullanim, name="kullanim-sartlari"),
    path('story-preview/<slug:slug>/', views.StoryPreviewView.as_view(), name='story_preview'),

    path("add-post/", views.post_add),
    path("real-add-post/", views.real_post_add), #Burası nerede hatırlayamadım

    path("mahsul-yakala/", views.mahsulyakala),
    path("mahsul-listesi-cek/", views.mahsullistesicek),
    path("mahsul-cek/", views.mahsulcek),
    path("ilerizeka-cek/", views.ilerizekacek),
    path("karepost-cek/", views.karepostcek),
    path("gonder-wp-tg/", views.send_Telegrampost),
    path("oto-paylas/", views.Oto_Paylas),
    path("index-ver/", views.indexing_var_mi, name="indexver"),
    path("Ads.txt/", views.ads, name="ads"),
    path("ads.txt/", views.ads, name="ads"),
    path("sill.txt/", views.delete_duplicates),




    path("farkli-haber/", views.fadilEnderun),
    path('<str:post_slug>/', views.Enderun, name='post-getir'),#Blog Git

]

