from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from TeknoBlog.custom_storages import ImageSettingStorage
# Create your models here.
status_cho = (
    ("Taslak", "Taslak"),
    ("Hazir", "Hazir"),
    ("Yayinda", "Yayinda"),
    ("oto", "oto"),
    ("manuel", "manuel"),
)
HELP_TEXTS = {
    "title": "Masal Hiyenin başlığını girin.",
    "h1": "İçeriğin H1 Seo uyumlu girilmesi Lazım.",
    "Model": "Modele göre sılanma ve konumlandırılma olacaktır.",
    "yazar": "Şiiri yazan kullanıcıyı seçin.",
    "slug": "Şiirin URL'de görünecek kısmını girin.",
    "kategorisi": "Şiirin kategorisini seçin.",
    "resim": "800 x 400",
    "icerik": "Şiirin içeriğini girin.",
    "kapak_resmi": "Anasayfa Resim",
    "status": "Şiirin durumunu seçin.",
    "aktif": "Şiirin aktif olup olmadığını belirtin.",
    "meta_title": "Sayfanın meta başlığını girin.",
    "meta_description": "Sayfanın meta açıklamasını girin.",
    "keywords": "Sayfanın anahtar kelimelerini \" Virgül '  ' \" ile ayrınız. ",
    "banner": "Ana Sayfadaki büyük resim alanında ögrünür",
    "small_banner": "Ana sayfada küçük resimlerde görünür.",
    "hakkinda": "Şiir hakkında anlatılmak istenen.",
    "Acikalama": "Kullanıcının işlem durumunu gösterir.",
    "Story Catagory": "Hikayenin kategorisi",
}
def kapak_resmi_upload_to(instance, filename):
    # Dosya adını değiştir
    yeni_ad = f"{instance.slug}"
    # Dosya uzantısını koru
    uzanti = filename.split('.')[-1]
    # Yeni dosya adını döndür
    return f"kapak_resimleri/{yeni_ad}.{uzanti}"


class PostKategori(models.Model):
    Title = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, blank=True)
    H1 = models.CharField(max_length=255,blank=True, null=True)
    description = models.TextField( blank=True, null=True, help_text=HELP_TEXTS["meta_description"])
    keywords = models.CharField(max_length=255,blank=True,null=True,help_text=HELP_TEXTS["keywords"])
    short_title = models.CharField(max_length=255, blank=True)
    Aktif = models.BooleanField(default=False)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Post Kategori"
    def __str__(self):
        return self.short_title




# Create your models here.
class Post(models.Model):
    YAZARLAR = [
        ('Melih ÖZKAŞ', 'Melih ÖZKAŞ'),
        ('Hava ÖZKAŞ', 'Hava ÖZKAŞ'),
        ('Ayşe POLAT', 'Ayşe POLAT'),
        ('Fatma ÖZTÜRK', 'Fatma ÖZTÜRK'),
        ('Ebru GÜNEŞ', 'Ebru GÜNEŞ'),
        ('Adem YALÇIN', 'Adem YALÇIN'),
    ]


    title = models.CharField(max_length=255, help_text=HELP_TEXTS["title"])
    slug = models.SlugField(max_length=255, unique=True, blank=True,help_text=HELP_TEXTS["slug"])
    h1 = models.CharField(max_length=255,blank=True, help_text=HELP_TEXTS["h1"])
    Post_Turu = models.ForeignKey(PostKategori, null=True, on_delete=models.SET_NULL)
    yazar = models.CharField(max_length=255, choices=YAZARLAR, null=True,blank=True)
    icerik = RichTextField(null=True, blank=True, help_text=HELP_TEXTS["icerik"])
    #resim = models.ImageField(upload_to='kapak_resimleri/',null=True,blank=True)
    resim = models.ImageField(upload_to=kapak_resmi_upload_to,
                                    storage=ImageSettingStorage(),
                                    help_text=HELP_TEXTS["resim"], null=True, blank=True)
    youtube = models.URLField(blank=True)
    meta_description = models.TextField(blank=True,verbose_name="Meta Açıklama",help_text=HELP_TEXTS["meta_description"])
    keywords = models.CharField(max_length=255,blank=True,verbose_name="Anahtar Kelimeler",help_text=HELP_TEXTS["keywords"])
    yayin_tarihi = models.DateTimeField(null=True, blank=True, help_text="Postanın yayınlanacağı tarih ve saat")
    status = models.CharField(max_length=10, choices=status_cho, default="Taslak", help_text=HELP_TEXTS["status"])
    aktif = models.BooleanField(default=False, help_text=HELP_TEXTS["aktif"])
    banner = models.BooleanField(default=False, help_text=HELP_TEXTS["banner"])
    editor = models.BooleanField(default=False,help_text=HELP_TEXTS["small_banner"])
    okunma_sayisi = models.PositiveBigIntegerField(default=0)
    Kaynak_Linki = models.URLField(blank=True, null=True)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = "Post"
    def __str__(self):
        return self.title




class iletisimmodel(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255,blank=True,null=True,help_text=HELP_TEXTS["keywords"])
    title = models.TextField( blank=True, null=True)
    icerik = models.TextField( blank=True, null=True, help_text=HELP_TEXTS["meta_description"])
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "iletişim Formu"
    def __str__(self):
        return self.name






class Kontrol(models.Model):
    kontrol = [
        ('Salla', 'Salla'),
        ('Tamamlandi', 'Tamamlandi'),
        ('Hazirla', 'Hazirla'),
    ]

    title = models.CharField(max_length=255, help_text=HELP_TEXTS["title"])
    slug = models.CharField(max_length=255, help_text=HELP_TEXTS["title"], null=True,blank=True)
    h1 = models.CharField(max_length=255,blank=True, help_text=HELP_TEXTS["h1"], null=True)
    Post_Turu = models.ForeignKey(PostKategori, null=True, on_delete=models.SET_NULL)
    icerik = RichTextField(null=True, blank=True, help_text=HELP_TEXTS["icerik"])
    meta_description = models.TextField(blank=True,verbose_name="Meta Açıklama",help_text=HELP_TEXTS["meta_description"])
    keywords = models.CharField(max_length=255,blank=True,verbose_name="Anahtar Kelimeler",help_text=HELP_TEXTS["keywords"])
    Akibeti = models.CharField(max_length=255, choices=kontrol, null=True, blank=True)
    Kaynak_Linki = models.URLField(blank=True, null=True)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Kontrol"
    def __str__(self):
        return self.title