class AnggotaOrganisasi:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan
        self.bawahan = []

    def tambah_bawahan(self, anggota):
        self.bawahan.append(anggota)


class OrganisasiMahasiswa:
    def __init__(self):
        self.anggota = {}

    def tambah_anggota(self, nama, jabatan):
        self.anggota[nama] = AnggotaOrganisasi(nama, jabatan)

    def tambah_hubungan(self, atasan, bawahan):
        self.anggota[atasan].tambah_bawahan(self.anggota[bawahan])

    def tampilkan_struktur(self, root, level=0):
        print("  " * level + f"- {root.jabatan}: {root.nama}")
        for b in root.bawahan:
            self.tampilkan_struktur(b, level + 1)


org = OrganisasiMahasiswa()

org.tambah_anggota("Andi", "Ketua")
org.tambah_anggota("Budi", "Wakil Ketua")
org.tambah_anggota("Siti", "Sekretaris")
org.tambah_anggota("Rina", "Bendahara")
org.tambah_anggota("Doni", "Koordinator Divisi pdd")
org.tambah_anggota("Beni", "Koordinator Divisi kestari")
org.tambah_anggota("Rudi", "Koordinator Divisi humas")

org.tambah_hubungan("Andi", "Budi")
org.tambah_hubungan("Budi", "Siti")
org.tambah_hubungan("Budi", "Rina")
org.tambah_hubungan("Rina", "Doni")
org.tambah_hubungan("Rina", "Beni")
org.tambah_hubungan("Rina", "Rudi")

root = org.anggota["Andi"]

print("Struktur Organisasi Mahasiswa:")
org.tampilkan_struktur(root)