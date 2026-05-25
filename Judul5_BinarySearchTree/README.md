Membuat Struktur Organisasi Mahasiswa Menggunakan Binary Search Tree

Kode ini berfungsi untuk membuat sistem sederhana yang dapat merepresentasikan struktur organisasi mahasiswa secara terstruktur dan bertingkat. Program ini menggunakan konsep pemrograman berorientasi objek untuk menyimpan data setiap anggota organisasi beserta jabatannya, serta menghubungkan anggota sebagai atasan dan bawahan. Selain itu, kode ini juga mampu menampilkan susunan organisasi dalam bentuk hierarki seperti pohon, dimulai dari ketua hingga anggota di bawahnya, sehingga memudahkan pengguna dalam memahami hubungan dan posisi setiap anggota dalam organisasi.

Source Code:
<img width="1326" height="2078" alt="code ta 5" src="https://github.com/user-attachments/assets/05b764a7-4ea4-4c58-a89d-53f44e37cc58" />

Penjelasannya:
Pada baris pertama terdapat deklarasi class AnggotaOrganisasi, yang berfungsi untuk merepresentasikan setiap anggota dalam organisasi mahasiswa. Pada baris kedua 
terdapat fungsi __init__ yang digunakan sebagai constructor untuk menginisialisasi objek dengan parameter nama dan jabatan. Pada baris ketiga dan keempat, nilai
nama dan jabatan disimpan ke dalam atribut objek menggunakan self.nama dan self.jabatan. Pada baris kelima dibuat variabel bawahan berupa list kosong yang nantinya
akan digunakan untuk menyimpan anggota-anggota yang berada di bawahnya. Pada baris ketujuh terdapat fungsi tambah_bawahan yang berfungsi untuk menambahkan anggota 
lain sebagai bawahan. Pada baris kedelapan, fungsi .append() digunakan untuk memasukkan objek anggota ke dalam list bawahan. Pada baris kesebelas terdapat 
deklarasi class OrganisasiMahasiswa yang berfungsi sebagai pengelola seluruh anggota organisasi. Pada baris kedua belas terdapat fungsi __init__ yang digunakan 
untuk membuat variabel anggota berupa dictionary kosong. Dictionary ini digunakan untuk menyimpan data anggota dengan format pasangan key dan value, dimana key 
berupa nama anggota dan value berupa objek AnggotaOrganisasi. Pada baris kelima belas terdapat fungsi tambah_anggota yang digunakan untuk menambahkan anggota baru 
ke dalam organisasi. Pada baris keenam belas, dibuat objek AnggotaOrganisasi berdasarkan nama dan jabatan yang diberikan, kemudian disimpan ke dalam dictionary 
anggota. Pada baris kedelapan belas terdapat fungsi tambah_hubungan yang berfungsi untuk membuat relasi antara atasan dan bawahan. Pada baris kesembilan belas, 
program mengambil objek atasan dari dictionary, kemudian memanggil fungsi tambah_bawahan untuk menambahkan bawahan ke dalam list bawahan milik atasan tersebut.
Pada baris kedua puluh satu terdapat fungsi tampilkan_struktur yang berfungsi untuk menampilkan struktur organisasi secara hierarki. Parameter root digunakan 
sebagai titik awal struktur, sedangkan level digunakan untuk menentukan kedalaman atau tingkat dalam struktur. Pada baris kedua puluh dua, program mencetak 
jabatan dan nama anggota dengan tambahan spasi sesuai level agar tampilan menjadi bertingkat. Pada baris kedua puluh tiga dilakukan perulangan untuk setiap 
bawahan yang dimiliki oleh anggota tersebut. Pada baris kedua puluh empat, fungsi yang sama dipanggil kembali secara rekursif dengan level yang ditambah satu 
untuk menampilkan struktur yang lebih dalam. Pada baris kedua puluh tujuh dibuat objek org dari class OrganisasiMahasiswa. Pada baris kedua puluh sembilan sampai 
tiga puluh lima, program menambahkan beberapa anggota organisasi seperti Ketua, Wakil Ketua, Sekretaris, Bendahara, serta beberapa Koordinator Divisi ke dalam 
dictionary anggota. Pada baris ketiga puluh tujuh sampai empat puluh dua, program membuat hubungan antara atasan dan bawahan, dimana Andi sebagai Ketua memiliki 
bawahan Budi, kemudian Budi memiliki bawahan Siti dan Rina, dan Rina memiliki bawahan Doni, Beni, serta Rudi. Pada baris keempat puluh empat, variabel root diisi 
dengan objek anggota bernama Andi yang berperan sebagai Ketua, sehingga struktur organisasi akan ditampilkan mulai dari Andi sebagai akar. Pada baris keempat 
puluh enam, program mencetak judul “Struktur Organisasi Mahasiswa”. Pada baris keempat puluh tujuh, method tampilkan_struktur dipanggil untuk menampilkan seluruh 
struktur organisasi secara bertingkat 

Outputnya: 

<img width="875" height="262" alt="Screenshot 2026-05-25 205903" src="https://github.com/user-attachments/assets/2861f943-70a0-4789-aa4d-fc2ea8da5bdd" />

Penjelasannya:


