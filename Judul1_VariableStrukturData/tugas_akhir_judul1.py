def menu():
    print("\n=== APLIKASI DAFTAR BELANJA ===")
    print("1. Tambah Item Belanja")
    print("2. Lihat Daftar Belanja")
    print("3. Hapus Item Belanja (berdasarkan nomor)")
    print("4. Keluar")

def main():
    daftar_belanja = []
    
    while True:
        menu()
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            item = input("Masukkan nama item belanja: ")
            daftar_belanja.append(item)
            print(f"'{item}' berhasil ditambahkan ke daftar belanja.")

        elif pilihan == '2':
            print("\n DAFTAR ITEM BELANJA ANDA")
            if not daftar_belanja:
                print("Daftar masih kosong.")
            else:
                for i in range(len(daftar_belanja)):
                    print(f"{i + 1}. {daftar_belanja[i]}")

        elif pilihan == '3':
            if not daftar_belanja:
                print("Tidak ada item belanja yang bisa dihapus.")
            else:
                try:
                    nomor = int(input("Masukkan nomor item yang ingin dihapus: "))
                    if 1 <= nomor <= len(daftar_belanja):
                        dihapus = daftar_belanja.pop(nomor - 1)
                        print(f"'{dihapus}' telah dihapus dari daftar.")
                    else:
                        print("Nomor tidak valid.")
                except ValueError:
                    print("Masukkan angka yang benar!")

        elif pilihan == '4':
            print("Terima kasih! Jangan sampai ada yang tertinggal saat belanja.")
            break
        
        else:
            print("Pilihan tidak tersedia, silakan coba lagi.")

if __name__ == "__main__":
    main()