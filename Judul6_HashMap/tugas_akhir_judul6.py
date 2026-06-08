class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2


class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY


class HashMapOpenAddressing:
    def __init__(self, size=20):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return key % self.SIZE

    def insert(self, key, value):
        idx = self.hash_function(key)

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE

            if self.table[i].state != SlotState.OCCUPIED:
                self.table[i].key = key
                self.table[i].value = value
                self.table[i].state = SlotState.OCCUPIED
                return True

        return False

    def display_by_category(self, kategori):
        print(f"\n=== DAFTAR HARGA {kategori.upper()} ===")

        ditemukan = False

        for entry in self.table:
            if (entry.state == SlotState.OCCUPIED and
                    entry.value["kategori"] == kategori):

                print(
                    f"Kode : {entry.key} | "
                    f"Nama : {entry.value['nama']} | "
                    f"Harga : Rp{entry.value['harga']:,}/kg"
                )
                ditemukan = True

        if not ditemukan:
            print("Data tidak ditemukan.")


def main():
    hashmap = HashMapOpenAddressing()

    hashmap.insert(101, {
        "kategori": "ikan",
        "nama": "Lele",
        "harga": 25000
    })

    hashmap.insert(102, {
        "kategori": "ikan",
        "nama": "Nila",
        "harga": 30000
    })

    hashmap.insert(103, {
        "kategori": "ikan",
        "nama": "Patin",
        "harga": 28000
    })

    hashmap.insert(104, {
        "kategori": "ikan",
        "nama": "Gurame",
        "harga": 45000
    })

    hashmap.insert(201, {
        "kategori": "ayam",
        "nama": "Ayam Broiler",
        "harga": 38000
    })

    hashmap.insert(202, {
        "kategori": "ayam",
        "nama": "Ayam Kampung",
        "harga": 65000
    })

    hashmap.insert(203, {
        "kategori": "ayam",
        "nama": "Ayam Pejantan",
        "harga": 50000
    })

    while True:
        print("\n==============================")
        print(" SISTEM DAFTAR HARGA")
        print("==============================")
        print("1. Lihat Harga Ikan")
        print("2. Lihat Harga Ayam")
        print("3. Lihat Semua")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1-4): ")

        if pilihan == "1":
            hashmap.display_by_category("ikan")

        elif pilihan == "2":
            hashmap.display_by_category("ayam")

        elif pilihan == "3":
            hashmap.display_by_category("ikan")
            hashmap.display_by_category("ayam")

        elif pilihan == "4":
            print("\nTerima kasih telah menggunakan program.")
            break

        else:
            print("\nPilihan tidak valid! Silakan coba lagi.")


if __name__ == "__main__":
    main()