

Hospital Patient Management System (Python CRUD)
*Proyek ini dibuat untuk memenuhi capstone project 2, kursus Bisnis Data Analis di Bootcamp Purwadhika*

Hospital Patient Management System adalah aplikasi berbasis Command Line Interface (CLI) yang dikembangkan menggunakan Python. Proyek ini bertujuan untuk mendigitalisasi manajemen data pasien di fasilitas kesehatan guna menggantikan pencatatan manual yang rentan terhadap kesalahan.

Aplikasi ini menerapkan konsep CRUD (Create, Read, Update, Delete) secara penuh dengan fokus pada integritas data, validasi input yang ketat, dan antarmuka tabel yang elegan untuk memudahkan operasional harian tenaga administrasi rumah sakit.

Selamat datang di Aplikasi Manajemen Data Pasien di Rumah Sakit
Sebuah aplikasi yang memungkinkan Anda mengelola basis Pasien di Rumah Sakit Anda. Fitur-fitur yang disediakan dalam aplikasi ini adalah:
1. Tampilkan Data Pasien (READ)
2. Tambah Data Pasien (CREATE)
3. Update Data Pasien (UPDATE)
4. Hapus Data Pasien (DELETE)
5. Keluar
<img width="653" height="223" alt="Screenshot 2026-02-10 222200" src="https://github.com/user-attachments/assets/2a7c717e-154f-430c-95dd-5a362f1fbad4" />


Berikut adalah langkah-langkah kerja aplikasi ini:
### 1. Inisialisasi Data (Pre-loaded Data)

Aplikasi memulai perjalanannya dengan menyediakan data awal (dummy data). Ini bertujuan agar user bisa langsung mencoba fitur aplikasi tanpa harus menginput data dari nol. Data ini mencakup ID pasien, nama, umur, diagnosa, hingga status perawatan.
<img width="1536" height="200" alt="Screenshot 2026-02-10 222621" src="https://github.com/user-attachments/assets/572966f5-3842-4142-8653-a66d8119f637" />

### 2. Dashboard Menu Utama

Begitu aplikasi dijalankan, user akan disambut dengan Menu Utama yang bersih dan intuitif. Menggunakan library `PrettyTable`, semua data akan disajikan dalam bentuk tabel yang rapi (seperti Excel) sehingga mata user tidak lelah saat membaca informasi.
<img width="786" height="236" alt="Screenshot 2026-02-10 222410" src="https://github.com/user-attachments/assets/b171c3cf-44c7-4ef1-9486-7264e834bf2c" />

### 3. Fitur Utama (Langkah demi Langkah):

* **Step 1: Menampilkan Data (READ)** 
Aplikasi tidak hanya menampilkan semua data sekaligus. User diberikan fleksibilitas untuk mencari data spesifik berdasarkan **ID Pasien** atau memfilter pasien berdasarkan **Status Perawatan** (misalnya: hanya ingin melihat pasien "Rawat Inap").
* *Nilai Tambah:* Mempercepat pengambilan keputusan medis dengan filter data yang akurat.
<img width="523" height="133" alt="Screenshot 2026-02-10 223046" src="https://github.com/user-attachments/assets/bb1124eb-9c9b-4146-8154-b83e29eeee7b" />

Menammpilkan Semua Data Pasien
<img width="827" height="296" alt="Screenshot 2026-02-10 222941" src="https://github.com/user-attachments/assets/97d5677e-2e54-4f7f-a352-f6e05400ece6" />

Menampilkan Data Pasien Berdasarkan ID
<img width="757" height="214" alt="Screenshot 2026-02-10 222935" src="https://github.com/user-attachments/assets/d0d207c8-d0d5-45cd-9ee7-b2cedf5736de" />

Menampilkan Data Pasien Berdasarkan Status
<img width="829" height="263" alt="Screenshot 2026-02-10 223007" src="https://github.com/user-attachments/assets/ebee6fc4-0670-45e6-bfdc-633377fb3324" />


* **Step 2: Menambah Pasien Baru (CREATE)** 
User dapat mendaftarkan pasien baru ke dalam sistem. Aplikasi dilengkapi dengan sistem **Validasi ID**, di mana sistem akan menolak jika ID yang dimasukkan sudah ada (mencegah duplikasi data).
* *Nilai Tambah:* Menjamin integritas data agar tidak ada ID ganda dalam satu database.
<img width="363" height="136" alt="Screenshot 2026-02-10 223454" src="https://github.com/user-attachments/assets/6d4244fc-d612-4e52-b3c7-6f7f14c14254" />
<img width="804" height="641" alt="Screenshot 2026-02-10 223546" src="https://github.com/user-attachments/assets/5e6a03a5-c110-484c-b1ce-5fd4b515cf53" />

* **Step 3: Memperbarui Informasi (UPDATE)** 
Kondisi pasien bisa berubah kapan saja. User dapat memilih untuk mengubah **seluruh data** sekaligus atau **hanya bagian tertentu** (misalnya hanya mengubah diagnosa atau status perawatan saja).
* *Nilai Tambah:* Fleksibilitas pengeditan yang menghemat waktu user karena tidak perlu mengetik ulang semua data.
  
<img width="388" height="123" alt="Screenshot 2026-02-10 223641" src="https://github.com/user-attachments/assets/af346e69-ee85-4d17-acce-57bff09a34f0" />


Mengubah Seluruh Data

<img width="818" height="550" alt="Screenshot 2026-02-10 223737" src="https://github.com/user-attachments/assets/60d25cb2-3171-4e8f-8881-8d4a8d9efc73" />


Mengubah Data Tertentu

<img width="782" height="677" alt="Screenshot 2026-02-10 223932" src="https://github.com/user-attachments/assets/17fe33d6-b529-469f-b57e-9676de18ea12" />

* **Step 4: Menghapus Data (DELETE)** 
Jika pasien sudah keluar atau ada kesalahan input, data bisa dihapus. Sebelum benar-benar terhapus, aplikasi akan meminta **Konfirmasi Ulang (y/n)** untuk memastikan tidak ada data yang terhapus secara tidak sengaja.
* *Nilai Tambah:* Keamanan data ekstra dengan fitur konfirmasi sebelum aksi penghapusan.

<img width="808" height="368" alt="Screenshot 2026-02-10 224209" src="https://github.com/user-attachments/assets/20955980-cc7e-4117-8b29-c156eb4431a8" />


<img width="817" height="888" alt="Screenshot 2026-02-10 224124" src="https://github.com/user-attachments/assets/feecb1cd-1610-4dd9-8abb-ec24feb2f20b" />


### 4. Sistem Validasi & Error Handling

Aplikasi ini cukup cerdas untuk menangani kesalahan user. Contohnya, jika user diminta memasukkan angka pada kolom "Umur" namun malah memasukkan huruf, aplikasi akan memberikan pesan error yang ramah dan meminta input ulang tanpa membuat program berhenti mendadak (*crash*).
<img width="447" height="268" alt="Screenshot 2026-02-10 224510" src="https://github.com/user-attachments/assets/8f301f12-fd76-46d0-8c8e-4e80e28cf852" />

### 5. Navigasi & Keluar Aplikasi

Setiap selesai melakukan sebuah aksi, aplikasi akan bertanya apakah user ingin kembali ke menu utama atau tetap di menu tersebut. Saat ingin keluar, user kembali dimintai konfirmasi untuk mencegah tertutupnya aplikasi secara tidak sengaja.
<img width="861" height="243" alt="Screenshot 2026-02-10 224558" src="https://github.com/user-attachments/assets/f0251713-4225-448b-9416-176400a692b8" />

---
This app is created by Yoseph C L / @yosephcl. You can reach me through any social media GitHub, LinkedIn, and IG

###  Mengapa Aplikasi Ini Berbeda?

* **User-Centric Design:** Meski berbasis terminal, penggunaan tabel membuat tampilan tetap estetik dan mudah dibaca.
* **Safe Interaction:** Setiap aksi kritikal (seperti hapus atau keluar) selalu membutuhkan konfirmasi user.
* **Clean Code:** Dibangun dengan fungsi (`def`) yang modular, sehingga kode mudah dikembangkan atau diintegrasikan ke sistem yang lebih besar di masa depan.
