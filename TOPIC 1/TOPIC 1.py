class Person:
    def __init__(self, nama, usia, alamat):
        self.nama = nama
        self.usia = usia
        self.alamat = alamat

    def perkenalan(self):
        print(f"Halo, nama saya {self.nama}. Saya berusia {self.usia} tahun dan tinggal di {self.alamat}.")

    def ulang_tahun(self):
        self.usia += 1
        print(f"Halo, nama saya {self.nama}. Saya berusia {self.usia} tahun setelah ulang tahun.")

miya = Person("Miya", 19, "Kartasura")
amel = Person("Amel", 20, "Kadipiro")
mila = Person("Mila", 19, "Pekalongan")

miya.perkenalan()
amel.perkenalan()
mila.ulang_tahun()
