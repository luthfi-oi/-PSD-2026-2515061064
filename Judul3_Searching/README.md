Menemukan Nomor Kursi di Tumpukan Menggunakan Sequential searching

Program Sequential Searching untuk mencari nomor kursi yang ditumpuk berfungsi untuk membantu pengguna menemukan posisi nomor kursi tertentu di dalam sebuah kumpulan data secara berurutan. Program akan memeriksa setiap data mulai dari indeks pertama hingga terakhir sampai nomor kursi yang dicari ditemukan. Ketika program dijalankan, pengguna diminta memasukkan nomor kursi yang ingin dicari, kemudian sistem akan mengecek satu per satu isi data kursi menggunakan perulangan. Jika nomor kursi ditemukan, program akan menampilkan posisi tumpukan kursi tersebut, sedangkan jika data tidak ditemukan maka program akan memberikan pesan bahwa nomor kursi tidak ada di dalam daftar. Selain itu, program juga dilengkapi validasi input agar pengguna hanya dapat memasukkan angka sehingga dapat mengurangi terjadinya kesalahan saat proses pencarian berlangsung.

Source Code : 
<img width="1572" height="1356" alt="code" src="https://github.com/user-attachments/assets/ba1a1cac-14b5-4f6c-a61a-9bf7cdcb7667" />

Penjelasannya:
Pada baris pertama terdapat fungsi sequential_search(data, cari) yang digunakan untuk melakukan proses pencarian data menggunakan metode Sequential Search. Fungsi ini memiliki dua parameter yaitu data sebagai kumpulan data dan cari sebagai nilai yang ingin dicari.
Pada baris kedua terdapat variabel ditemukan yang diberi nilai False. Variabel ini berfungsi sebagai penanda apakah data yang dicari sudah ditemukan atau belum.
Pada baris keempat terdapat perulangan for i in range(len(data)): yang digunakan untuk memeriksa seluruh isi data satu per satu mulai dari indeks pertama hingga terakhir.
Pada baris kelima terdapat fungsi print yang digunakan untuk menampilkan proses pemeriksaan nomor kursi. Bagian i + 1 digunakan agar nomor indeks dimulai dari angka 1, bukan dari 0.
Pada baris ketujuh terdapat percabangan if data[i] == cari: yang berfungsi untuk mengecek apakah data pada indeks ke-i sama dengan nilai yang dicari user.
Pada baris kedelapan terdapat fungsi print yang digunakan untuk menampilkan bahwa nomor kursi yang dicari berhasil ditemukan beserta posisi tumpukannya.
Pada baris kesembilan variabel ditemukan diubah menjadi True yang menandakan bahwa data sudah berhasil ditemukan.
Pada baris kesepuluh terdapat fungsi break yang digunakan untuk menghentikan perulangan setelah data ditemukan sehingga program tidak melanjutkan pencarian ke indeks berikutnya.
Pada baris kedua belas terdapat percabangan if ditemukan == False: yang digunakan untuk mengecek apakah data tidak ditemukan setelah seluruh data diperiksa.
Pada baris ketiga belas terdapat fungsi print yang digunakan untuk menampilkan pesan bahwa nomor kursi yang dicari tidak ditemukan di dalam data.
Pada baris kelima belas terdapat fungsi main() yang digunakan sebagai tempat utama menjalankan program.
Pada baris keenam belas terdapat variabel data yang berisi list nomor kursi yaitu [10, 8, 3, 9, 7, 4, 6, 2, 5, 1].
Pada baris ketujuh belas terdapat fungsi print untuk menampilkan seluruh data nomor kursi yang tersedia.
Pada baris kedelapan belas terdapat perulangan while True: yang digunakan agar program terus meminta input sampai user memasukkan data yang benar.
Pada baris kesembilan belas terdapat try yang digunakan untuk menangani kemungkinan kesalahan input dari user.
Pada baris kedua puluh terdapat variabel cari yang digunakan untuk menyimpan input nomor kursi dari user dalam bentuk integer menggunakan fungsi int(input()).
Pada baris kedua puluh satu terdapat fungsi break yang digunakan untuk menghentikan perulangan jika input yang dimasukkan user sudah benar.
Pada baris kedua puluh dua terdapat except ValueError: yang digunakan untuk menangkap error jika user memasukkan input selain angka.
Pada baris kedua puluh tiga terdapat fungsi print yang digunakan untuk menampilkan pesan bahwa input tidak valid dan user harus memasukkan angka.
Pada baris kedua puluh lima terdapat pemanggilan fungsi sequential_search(data, cari) yang digunakan untuk menjalankan proses pencarian data berdasarkan input user.
Pada baris kedua puluh tujuh dan dua puluh delapan terdapat kode standar Python: Kode tersebut digunakan agar fungsi main() hanya dijalankan ketika file program dijalankan secara langsung, bukan ketika file diimpor ke program lain.

Output Program :

<img width="674" height="129" alt="Screenshot 2026-05-10 131303" src="https://github.com/user-attachments/assets/2a146498-3d53-479d-bc7f-c41d57cf6d12" />

Output program tersebut menunjukkan proses pencarian nomor kursi menggunakan metode Sequential Search atau pencarian berurutan. Pertama, program menampilkan data nomor kursi yang tersimpan dalam array yaitu [10, 8, 3, 9, 7, 4, 6, 2, 5, 1]. Setelah itu, pengguna memasukkan angka 3 sebagai nomor kursi yang ingin dicari. Program kemudian mulai memeriksa data satu per satu dari posisi pertama dengan menampilkan tulisan “Memeriksa kursi ke-1”, lalu dilanjutkan ke kursi ke-2 karena angka yang dicari belum ditemukan. Saat program memeriksa kursi ke-3, ditemukan bahwa nilai pada posisi tersebut adalah angka 3, sehingga proses pencarian dihentikan. Terakhir, program menampilkan pesan bahwa nomor kursi angka 3 ditemukan pada tumpukan atau posisi ke-3.

Link YouTube : https://youtu.be/toOra-ZkJVE?si=gIlhYYZk91CnJxh_

<img width="1290" height="1192" alt="WhatsApp Image 2026-05-11 at 21 58 14" src="https://github.com/user-attachments/assets/eb1dc7f9-a90f-42d5-ac3b-42a890bccab9" />



