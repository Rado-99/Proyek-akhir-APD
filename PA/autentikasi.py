import pwinput

import storage
from menu import jeda, pesan_error, pesan_sukses

MAKS_PERCOBAAN = 3

def cek_login(username, password):
    return username in storage.users and storage.users[username]["password"] == password

def login():
    """Login dengan maksimal 3 kali percobaan.
    Jika username salah, hanya username yang diulang.
    Jika password salah, hanya password yang diulang."""
    percobaan = 0
    username = None
    while percobaan < MAKS_PERCOBAAN:
        try:
            if username is None:
                username = input("Username: ").strip()
                if username not in storage.users:
                    username = None
                    raise ValueError("Username tidak ditemukan!")
            password = pwinput.pwinput("Password:").strip()
            if not cek_login(username, password):
                raise ValueError("Password salah!")
        except ValueError as e:
            percobaan += 1
            sisa = MAKS_PERCOBAAN - percobaan
            if sisa > 0:
                pesan_error(f"{e} Sisa percobaan: {sisa}")
            else:
                pesan_error(e)
        else:
            pesan_sukses(f"Login berhasil. Selamat datang, {username}!")
            jeda()
            return username
    pesan_error(f"Gagal login {MAKS_PERCOBAAN} kali. Kembali ke menu awal.")
    jeda()
    return None

def register():
    try:
        username = input("Username baru: ").strip()
        password = pwinput.pwinput("Password baru:").strip()
        id_teks = input("ID karyawan Anda: ").strip()
        if username == "" or password == "":
            raise ValueError("Username dan password tidak boleh kosong!")
        if username in storage.users:
            raise ValueError("Username sudah dipakai!")
        if not id_teks.isdecimal():
            raise ValueError("ID karyawan harus berupa angka!")
        id_k = int(id_teks)
        if id_k not in storage.karyawan:
            raise ValueError("ID karyawan tidak ditemukan!")
        if storage.id_sudah_dipakai(id_k):
            raise ValueError("ID karyawan sudah terhubung dengan akun lain!")
    except ValueError as e:
        pesan_error(e)
    else:
        storage.users[username] = {"password": password, "role": "user", "id_karyawan": id_k}
        pesan_sukses("Register berhasil, silakan login.")
    finally:
        jeda()