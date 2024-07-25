from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from TeknoBlog.custom_storages import ImageSettingStorage
from tinymce.models import HTMLField

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
    "Wp-TG": "Whatsapp ve Telegramda paylaş",
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
    H1 = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True, help_text=HELP_TEXTS["meta_description"])
    keywords = models.CharField(max_length=255, blank=True, null=True, help_text=HELP_TEXTS["keywords"])
    short_title = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    renk = models.CharField(max_length=255, blank=True)
    resim = models.ImageField(upload_to=kapak_resmi_upload_to,
                              storage=ImageSettingStorage(),
                              help_text=HELP_TEXTS["resim"], null=True, blank=True)
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

    Jsonu = [
        ('Article', 'Article'),
        ('NewsArticle', 'NewsArticle'),
        ('BlogPosting', 'BlogPosting'),
    ]

    OkumaSuresi = [
        ('2 Dakika Dakika Okuma Süresi', '2 Dakika Dakika Okuma Süresi'),
        ('3 Dakika Dakika Okuma Süresi', '3 Dakika Dakika Okuma Süresi'),
        ('4 Dakika Dakika Okuma Süresi', '4 Dakika Dakika Okuma Süresi'),
        ('5 Dakika Dakika Okuma Süresi', '5 Dakika Dakika Okuma Süresi'),
        ('6 Dakika Dakika Okuma Süresi', '6 Dakika Dakika Okuma Süresi'),
    ]

    title = models.CharField(max_length=255, help_text=HELP_TEXTS["title"])
    hiddenTitle = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, help_text=HELP_TEXTS["slug"])
    h1 = models.CharField(max_length=255, blank=True, help_text=HELP_TEXTS["h1"])
    hiddenH1 = models.TextField(blank=True, null=True)
    Post_Turu = models.ForeignKey(PostKategori, null=True, on_delete=models.SET_NULL)
    Post_type = models.CharField(max_length=255, choices=Jsonu, null=True, default="NewsArticle")
    sure = models.CharField(max_length=255, choices=OkumaSuresi, null=True, default="2 Dakika Dakika Okuma Süresi")
    yazar = models.CharField(max_length=255, choices=YAZARLAR, null=True, blank=True)

    yenicerik1 = HTMLField(null=True, blank=True, help_text="ismin uzun anlamı kökeni vs...")
    yenicerik2 = HTMLField(null=True, blank=True, help_text="ismin kişilik özellikleri")
    yenicerik3 = HTMLField(null=True, blank=True, help_text="isminde ki ünlü isimler!")
    yenicerik4 = HTMLField(null=True, blank=True)
    yenicerik5 = HTMLField(null=True, blank=True)
    yenicerik6 = HTMLField(null=True, blank=True)

    icerik = RichTextField(null=True, blank=True, help_text=HELP_TEXTS["icerik"])
    icerik2 = RichTextField(null=True, blank=True, help_text=HELP_TEXTS["icerik"])
    icerik3 = RichTextField(null=True, blank=True, help_text=HELP_TEXTS["icerik"])
    #icerik4 = RichTextField(null=True, blank=True, help_text=HELP_TEXTS["icerik"])
    #icerik5 = RichTextField(null=True, blank=True, help_text=HELP_TEXTS["icerik"])
    #icerik6 = RichTextField(null=True, blank=True, help_text=HELP_TEXTS["icerik"])
    ozet = models.TextField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    resim = models.ImageField(upload_to=kapak_resmi_upload_to,
                              storage=ImageSettingStorage(),
                              help_text=HELP_TEXTS["resim"], null=True, blank=True)
    resim2 = models.ImageField(upload_to=kapak_resmi_upload_to,
                               storage=ImageSettingStorage(),
                               help_text=HELP_TEXTS["resim"], null=True, blank=True)
    resim3 = models.ImageField(upload_to=kapak_resmi_upload_to,
                               storage=ImageSettingStorage(),
                               help_text=HELP_TEXTS["resim"], null=True, blank=True)
    resim4 = models.ImageField(upload_to=kapak_resmi_upload_to,
                               storage=ImageSettingStorage(),
                               help_text=HELP_TEXTS["resim"], null=True, blank=True)
    resim5 = models.ImageField(upload_to=kapak_resmi_upload_to,
                               storage=ImageSettingStorage(),
                               help_text=HELP_TEXTS["resim"], null=True, blank=True)
    resim6 = models.ImageField(upload_to=kapak_resmi_upload_to,
                               storage=ImageSettingStorage(),
                               help_text=HELP_TEXTS["resim"], null=True, blank=True)
    youtube = models.URLField(blank=True)
    youtube2 = models.URLField(blank=True)
    youtube3 = models.URLField(blank=True)
    twitterwidget = models.TextField(blank=True, null=True)
    twitterwidget2 = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, verbose_name="Meta Açıklama",
                                        help_text=HELP_TEXTS["meta_description"])
    keywords = models.CharField(max_length=255, blank=True, verbose_name="Anahtar Kelimeler",
                                help_text=HELP_TEXTS["keywords"])
    hiddenKeys = models.TextField(blank=True, null=True)
    yayin_tarihi = models.DateTimeField(null=True, blank=True, help_text="Postanın yayınlanacağı tarih ve saat")
    status = models.CharField(max_length=10, choices=status_cho, default="Taslak", help_text=HELP_TEXTS["status"])
    Star = models.BooleanField(default=False, help_text="Favori Konuları İşaretliyoruz.")
    TelegramSend = models.BooleanField(default=False, help_text="Telegramdan Link Gönderir.")
    Whatsapp = models.BooleanField(default=False, help_text="Whatsapp Link Gönderir.")
    Video = models.BooleanField(default=False, help_text="1920 x 1080 Video Yapar")
    SosyalDik = models.BooleanField(default=True, help_text="1920 x 1080 Resim üret")
    SosyalKare = models.BooleanField(default=True, help_text="Havanın Wp Attığı Post Turu")
    aktif = models.BooleanField(default=False, help_text=HELP_TEXTS["aktif"])
    indexing = models.BooleanField(default=True, help_text="Indexlensin mi?")
    banner = models.BooleanField(default=False, help_text=HELP_TEXTS["banner"])
    editor = models.BooleanField(default=False, help_text=HELP_TEXTS["small_banner"])
    facebook = models.BooleanField(default=True, help_text="Facebook da Paylaşılsın mı ?")
    twitter = models.BooleanField(default=True, help_text="twitter da Paylaşılsın mı ?")
    pinterest = models.BooleanField(default=True, help_text="twitter da Paylaşılsın mı ?")
    okunma_sayisi = models.PositiveBigIntegerField(default=0)
    Kaynak_Linki = models.URLField(blank=True, null=True)
    Kaynak_Follow = models.TextField(blank=True, null=True)
    Kaynak_NoFollow = models.TextField(blank=True, null=True)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Post"

    def __str__(self):
        return self.title


class iletisimmodel(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True, help_text=HELP_TEXTS["keywords"])
    title = models.TextField(blank=True, null=True)
    icerik = models.TextField(blank=True, null=True, help_text=HELP_TEXTS["meta_description"])
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "iletişim Formu"

    def __str__(self):
        return self.name


class Kontrol(models.Model):
    kontrol = [
        ('Salla', 'Salla'),
        ('Beklemede', 'Beklemede'),
        ('Tamamlandi', 'Tamamlandi'),
        ('Hazirla', 'Hazirla'),
        ('Yolda', 'Yolda'),
    ]

    title = models.CharField(max_length=255, help_text=HELP_TEXTS["title"])
    slug = models.CharField(max_length=255, help_text=HELP_TEXTS["title"], null=True, blank=True)
    h1 = models.CharField(max_length=255, blank=True, help_text=HELP_TEXTS["h1"], null=True)
    Post_Turu = models.ForeignKey(PostKategori, null=True, on_delete=models.SET_NULL)
    icerik = RichTextField(null=True, blank=True, help_text=HELP_TEXTS["icerik"])
    meta_description = models.TextField(blank=True, verbose_name="Meta Açıklama",
                                        help_text=HELP_TEXTS["meta_description"])
    keywords = models.CharField(max_length=255, blank=True, verbose_name="Anahtar Kelimeler",
                                help_text=HELP_TEXTS["keywords"])
    Akibeti = models.CharField(max_length=255, choices=kontrol, null=True, blank=True)
    Kaynak_Linki = models.URLField(blank=True, null=True)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Kontrol"

    def __str__(self):
        return self.title

    def kelime_sayisi(self):
        return len(self.icerik.split())


class Mahsul(models.Model):
    kontrol = [
        ('Tamamlandi', 'Tamamlandi'),
        ('Beklemede', 'Beklemede'),
    ]
    Tarla_Link = models.URLField(blank=True, null=True)
    Mahsul_Link = models.URLField(blank=True, null=True, unique=True)
    Akibeti = models.CharField(max_length=255, choices=kontrol, null=True, blank=True)
    Aciklama = models.CharField(max_length=255, blank=True, null=True)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Mahsuller"
