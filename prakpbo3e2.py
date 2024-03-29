class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar


# Membuat objek dari class PersegiPanjang
persegi_panjang = PersegiPanjang(20, 12)

# Menampilkan informasi
print("Rafael Gala Herlambang 064002300036 Teknik Industri\n-----PROGRAM MENGHITUNG LUAS PERSEGI PANJANG-----\nPersegi panjang dengan panjang {0}cm dan lebar {1}cm memiliki luas sebesar {2}cm^2".format(persegi_panjang.panjang, persegi_panjang.lebar, persegi_panjang.hitung_luas()))
