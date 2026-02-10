# CAPSTONE PROJECT MODUL 2
# Yoseph Cristaday Limbong
# MEMBUAT APLIKASI DENGAN BASIS FITUR CRUD
# DATA PASIEN PADA RUMAH SAKIT

# Import
from prettytable import PrettyTable
import os

# Data Awal
data_pasien = [
    {"id": "P001", "nama": "Andi Cahyadi", "umur": 30, "gender": "Laki-laki", "diagnosa": "Demam", "status": "Rawat Jalan"},
    {"id": "P002", "nama": "Budi Setiawan", "umur": 45, "gender": "Laki-laki", "diagnosa": "Diabetes", "status": "Rawat Inap"},
    {"id": "P003", "nama": "Citra Kirana D", "umur": 28, "gender": "Perempuan", "diagnosa": "Flu", "status": "Rawat Jalan"},
    {"id": "P004", "nama": "Dewi Yahya", "umur": 35, "gender": "Perempuan", "diagnosa": "Asma", "status": "Rawat Inap"},
    {"id": "P005", "nama": "M.Eko", "umur": 50, "gender": "Laki-laki", "diagnosa": "Hipertensi", "status": "Rawat Jalan"},
]

# Fungsi Def
def tampilkan_tabel(daftar, judul="\nDAFTAR DATA PASIEN"):
    """Fungsi untuk menampilkan data dalam bentuk PrettyTable"""
    if not daftar:
        print("\n[!] Data tidak ditemukan.")
    else:
        table = PrettyTable()
        table.field_names = ["ID", "Nama", "Umur", "Gender", "Diagnosa", "Status"]
        for pasien in daftar:
            table.add_row([
                pasien["id"], pasien["nama"], pasien["umur"], 
                pasien["gender"], pasien["diagnosa"], pasien["status"]
            ])
        print(judul)
        print(table)

def konfirmasi_kembali(pesan="\nKembali ke menu utama? (y/n): "):
    """Fungsi untuk validasi input y/n (pengganti variabel pilih_kembali)"""
    while True:
        pilih = input(pesan).lower()
        if pilih == 'y':
            return True
        elif pilih == 'n':
            return False
        else:
            print("Input tidak valid, silahkan pilih y atau n")

def clearScreenView() :
    if os.name == 'nt' : # for windows
        os.system('cls')

# ================= PROGRAM UTAMA =================
clearScreenView()
while True:
    print("\n=== SELAMAT DATANG DI SISTEM DATA PASIEN RUMAH SAKIT ===")
    print("1. Tampilkan Data Pasien (READ)")
    print("2. Tambah Data Pasien (CREATE)")
    print("3. Update Data Pasien (UPDATE)")
    print("4. Hapus Data Pasien (DELETE)")
    print("5. Keluar")
    
    pilihan_menu = input("Pilih menu (1-5): ")

    # ================= Menampilkan Data Pasien =================
    if pilihan_menu == "1":   # READ
        while True:
            print("\n--- MENU TAMPILKAN DATA PASIEN ---")
            print("1. Tampilkan Semua Data Pasien")
            print("2. Tampilkan Data Pasien Berdasarkan ID")
            print("3. Tampilkan Data Pasien Berdasarkan Status")
            print("4. Kembali ke Menu Utama")

            pilihan_read = input("Pilih menu (1-4): ")

            #  1. TAMPILKAN SEMUA DATA  
            if pilihan_read == "1":
                if len(data_pasien) == 0:
                    print("\nData pasien belum tersedia.")
                else:
                    tampilkan_tabel(data_pasien) # Menggunakan fungsi def)
                    
            #  2. BERDASARKAN ID 
            elif pilihan_read == "2":
                cari_id = input("Masukkan ID Pasien: ")
                hasil = [p for p in data_pasien if p["id"] == cari_id]
                if hasil:
                    tampilkan_tabel(hasil, "\nDATA PASIEN DITEMUKAN")
                else:
                    print("\n Data pasien dengan ID tersebut tidak ditemukan.")

            #   3. BERDASARKAN STATUS
            elif pilihan_read == "3":
                cari_status = input("Masukkan Status Perawatan: ")
                hasil = [p for p in data_pasien if p["status"].lower() == cari_status.lower()]
                tampilkan_tabel(hasil, "\nDATA PASIEN BERDASARKAN STATUS")

            #  4. KEMBALI 
            elif pilihan_read == "4":
                break
            else:
                print("Pilihan tidak valid di menu READ")

    # ================= Menambah Data Pasien =================
    elif pilihan_menu == "2":   # CREATE
        while True:
            print("\n--- MENU TAMBAH DATA PASIEN ---")
            print("1. Tambah Data Pasien Baru")
            print("2. Kembali ke Menu Utama")

            pilihan_create = input("Pilih menu (1-2): ")

            if pilihan_create == "1":
                id_baru = input("Masukkan ID Pasien: ")

                id_ada = False
                for pasien in data_pasien:
                    if pasien["id"] == id_baru:
                        id_ada = True
                        break

                if id_ada:
                    print("ID sudah digunakan.")
                else:
                    nama = input("Nama Pasien: ")
                    while True:
                        try:
                            umur = int(input("Umur Pasien: "))
                            break
                        except ValueError:
                            print("Error: Mohon masukkan angka untuk umur!")
                    gender = input("Jenis Kelamin (Laki-Laki/Perempuan): ")
                    diagnosa = input("Diagnosa: ")
                    status = input("Status Perawatan (Rawat Jalan/Rawat Inap): ")

                    data_pasien.append({
                        "id": id_baru,
                        "nama": nama,
                        "umur": umur,
                        "gender": gender,
                        "diagnosa": diagnosa,
                        "status": status
                    })

                    print("\nData pasien berhasil ditambahkan.")
                    tampilkan_tabel(data_pasien, "\nDATA PASIEN TERKINI")
            elif pilihan_create == "2":
                break
            else:
                print("Pilihan tidak valid.")
    
    # ================= Mengupdate Data Pasien =================
    elif pilihan_menu == "3":   # UPDATE DATA PASIEN
        while True:
            print("\n--- MENU UPDATE DATA PASIEN ---")
            print("1. Update Seluruh Data Pasien")
            print("2. Update Data Tertentu")
            print("3. Kembali ke Menu Utama")

            pilihan_update = input("Pilih menu (1-3): ")

            if pilihan_update in ["1", "2"]:
                cari_id = input("Masukkan ID Pasien: ")
                ditemukan = False

                for pasien in data_pasien:
                    if pasien["id"] == cari_id:
                        ditemukan = True

                        # UPDATE SELURUH DATA
                        if pilihan_update == "1":
                            pasien["nama"] = input("Nama Baru: ")
                            while True:
                                try:
                                    pasien["umur"] = int(input("Umur Pasien: "))
                                    break
                                except ValueError:
                                    print("Error: Mohon masukkan angka untuk umur!")
                            pasien["gender"] = input("Gender Baru (Laki-Laki/Perempuan): ")
                            pasien["diagnosa"] = input("Diagnosa Baru: ")
                            pasien["status"] = input("Status Baru (Rawat Jalan/Rawat Inap): ")
                            print("Data pasien berhasil diupdate.")

                        # UPDATE DATA TERTENTU
                        else:
                            print("\nPilih data yang ingin diubah:")
                            print("1. Nama")
                            print("2. Umur")
                            print("3. Gender")
                            print("4. Diagnosa")
                            print("5. Status")

                            field = input("Pilih (1-5): ")

                            if field == "1":
                                pasien["nama"] = input("Nama Baru: ")
                            elif field == "2":
                                while True:
                                    try:
                                        pasien["umur"] = int(input("Umur Pasien: "))
                                        break
                                    except ValueError:
                                        print("Error: Mohon masukkan angka untuk umur!")
                            elif field == "3":
                                pasien["gender"] = input("Gender Baru: ")
                            elif field == "4":
                                pasien["diagnosa"] = input("Diagnosa Baru: ")
                            elif field == "5":
                                pasien["status"] = input("Status Baru: ")
                            else:
                                print("Pilihan tidak valid.")

                            print("✅ Data pasien berhasil diupdate.")

                        # TAMPILKAN TABEL TERBARU
                        print("\n📋 DATA PASIEN TERKINI SETELAH UPDATE")
                        tampilkan_tabel(data_pasien, "\n📋 DATA PASIEN TERKINI SETELAH UPDATE")
                        break

                if not ditemukan:
                    print("Data pasien tidak ditemukan.")
                    if konfirmasi_kembali(): break 
            elif pilihan_update == "3":
                break
            else:
                print("Pilihan tidak valid.")

    # ================= Menghapus Data Pasien =================
    elif pilihan_menu == "4":   # DELETE
        while True:
            if len(data_pasien) == 0:
                print("\nData pasien masih kosong.")
                break

            print("\n--- HAPUS DATA PASIEN ---")

            # Tampilkan semua data sebelum hapus
            tampilkan_tabel(data_pasien, "\n--- HAPUS DATA PASIEN ---")
            cari_id = input("\nMasukkan ID pasien yang ingin dihapus (atau ketik 'no' jika cancel): ")

            if cari_id.lower() == "no": break

            pasien = next((p for p in data_pasien if p["id"] == cari_id), None)
            if pasien:
                tampilkan_tabel([pasien], "\nData yang akan dihapus:")
                if konfirmasi_kembali("Yakin ingin menghapus data ini? (y/n): "):
                    data_pasien.remove(pasien)
                    print("\nData pasien berhasil dihapus.")
                    tampilkan_tabel(data_pasien, "\nDATA PASIEN TERKINI")
                    break
            else:
                print("Data tidak ditemukan.")
                if konfirmasi_kembali(): break

    # ================= Keluar Dari Aplikasi =================                   
    elif pilihan_menu == "5":   # EXIT
        if konfirmasi_kembali("\nApa Anda yakin ingin keluar?Pilih (y),Kembali ke menu utama (n): "):
            print("\nTerima kasih telah menggunakan Aplikasi Data Pasien.")
            exit()
