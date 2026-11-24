import os

from colorama import Fore, init
from prettytable import PrettyTable

import storage

init(autoreset=True)

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

def jeda():
    input(Fore.CYAN + "Tekan Enter untuk lanjut...")

def format_rupiah(angka):
    return "Rp " + f"{round(angka):,}".replace(",", ".")

def pesan_sukses(teks):
    print(Fore.GREEN + str(teks))

def pesan_error(teks):
    print(Fore.RED + str(teks))

def pesan_info(teks):
    print(Fore.YELLOW + str(teks))

def cetak_tabel(tabel):
    """Mencetak tabel PrettyTable dengan warna cyan."""
    print(Fore.CYAN + tabel.get_string())

def tampilkan_menu(judul, daftar_menu):
    """Menampilkan menu dalam bentuk tabel. daftar_menu berisi pasangan (nomor, nama)."""
    tabel = PrettyTable()
    tabel.title = judul
    tabel.field_names = ["No", "Menu"]
    tabel.align["Menu"] = "l"
    for nomor, nama in daftar_menu:
        tabel.add_row([nomor, nama])
    cetak_tabel(tabel)

def tampilkan_tabel_karyawan(daftar_id=None, judul="DATA KARYAWAN"):
    """Menampilkan karyawan dalam tabel. daftar_id berisi ID yang ditampilkan (None = semua)."""
    if daftar_id is None:
        daftar_id = list(storage.karyawan)
    tabel = PrettyTable()
    tabel.title = judul
    tabel.field_names = ["ID", "Nama", "Jabatan", "Gaji Pokok",
                        "Jam Lembur", "Bonus Lembur", "Gaji Bersih"]
    tabel.align["Nama"] = "l"
    tabel.align["Jabatan"] = "l"
    for kolom in ["Gaji Pokok", "Jam Lembur", "Bonus Lembur", "Gaji Bersih"]:
        tabel.align[kolom] = "r"
    for id_k in daftar_id:
        k = storage.karyawan[id_k]
        jam = storage.total_jam_lembur(id_k)
        bonus = storage.total_bonus_lembur(id_k)
        tabel.add_row([id_k, k["nama"], k["jabatan"], format_rupiah(k["gaji"]),
                    f"{jam:g} jam", format_rupiah(bonus),
                    format_rupiah(k["gaji"] + bonus)])
    cetak_tabel(tabel)

def tampilkan_daftar_singkat():
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama"]
    tabel.align["Nama"] = "l"
    for id_k, k in storage.karyawan.items():
        tabel.add_row([id_k, k["nama"]])
    cetak_tabel(tabel)

def tampilkan_tabel_statistik(baris):
    """Menampilkan statistik gaji. baris berisi pasangan (keterangan, nilai)."""
    tabel = PrettyTable()
    tabel.title = "LAPORAN GAJI KARYAWAN"
    tabel.field_names = ["Keterangan", "Nilai"]
    tabel.align["Keterangan"] = "l"
    tabel.align["Nilai"] = "r"
    for keterangan, nilai in baris:
        tabel.add_row([keterangan, nilai])
    cetak_tabel(tabel)

def tampilkan_tabel_per_jabatan(per_jabatan):
    """Menampilkan jumlah karyawan per jabatan. per_jabatan adalah dictionary {jabatan: jumlah}."""
    tabel = PrettyTable()
    tabel.title = "KARYAWAN PER JABATAN"
    tabel.field_names = ["Jabatan", "Jumlah"]
    tabel.align["Jabatan"] = "l"
    for jabatan, jumlah in per_jabatan.items():
        tabel.add_row([jabatan, f"{jumlah} orang"])
    cetak_tabel(tabel)

def baca_id_berulang():
    """Meminta ID karyawan terus-menerus sampai benar.
    Kosongkan (Enter) untuk membatalkan, fungsi mengembalikan None."""
    pesan_info("Tekan Enter untuk ke menu utama")
    while True:
        try:
            teks = input("ID karyawan: ").strip()
            if teks == "":
                return None
            if not teks.isdecimal():
                raise ValueError("ID harus berupa angka!")
            id_k = int(teks)
            if id_k not in storage.karyawan:
                raise KeyError(id_k)
        except KeyError:
            pesan_error("ID tidak ditemukan! Silakan masukkan ID yang benar.")
        except ValueError as e:
            pesan_error(f"{e} Silakan masukkan ID yang benar.")
        else:
            return id_k