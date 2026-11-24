import storage
from autentikasi import login, register, ubah_password
from create import tambah_karyawan
from delete import hapus_karyawan
from lembur import tambah_lembur
from menu import bersihkan_layar, jeda, pesan_error, tampilkan_menu
from read import cari_karyawan, lihat_data_sendiri, lihat_karyawan, statistik_gaji
from update import ubah_karyawan

user_aktif = None
jalan = True

def proses_menu_awal():
    global user_aktif, jalan
    bersihkan_layar()
    tampilkan_menu("SISTEM DATA KARYAWAN", [("1", "Login"), ("2", "Register"), ("0", "Keluar")])
    pilih = input("Pilih: ").strip()

    if pilih == "1":
        user_aktif = login()
    elif pilih == "2":
        register()
    elif pilih == "0":
        jalan = False
    else:
        pesan_error("Pilihan tidak valid!")
        jeda()

def proses_menu_utama():
    global user_aktif
    bersihkan_layar()
    role = storage.users[user_aktif]["role"]
    if role == "admin":
        daftar_menu = [("1", "Tambah Karyawan"), ("2", "Lihat Karyawan"),
                    ("3", "Ubah Karyawan"), ("4", "Hapus Karyawan"),
                    ("5", "Cari Karyawan"), ("6", "Laporan Gaji Karyawan"),
                    ("7", "Catat Lembur"), ("0", "Logout")]
    else:
        daftar_menu = [("1", "Lihat Data Saya"), ("2", "Ubah Password"), ("0", "Logout")]
    tampilkan_menu(f"MENU ({user_aktif} - {role})", daftar_menu)
    pilih = input("Pilih: ").strip()

    nomor_valid = [nomor for nomor, nama in daftar_menu if nomor != "0"]

    if pilih == "0":
        user_aktif = None
    elif pilih in nomor_valid:
        bersihkan_layar()
        if role == "user":
            if pilih == "1":
                lihat_data_sendiri(user_aktif)
            elif pilih == "2":
                ubah_password(user_aktif)
        elif pilih == "1":
            tambah_karyawan()
        elif pilih == "2":
            lihat_karyawan()
        elif pilih == "3":
            ubah_karyawan()
        elif pilih == "4":
            hapus_karyawan()
        elif pilih == "5":
            cari_karyawan()
        elif pilih == "6":
            statistik_gaji()
        elif pilih == "7":
            tambah_lembur()
    else:
        pesan_error("Pilihan tidak valid!")
        jeda()

if __name__ == "__main__":
    while jalan:
        if user_aktif is None:
            proses_menu_awal()
        else:
            proses_menu_utama()

    bersihkan_layar()
    print("Terima kasih!")