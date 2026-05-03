Mengurutkan ukuran sepatu secara (Descending) menggunakan bubble short

program ini berfungsi untuk mengurutkan data ukuran sepatu yang dimasukkan oleh pengguna menggunakan metode Bubble Sort secara descending (dari terbesar ke terkecil). Program dimulai dengan meminta jumlah data, lalu pengguna menginput ukuran sepatu satu per satu yang disimpan dalam sebuah list. Setelah itu, data akan diurutkan dengan cara membandingkan elemen yang bersebelahan dan menukarnya jika urutannya belum sesuai. Sebelum dan sesudah proses pengurutan, program akan menampilkan isi array agar pengguna bisa melihat perubahan hasilnya.

Source Code :
<img width="1356" height="1698" alt="code" src="https://github.com/user-attachments/assets/b55d3f41-33d4-49d0-869e-41e1fd3f05f0" />

Penjelasannya :

Pada baris 1 terdapat fungsi tukar(arr, i, j) yang digunakan untuk menukar posisi dua elemen dalam array berdasarkan indeks i dan j.
Pada baris 2 terdapat variabel temp yang menyimpan sementara nilai dari arr[i] agar nilainya tidak hilang saat proses pertukaran.
Pada baris 3 nilai pada indeks i diisi dengan nilai dari indeks j, sehingga elemen pertama diganti dengan elemen kedua.
Pada baris 4 nilai pada indeks j diisi dengan nilai yang sebelumnya disimpan di variabel temp, sehingga proses pertukaran selesai.
Pada baris 6 terdapat fungsi bubble_sort(arr, n) yang berfungsi untuk mengurutkan array menggunakan algoritma Bubble Sort.
Pada baris 7 terdapat perulangan for i in range(n - 1) yang digunakan untuk menentukan jumlah iterasi sorting sebanyak panjang array dikurangi 1.
Pada baris 8 terdapat perulangan for j in range(n - i - 1) yang digunakan untuk membandingkan elemen yang bersebelahan dalam array.
Pada baris 9 terdapat kondisi if arr[j] < arr[j + 1] yang berarti jika elemen sekarang lebih kecil dari elemen setelahnya, maka kedua elemen harus ditukar agar urutan descending tercapai.
Pada baris 10 fungsi tukar(arr, j, j + 1) dipanggil untuk menukar posisi kedua elemen tersebut.
Pada baris 11 terdapat fungsi main() yang menjadi tempat utama program dijalankan.
Pada baris 12 terdapat blok try yang digunakan untuk menangani kemungkinan error ketika user memasukkan input.
Pada baris 13 terdapat variabel n yang digunakan untuk menyimpan jumlah data sepatu yang ingin dimasukkan user, dengan tipe data integer.
Pada baris 14 terdapat except ValueError yang akan menangkap error jika input yang dimasukkan user bukan angka.
Pada baris 15 program menampilkan pesan "Input tidak valid!" jika user memasukkan data yang salah.
Pada baris 16 terdapat return yang berfungsi menghentikan program jika terjadi error input.
Pada baris 18 dibuat variabel arr = [] yaitu list kosong untuk menyimpan ukuran sepatu.
Pada baris 19 terdapat perulangan for i in range(n) yang digunakan agar user dapat menginput data sebanyak jumlah yang sudah ditentukan sebelumnya.
Pada baris 20 program menampilkan teks "Masukkan ukuran sepatu:".
Pada baris 21 terdapat while True yang membuat perulangan terus berjalan sampai input valid diberikan.
Pada baris 22 terdapat blok try untuk menangani error input ukuran sepatu.
Pada baris 23 terdapat variabel nilai yang menyimpan input ukuran sepatu dari user dalam bentuk integer.
Pada baris 24 terdapat fungsi arr.append(nilai) yang digunakan untuk menambahkan data ukuran sepatu ke dalam list.
Pada baris 25 terdapat break yang berfungsi keluar dari perulangan while jika input sudah valid.
Pada baris 26 terdapat except ValueError untuk menangkap error jika input bukan angka.
Pada baris 27 program menampilkan pesan "Input tidak valid, silakan masukkan angka!" jika user salah memasukkan input.
Pada baris 28 program menampilkan isi array sebelum diurutkan menggunakan print(f"Array sebelum diurutkan: {arr}").
Pada baris 29 program memanggil fungsi bubble_sort(arr, n) untuk mengurutkan data ukuran sepatu secara descending.
Pada baris 30 program menampilkan teks "Array setelah diurutkan (Bubble Sort):" tanpa pindah baris karena menggunakan end=" ".
Pada baris 31 terdapat perulangan for i in range(n) untuk menampilkan seluruh elemen array yang sudah diurutkan.
Pada baris 32 program mencetak setiap elemen array satu per satu dengan spasi menggunakan print(arr[i], end=" ").
Pada baris 33 fungsi print() digunakan agar setelah semua data dicetak, kursor pindah ke baris baru.
Pada baris 36 terdapat if __name__ == "__main__": yang merupakan standar Python agar fungsi main() hanya dijalankan jika file dieksekusi langsung.
Pada baris 37 fungsi main() dipanggil untuk menjalankan keseluruhan program.

Output Program : 

<img width="714" height="312" alt="Screenshot 2026-05-03 201420" src="https://github.com/user-attachments/assets/008d60b1-b98e-4e5f-adeb-3f2db8813656" />


Program akan meminta user memasukkan jumlah sepatu terlebih dahulu. Setelah itu user diminta memasukkan ukuran sepatu sesuai jumlah data. Program akan menampilkan array sebelum diurutkan, lalu mengurutkannya menggunakan Bubble Sort secara descending sehingga data ditampilkan dari nilai terbesar ke terkecil.
