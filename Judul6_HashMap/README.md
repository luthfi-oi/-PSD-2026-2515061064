Membuat Sistem Daftar Harga Ikan dan Ayam dengan metode Open Addressing

Program ini berfungsi sebagai sistem daftar harga ikan dan ayam yang menggunakan struktur data Hash Map dengan metode Open Addressing (Linear Probing) untuk menyimpan dan mengelola data. Setiap produk memiliki kode, kategori, nama, dan harga yang disimpan ke dalam hash table sehingga data dapat diorganisasikan dengan lebih terstruktur. Program juga menyediakan menu interaktif yang memungkinkan pengguna melihat daftar harga ikan, melihat daftar harga ayam, menampilkan seluruh data, atau keluar dari program. Dengan adanya perulangan while True dan percabangan if-elif-else, program dapat terus berjalan dan menerima pilihan pengguna hingga pengguna memilih menu keluar. Secara keseluruhan, program ini merupakan implementasi sederhana dari konsep **Hash Map, perulangan, dan percabangan** dalam Python untuk mengelola data harga produk.

Source Code:

<img width="1278" height="5270" alt="code" src="https://github.com/user-attachments/assets/3b61c959-41b2-4f07-b4a4-a3ea948d5758" />

Penjelasannya:

Pada baris 1 terdapat kelas `SlotState` yang digunakan untuk menentukan status dari setiap slot pada hash table. Pada baris 2 terdapat Variable `EMPTY = 0` yang menandakan slot masih kosong. Pada baris 3 terdapat variable `OCCUPIED = 1` yang menandakan slot telah terisi data. Pada baris 4 terdapat variabel `DELETED = 2` yang menandakan data pada slot telah dihapus.

Pada baris 7 terdapat kelas `Entry` yang digunakan sebagai tempat penyimpanan data pada setiap slot hash table. Pada baris 8 terdapat fungsi konstruktor `__init__()` yang akan dijalankan secara otomatis saat objek dibuat. Pada baris 9 terdapat atribut `key` yang diinisialisasi dengan nilai `None`. Pada baris 10 terdapat atribut `value` yang juga diinisialisasi dengan nilai `None`. Pada baris 11 terdapat atribut `state` yang diisi dengan status `EMPTY`.

Pada baris 14 terdapat kelas `HashMapOpenAddressing` yang digunakan untuk mengimplementasikan struktur data Hash Map menggunakan metode Open Addressing. Pada baris 15 terdapat fungsi konstruktor `__init__()` yang menerima parameter ukuran tabel dengan nilai default 20. Pada baris 16 terdapat variabel `SIZE` yang digunakan untuk menyimpan ukuran hash table. Pada baris 17 terdapat variabel `table` yang berisi daftar objek `Entry` sebanyak ukuran hash table menggunakan list comprehension.

Pada baris 19 terdapat fungsi `hash_function()` yang digunakan untuk menghitung indeks penyimpanan data berdasarkan nilai key. Pada baris 20 terdapat operasi `key % self.SIZE` yang menghasilkan indeks penyimpanan pada hash table.

Pada baris 22 terdapat fungsi `insert()` yang digunakan untuk memasukkan data ke dalam hash table. Pada baris 23 terdapat variabel `idx` yang menyimpan hasil dari fungsi hash. Pada baris 25 terdapat perulangan `for` yang digunakan untuk melakukan pencarian slot kosong apabila terjadi collision. Pada baris 26 terdapat variabel `i` yang digunakan untuk menghitung posisi penyimpanan menggunakan metode Linear Probing.

Pada baris 28 terdapat percabangan `if` yang memeriksa apakah slot belum terisi data. Pada baris 29 data key disimpan ke dalam slot hash table. Pada baris 30 data value disimpan ke dalam slot tersebut. Pada baris 31 status slot diubah menjadi `OCCUPIED`. Pada baris 32 fungsi mengembalikan nilai `True` yang menunjukkan bahwa proses penyimpanan berhasil dilakukan. Pada baris 34 fungsi mengembalikan nilai `False` apabila tidak ditemukan slot kosong.

Pada baris 36 terdapat fungsi `display_by_category()` yang digunakan untuk menampilkan data berdasarkan kategori tertentu. Pada baris 37 terdapat perintah `print()` yang digunakan untuk menampilkan judul kategori yang dipilih. Pada baris 39 terdapat variabel `ditemukan` yang digunakan sebagai penanda apakah data ditemukan atau tidak.

Pada baris 41 terdapat perulangan `for` yang digunakan untuk memeriksa seluruh isi hash table. Pada baris 42 sampai 43 terdapat percabangan yang memeriksa apakah slot berstatus `OCCUPIED` dan kategori data sesuai dengan kategori yang dipilih pengguna.

Pada baris 45 sampai 49 terdapat perintah `print()` yang digunakan untuk menampilkan informasi produk berupa kode, nama, dan harga per kilogram. Pada baris 50 variabel `ditemukan` diubah menjadi `True` karena data berhasil ditemukan.

Pada baris 52 terdapat percabangan `if not ditemukan` yang digunakan untuk memeriksa apakah tidak ada data yang sesuai dengan kategori yang dipilih. Pada baris 53 program akan menampilkan pesan "Data tidak ditemukan".

Pada baris 56 terdapat fungsi `main()` yang menjadi pusat jalannya program. Pada baris 57 dibuat objek `hashmap` dari kelas `HashMapOpenAddressing`.

Pada baris 59 sampai 81 terdapat beberapa pemanggilan fungsi `insert()` untuk memasukkan data ikan ke dalam hash table. Data yang dimasukkan terdiri dari kode ikan, kategori, nama ikan, dan harga ikan per kilogram. Data yang dimasukkan yaitu Lele, Nila, Patin, dan Gurame.

Pada baris 83 sampai 99 terdapat beberapa pemanggilan fungsi `insert()` untuk memasukkan data ayam ke dalam hash table. Data yang dimasukkan yaitu Ayam Broiler, Ayam Kampung, dan Ayam Pejantan beserta harga per kilogramnya.

Pada baris 101 terdapat perulangan `while True` yang digunakan agar program terus berjalan hingga pengguna memilih menu keluar.

Pada baris 102 sampai 108 terdapat beberapa perintah `print()` yang digunakan untuk menampilkan menu program. Menu yang tersedia adalah melihat harga ikan, melihat harga ayam, melihat seluruh data, dan keluar dari program.

Pada baris 110 terdapat variabel `pilihan` yang digunakan untuk menerima input dari pengguna berupa nomor menu yang dipilih.

Pada baris 112 terdapat percabangan `if` yang akan dijalankan apabila pengguna memasukkan angka 1. Pada baris 113 fungsi `display_by_category("ikan")` dipanggil untuk menampilkan seluruh daftar harga ikan.

Pada baris 115 terdapat percabangan `elif` yang akan dijalankan apabila pengguna memasukkan angka 2. Pada baris 116 fungsi `display_by_category("ayam")` dipanggil untuk menampilkan seluruh daftar harga ayam.

Pada baris 118 terdapat percabangan `elif` yang akan dijalankan apabila pengguna memasukkan angka 3. Pada baris 119 dan 120 program akan menampilkan seluruh daftar harga ikan dan ayam secara bersamaan.

Pada baris 122 terdapat percabangan `elif` yang akan dijalankan apabila pengguna memasukkan angka 4. Pada baris 123 program menampilkan pesan terima kasih kepada pengguna. Pada baris 124 terdapat perintah `break` yang digunakan untuk menghentikan perulangan sehingga program selesai dijalankan.

Pada baris 126 terdapat percabangan `else` yang akan dijalankan apabila pengguna memasukkan pilihan selain angka 1 sampai 4. Pada baris 127 program akan menampilkan pesan bahwa pilihan yang dimasukkan tidak valid.

Pada baris 130 terdapat kode `if __name__ == "__main__":` yang digunakan untuk memastikan bahwa fungsi `main()` hanya akan dijalankan ketika file dieksekusi secara langsung.

Pada baris 131 terdapat pemanggilan fungsi `main()` yang digunakan untuk menjalankan seluruh program sehingga menu daftar harga ikan dan ayam dapat digunakan oleh pengguna.

Outputnya:
<img width="1391" height="915" alt="Screenshot 2026-06-08 095052" src="https://github.com/user-attachments/assets/cb139ae7-7593-4b61-bdaa-27d94dcc950c" />

Penjelasannya: 

Pada tampilan awal, program menampilkan menu utama yang berisi empat pilihan, yaitu Lihat Harga Ikan, Lihat Harga Ayam, Lihat Semua, dan Keluar. Pengguna kemudian diminta memasukkan pilihan dengan angka 1 sampai 4. Pada percobaan pertama, pengguna memasukkan angka 1. Karena memilih menu Lihat Harga Ikan, program menampilkan seluruh data ikan yang telah disimpan pada Hash Map. Data yang ditampilkan terdiri dari kode ikan, nama ikan, dan harga per kilogram. Data yang muncul yaitu Lele dengan harga Rp25.000/kg, Nila dengan harga Rp30.000/kg, Patin dengan harga Rp28.000/kg, dan Gurame dengan harga Rp45.000/kg. Setelah seluruh data ikan ditampilkan, program tidak langsung berhenti karena menggunakan perulangan while True. Oleh karena itu, menu utama ditampilkan kembali sehingga pengguna dapat memilih menu lainnya. Pada percobaan kedua, pengguna memasukkan angka 2. Karena memilih menu Lihat Harga Ayam, program menampilkan seluruh data ayam yang tersimpan pada Hash Map. Data yang ditampilkan meliputi Ayam Broiler dengan harga Rp38.000/kg, Ayam Kampung dengan harga Rp65.000/kg, dan Ayam Pejantan dengan harga Rp50.000/kg. Setelah data ayam ditampilkan, program kembali menampilkan menu utama. Hal ini menunjukkan bahwa perulangan masih berjalan dan program masih menunggu pilihan berikutnya dari pengguna. Pada percobaan terakhir, pengguna memasukkan angka 4. Pilihan ini mengaktifkan percabangan Keluar sehingga program menampilkan pesan "Terima kasih telah menggunakan program.". Setelah itu, perintah break dijalankan untuk menghentikan perulangan while True, sehingga program selesai dan kembali ke terminal.

Link YouTube: 
