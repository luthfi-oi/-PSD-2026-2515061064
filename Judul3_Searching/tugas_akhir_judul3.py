def sequential_search(data, cari):
    ditemukan = False

    for i in range(len(data)):
        print("Memeriksa kursi ke-", i + 1)

        if data[i] == cari:
            print("Nomor kursi angka", cari, "ditemukan pada tumpukan ke-", i + 1)
            ditemukan = True
            break

    if ditemukan == False:
        print("Nomor kursi angka", cari, "tidak ditemukan")
 
def main(): 
    data = [10, 8, 3, 9, 7, 4, 6, 2, 5, 1] 
    print(f"Data nomor kursi: {data}") 
    while True: 
        try: 
            cari = int(input("Masukkan nomor kursi yang ingin dicari: ")) 
            break 
        except ValueError: 
            print("Input tidak valid, silakan masukkan angka!") 

    sequential_search(data, cari)
 
if __name__ == "__main__": 
    main() 