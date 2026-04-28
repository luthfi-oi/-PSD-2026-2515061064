Daftar Belanja Menggunakan List 1 Dimensi

Program ini berfungsi sebagai asisten digital sederhana untuk membantu pengguna mengelola daftar barang yang perlu dibeli. 
Pengguna dapat melakukan operasi dasar pengelolaan data secara interaktif, yaitu menambah barang baru ke dalam daftar, 
menampilkan seluruh isi daftar secara berurutan, serta menghapus item tertentu berdasarkan nomor urutnya. Secara keseluruhan, 
program ini mengubah proses pencatatan manual menjadi sistem manajemen data yang terstruktur.

Struktur data utama yang diterapkan adalah List, yang merupakan implementasi dari variabel. Algoritma yang digunakan 
mencakup operasi penyisipan menggunakan metode .append() untuk menambah data di akhir memori, serta operasi 
penghapusan menggunakan metode .pop().


Source Code :
<img width="1572" height="2192" alt="ss percobaan 1" src="https://github.com/user-attachments/assets/3ab068c7-4c07-4c17-87b7-e6eab2667352" />

Penjelasannya: 

Pada baris pertama ada fungsi menu, fungsi ini bertugas mencetak teks pilihan menu ke layer. Pada baris kedua sampai keenam merupakan isi dari fungsi menu yang nanti akan ditampilkan di output. Pada baris kedelapan ada fungsi main yang dimana fungsi ini untuk tempat program dijalankan. Pada baris kesembilan merupakan variable daftar belanja yang dimana isinya list kosong. Pada baris kesebelas ada fungsi while true yang dimana tugasnya membuat perulangan yang tidak akan berhenti selama kondisinya benar. Pada baris kedua belas memanggil fungsi menu. Pada baris ketiga belas ada variable pilihan yang dimana user harus menginputkan nomor 1 sampai 4. Pada baris kelima belas ada fungsi if yang dimana jika user menginputkan angka 1 program akan menjalankan kode baris keenam belas sampai delapan belas. Pada baris keenam belas terdapat variable item untuk menginputkan item belanja. Pada baris ketujuh belas terdapat fungsi append berguna untuk menambahkan elemen baru ke posisi paling akhir. Pada baris kedelapan belas terdapat print untuk menampilkan item yang telah ditambahkan. Pada baris kedua puluh terdapat elif yang dimana jika user menginputkan angka 2 program akan menjalankan kode baris kedua puluh satu sampai dua puluh enam. Pada baris kedua puluh satu terdapat print untuk menampilkan kalimat daftar item belanja anda. Pada baris kedua puluh dua ada fungsi if not yang dimana jika variabel daftar belanja belum ada item yang diinputkan user maka pada baris kedua puluh tiga akan menampilkan daftar masih kosong. Pada baris kedua puluh empat ada else yang dimana jika variabel daftar belanja terapat item maka kode baris kedua puluh lima dan dua puluh enam akan menampilkan item yang ada di daftar belanja. Pada baris ke dua puluh enam terdapat i + 1 yang dimana agar indeks dimulai dari angka 1 bukan 0. Pada baris kedua puluh delapan terdapat elif yang dimana jika user menginputkan angka 3 maka program akan menjalankan kode baris kedua puluh sembilan sampai baris ke empat puluh. Pada baris keduapuluh sembilan ada fungsi if not yang dimana jika variabel daftar belanja belum ada item maka pada baris ketiga puluh ada print yang akan menampilkan kalimat tidak ada item belanja yang bisa dihapus. Pada baris ketiga puluh satu ada fungsi else yang merupakan percabangan dari if. Pada baris ke tiga puluh dua ada fungsi try untuk menangani kesalahan. Pada baris ke tiga puluh tiga terdapat variabel nomor yang berupa integer yang dimana user diminta menginputkan nomor angka yang ingin dihapus. Pada baris ke tiga puluh empat ada if yang dimana nomor yang dinputkan harus lebih dari sama dengan satu dan kurang dari sama dengan panjang pada daftar belanja. Pada baris ketiga puluh lima ada variabel dihapus yang isi nya ada fungsi pop berguna untuk menghapus item di daftar belanja. Pada baris ke tiga puluh enam ada kode print untuk menampilkan item apa yang dihapus. Pada baris ketiga puluh tujuh ada else yang dimana jika user tidak menginputkan angka yang tidak valid maka program akan menampilkan nomor tidak valid. Pada baris ketiga puluh sembilan ada except valueerror digunakan untuk menangkap error. Pada baris keempat puluh program akan menampilkan masukkan angka yang benar jika terjadi valueerror. Pada bari keempat puluh dua ada elif jika user menginputkan angka 4 maka program akan berhenti karna ada fungsi break. Pada baris ke empat puluh sembilan dan lima puluh kode tersebut adalah standar di Python untuk memastikan bahwa fungsi main() hanya akan dipanggil jika file ini dijalankan secara langsung, bukan saat diimpor oleh file lain. 

Output Program : 
<img width="613" height="581" alt="Screenshot 2026-04-28 201543" src="https://github.com/user-attachments/assets/b09a917c-8e0b-428c-b021-34c70af1c6dd" />
<img width="555" height="642" alt="Screenshot 2026-04-28 201525" src="https://github.com/user-attachments/assets/5cf1d186-258e-4547-93c1-5f55c6188fb1" />



