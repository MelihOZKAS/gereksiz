from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("teknoloji-haberleri/", views.KategoriHome, name="teknoloji"),
    path("bilim-haberleri/", views.KategoriHome, name="bilim"),
    path("otomobil-haberleri/", views.KategoriHome, name="otomobil"),
    path("oyun-haberleri/", views.KategoriHome, name="oyun"),
    #path("random/", views.create_random_post, name="random"),
    path("iletisim/", views.iletisim, name="iletisim"),
    path("hakkimizda/", views.hakkinda, name="hakkimizda"),
    path("cerez-politikasi/", views.cerez, name="cerez"),
    path("gizlilik-politikasi/", views.gizlilik, name="gizlilik-politikasi"),
    path("kullanim-sartlari/", views.kullanim, name="kullanim-sartlari"),




    path('<str:post_slug>/', views.Enderun, name='post-getir'),#Blog Git

]

