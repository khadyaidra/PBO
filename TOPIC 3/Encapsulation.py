class Person:
    def __init__(self, nama, usia, alamat):
        self.__nama = nama       # private property
        self.__usia = usia       # private property
        self.alamat = alamat     # public property

    # Getter untuk nama
    def get_nama(self):
        return self.__nama

    # Setter untuk nama
    def set_nama(self, nama_baru):
        self.__nama = nama_baru

    # Getter untuk usia
    def get_usia(self):
        return self.__usia

    # Setter untuk usia
    def set_usia(self, usia_baru):
        self.__usia = usia_baru

    def perkenalan(self):
        print(f"Halo, nama saya {self.__nama}. Saya berusia {self.__usia} tahun dan tinggal di {self.alamat}.")

    def ulang_tahun(self):
        self.__usia += 1
        print(f"Halo, nama saya {self.__nama}. Saya berusia {self.__usia} tahun setelah ulang tahun.")

miya = Person("Miya", 19, "Kartasura")
amel = Person("Amel", 20, "Kadipiro")
mila = Person("Mila", 19, "Pekalongan")

miya.perkenalan()
amel.perkenalan()
mila.ulang_tahun()

# Membuat objek baru
rara = Person("Rara", 18, "Surakarta")

# Akses awal menggunakan getter
print("\nSebelum diubah:")
print("Nama:", rara.get_nama())
print("Usia:", rara.get_usia())
rara.perkenalan()

# Mengubah nilai property private menggunakan setter
rara.set_nama("Anindita Azzahra Setiahati")
rara.set_usia(19)

print("\nSetelah diubah menggunakan setter:")
print("Nama:", rara.get_nama())
print("Usia:", rara.get_usia())
rara.perkenalan()