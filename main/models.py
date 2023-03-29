from django.db import models

# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.name


class Plants(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/plants/')

    def __str__(self):
        return self.name


class Plant(models.Model):
    parent = models.ForeignKey(Plants, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='images/plants/type/')
    name = models.CharField(max_length=200, null=True, blank=True)
    origin = models.CharField(max_length=200, null=True, blank=True)
    tozlayici = models.CharField(max_length=200, null=True, blank=True)
    mehsul_zamani = models.CharField(max_length=200, null=True, blank=True)
    meyve_agirligi = models.CharField(max_length=200, null=True, blank=True)
    lepe_agirligi = models.CharField(
        max_length=200, null=True, blank=True, default=None)
    qabigli_meyve_boyu = models.FloatField(null=True, blank=True)
    ic_meyve_boyu = models.FloatField(null=True, blank=True, default=None)
    qabigli_meyve_agirligi = models.FloatField(
        null=True, blank=True, default=None)
    rengi = models.CharField(max_length=200, null=True, blank=True)
    meyve_ic_rengi = models.CharField(max_length=200, null=True, blank=True)
    formasi = models.CharField(max_length=200, null=True, blank=True)
    kalibr = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Texnika(models.Model):
    ad = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to='images/techniques/', verbose_name="Şəkil")

    def __str__(self):
        return self.ad


class Model(models.Model):
    texnika = models.ForeignKey(
        Texnika, on_delete=models.CASCADE, verbose_name='Texnika')
    model = models.CharField(max_length=100, null=True,
                             blank=True, verbose_name='Model')
    marka = models.CharField(max_length=100, null=True,
                             blank=True, verbose_name='Marka')
    urun_kodu = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Ürün kodu')
    tank = models.IntegerField(null=True, blank=True, verbose_name='Tank')
    pompa = models.IntegerField(null=True, blank=True, verbose_name='Pompa')
    traktor_gucu = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Traktor Gücü')
    tezyiq = models.IntegerField(null=True, blank=True, verbose_name='Təzyiq')
    hava = models.IntegerField(null=True, blank=True, verbose_name='Hava')
    agirliq = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Ağırlıq')
    is_hecmi = models.IntegerField(
        null=True, blank=True, verbose_name='İş həcmi')
    enerji_menbeyi = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Enerji mənbəyi')
    qaranti = models.IntegerField(
        null=True, blank=True, verbose_name='Qarantiya')
    saatliq_mehsul = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Saatlıq məhsul')
    ayirma = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Ayırma')
    enerji_ehtiyaci = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Enerji ehtiyacı')
    guc = models.CharField(max_length=100, null=True,
                           blank=True, verbose_name='Güc')
    hecm = models.CharField(max_length=100, null=True,
                            blank=True, verbose_name='Həcm')
    motor_gucu = models.FloatField(
        null=True, blank=True, verbose_name='Motor gücü')
    guc_telebati = models.IntegerField(
        null=True, blank=True, verbose_name='Güc tələbatı')
    bicaq_sayi = models.IntegerField(
        null=True, blank=True, verbose_name='Bıçaq sayı')
    kazan_hacmi = models.IntegerField(
        null=True, blank=True, verbose_name='Kazan həcmi')
    calisma_yuksekligi = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Çalışma yüksəkliyi')
    calisma_uzunlugu = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Çalışma uzunluğu')
    calisma_yonu = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Çalışma yönü')
    ceviz_qurutma_qabilliyyeti = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Ceviz qurutma qabiliyyəti')
    guc_gereksinimi = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Güc gereksinimi')
    hidrolik_gereksinimi = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Hidrolik gereksinimi')
    traktor_orta_noktasindan_max_kol_uzunlugu = models.IntegerField(
        null=True, blank=True, verbose_name='Traktor orta nöqtəsindən max qol uzunluğu')
    calisma_derinligi = models.IntegerField(
        null=True, blank=True, verbose_name='Çalışma dərinliyi')
    capalama_genisligi = models.IntegerField(
        null=True, blank=True, verbose_name='Çapalama genişliyi')
    agac_sira_arasi = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Ağac sıra arası')
    umumi_genislik = models.FloatField(
        null=True, blank=True, verbose_name='Ümumi genişlik')
    isleme_genisliyi = models.FloatField(
        null=True, blank=True, verbose_name='İşləmə genişliyi')
    ilerleme_sureti = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='İlərləmə sürəti')
    ozellik_1 = models.CharField(
        max_length=200, blank=True, null=True, verbose_name='Özəllik 1', default=None)
    ozellik_2 = models.CharField(
        max_length=200, blank=True, null=True, verbose_name='Özəllik 2', default=None)
    ozellik_3 = models.CharField(
        max_length=200, blank=True, null=True, verbose_name='Özəllik 3', default=None)
    ozellik_4 = models.CharField(
        max_length=200, blank=True, null=True, verbose_name='Özəllik 4', default=None)

    def __str__(self):
        if self.model:
            return self.model
        elif self.marka:
            return self.marka
        elif self.urun_kodu:
            return self.urun_kodu
        else:
            return self.texnika.ad


class Tool(models.Model):
    name = models.CharField(max_length=100, verbose_name='Ad')
    image = models.ImageField(upload_to='images/tools/')

    def __str__(self):
        return self.name


class Gübre(models.Model):
    name = models.CharField(max_length=200, verbose_name='Ad')
    image = models.ImageField(
        upload_to='images/fertilizers/', verbose_name='Şəkil', default=None, null=True, blank=True)
    content = models.TextField(
        verbose_name='Məlumat', null=True, blank=True, default=None)
    element_1 = models.CharField(
        max_length=200, verbose_name='Element 1', null=True, blank=True)
    faiz_1 = models.FloatField(verbose_name="Faiz 1", null=True, blank=True)
    element_2 = models.CharField(
        max_length=200, verbose_name='Element 2', null=True, blank=True)
    faiz_2 = models.FloatField(verbose_name="Faiz 2", null=True, blank=True)
    element_3 = models.CharField(
        max_length=200, verbose_name='Element 3', null=True, blank=True)
    faiz_3 = models.FloatField(verbose_name="Faiz 3", null=True, blank=True)
    element_4 = models.CharField(
        max_length=200, verbose_name='Element 4', null=True, blank=True)
    faiz_4 = models.FloatField(verbose_name="Faiz 4", null=True, blank=True)
    element_5 = models.CharField(
        max_length=200, verbose_name='Element 5', null=True, blank=True)
    faiz_5 = models.FloatField(verbose_name="Faiz 5", null=True, blank=True)
    element_6 = models.CharField(
        max_length=200, verbose_name='Element 6', null=True, blank=True)
    faiz_6 = models.FloatField(verbose_name="Faiz 6", null=True, blank=True)
    element_7 = models.CharField(
        max_length=200, verbose_name='Element 7', null=True, blank=True)
    faiz_7 = models.FloatField(verbose_name="Faiz 7", null=True, blank=True)
    element_8 = models.CharField(
        max_length=200, verbose_name='Element 8', null=True, blank=True)
    faiz_8 = models.FloatField(verbose_name="Faiz 8", null=True, blank=True)
    element_9 = models.CharField(
        max_length=200, verbose_name='Element 9', null=True, blank=True)
    faiz_9 = models.FloatField(verbose_name="Faiz 9", null=True, blank=True)
    element_10 = models.CharField(
        max_length=200, verbose_name='Element 10', null=True, blank=True)
    faiz_10 = models.FloatField(verbose_name="Faiz 10", null=True, blank=True)
    element_11 = models.CharField(
        max_length=200, verbose_name='Element 11', null=True, blank=True)
    faiz_11 = models.FloatField(verbose_name="Faiz 11", null=True, blank=True)
    element_12 = models.CharField(
        max_length=200, verbose_name='Element 12', null=True, blank=True)
    faiz_12 = models.FloatField(verbose_name="Faiz 12", null=True, blank=True)
    element_13 = models.CharField(
        max_length=200, verbose_name='Element 13', null=True, blank=True)
    faiz_13 = models.FloatField(verbose_name="Faiz 13", null=True, blank=True)
    element_14 = models.CharField(
        max_length=200, verbose_name='Element 14', null=True, blank=True)
    faiz_14 = models.FloatField(verbose_name="Faiz 14", null=True, blank=True)
    element_15 = models.CharField(
        max_length=200, verbose_name='Element 15', null=True, blank=True)
    faiz_15 = models.FloatField(verbose_name="Faiz 15", null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Watering(models.Model):
    image = models.ImageField(upload_to='images/watering')
    name = models.CharField(max_length=200, null=True,
                            blank=True, verbose_name='Ad')
    content = models.TextField(
        verbose_name="Məlumat", default=None, null=True, blank=True)

    def __str__(self):
        return self.name


class Watering_tool(models.Model):
    tool = models.ForeignKey(Watering, on_delete=models.CASCADE)
    mehsul_kodu = models.CharField(
        max_length=200, null=True, blank=True, verbose_name='Məhsul kodu')
    giris_cixis = models.CharField(
        max_length=200, null=True, blank=True, verbose_name='Giriş-çıxış')
    hecm = models.CharField(max_length=200, null=True,
                            blank=True, verbose_name='Həcm')
    yosun_filteri = models.CharField(
        max_length=200, null=True, blank=True, verbose_name='Yosun Filteri')
    plastik_filter = models.CharField(
        max_length=200, null=True, blank=True, verbose_name='Plastik Filter')
    avtomatik_filter = models.CharField(
        max_length=200, null=True, blank=True, verbose_name='Avtomatik Filter')
    qum_tanki = models.IntegerField(null=True, blank=True)
    suzme_sethi = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.tool.name
