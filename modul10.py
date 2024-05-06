from abc import ABC, abstractmethod
print('==============================')
print('Nama: rafael gala herlambang')
print('Nim: 0064002300036')
print('==============================')
class BangunDatar(ABC):
    @abstractmethod
    def hitung_luas(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi * self.sisi

class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi

class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def hitung_luas(self):
        return 3.14 * self.jari_jari * self.jari_jari

class JajarGenjang(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return self.alas * self.tinggi

def main():
    persegi = Persegi(9)
    persegi_panjang = PersegiPanjang(8, 6)
    segitiga = Segitiga(6, 4)
    lingkaran = Lingkaran(7)
    jajar_genjang = JajarGenjang(2, 7)

    bangun_datar_list = [persegi, persegi_panjang, segitiga, lingkaran, jajar_genjang]

    for bangun_datar in bangun_datar_list:
        nama_bangun = bangun_datar.__class__.__name__
        luas = bangun_datar.hitung_luas()
        print(f"Luas {nama_bangun}: {luas}")

if __name__ == "__main__":
    main()