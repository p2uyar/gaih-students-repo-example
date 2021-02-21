class yemek:
    def __init__(self, isim):
        self.isim = isim
        self.malzemeler = []
        self.genelmalzemeler = ["yağ", "tuz", "su"]

    def MalzemeEkle(self, malzeme):
        self.malzemeler.append(malzeme)
        print(malzeme, "eklendi.")

    def kesme(self, malzeme):
        for m in malzeme:
            print(m, "doğranıyor.")

    def pisirme(self, sure):
        print(self.isim, sure, "pişiriliyor...")

    def kavurma(self):
        print(self.malzemeler, "kavruluyor...")

    def Tabakla(self):
        print(self.isim, "hazır. Afiyet Olsun!")

class MercimekCorbasi(yemek):
    def __init__(self, isim):
        super().__init__(isim)
        self.sebzeler = ["soğan", "havuç", "patates"]
        self.bakliyat = "mercimek"

    def Hazırla(self):
        self.kesme(self.sebzeler)
        self.MalzemeEkle(self.sebzeler[0])
        self.MalzemeEkle(self.genelmalzemeler[0])
        self.kavurma()
        self.MalzemeEkle(self.sebzeler[1:])
        self.MalzemeEkle(self.genelmalzemeler[1:])
        self.pisirme("40 dk")
        self.Blender()
        self.Tabakla()

    def Blender(self):
        print(self.isim, "blenderdan geçiriliyor..")

class Pilav(yemek):
    def __init__(self, isim):
        super().__init__(isim)
        self.bakliyat = "pirinç"

    def Hazırla(self):
        self.Yıkama()
        self.MalzemeEkle(self.genelmalzemeler[0])
        self.MalzemeEkle(self.bakliyat)
        self.kavurma()
        self.MalzemeEkle(self.genelmalzemeler[2])
        self.pisirme("Suyunu çekene kadar")
        self.Dinlendirme("15 dk")
        self.Tabakla()

    def Yıkama(self):
        print(self.bakliyat,"yıkanıyor")

    def Dinlendirme(self,sure):
        print(sure,"dinleniyor..")

class Kek(yemek):
    def __init__(self, isim):
        super().__init__(isim)
        self.ekmalzemeler = ["un", "kabartma tozu", "vanilin", "yumurta", "süt", "şeker"]

    def Hazırla(self):
        self.MalzemeEkle(self.ekmalzemeler[3])
        self.MalzemeEkle(self.ekmalzemeler[-1])
        self.Cirpma()
        self.MalzemeEkle(self.ekmalzemeler[4])
        self.MalzemeEkle(self.genelmalzemeler[0])
        self.Cirpma()
        self.MalzemeEkle(self.ekmalzemeler[:3])
        self.Cirpma()
        self.Yaglama()
        self.pisirme("30 dk")
        self.Tabakla()

    def Cirpma(self):
        print(self.malzemeler,"çırpılıyor..")
    def Yaglama(self):
        print("kek kalıbı yağlanıyor")


if __name__ == '__main__':
    corba = MercimekCorbasi("Mercimek Çorbası")
    corba.Hazırla()
    pilav = Pilav("Pilav")
    pilav.Hazırla()
    kek = Kek("Kek")
    kek.Hazırla()

