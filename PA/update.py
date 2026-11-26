import storage
from menu import (baca_id_berulang, jeda, pesan_error, pesan_info, pesan_sukses,
                tampilkan_menu, tampilkan_tabel_karyawan)

def baca_nama_baru():
    """Meminta nama baru sampai hanya berisi huruf (spasi boleh).
    Kosongkan (Enter) jika tidak diubah, fungsi mengembalikan None."""
    while True:
        try:
            nama = input("Nama baru    : ").strip()
            if nama == "":
                return None
            if not nama.replace(" ", "").isalpha():
                raise ValueError("Nama hanya boleh berisi huruf!")
        except ValueError as e:
            pesan_error(f"{e} Silakan masukkan nama yang benar.")
        else:
            return nama

def baca_jabatan_baru():
    """Menampilkan pilihan jabatan lalu meminta pilihan sampai benar.
    Kosongkan (Enter) jika tidak diubah, fungsi mengembalikan None."""
    tampilkan_menu("PILIHAN JABATAN", list(storage.DAFTAR_JABATAN.items()))
    batas = len(storage.DAFTAR_JABATAN)
    while True:
        try:
            pilih = input(f"Jabatan baru (1-{batas}): ").strip()
            if pilih == "":
                return None
            if pilih not in storage.DAFTAR_JABATAN:
                raise ValueError("Pilihan jabatan tidak valid!")
        except ValueError as e:
            pesan_error(f"{e} Silakan pilih angka 1-{batas}.")
        else:
            return storage.DAFTAR_JABATAN[pilih]

def baca_gaji_baru():
    """Meminta gaji baru sampai valid.
    Kosongkan (Enter) jika tidak diubah, fungsi mengembalikan None."""
    while True:
        try:
            gaji_teks = input("Gaji baru    : ").strip()
            if gaji_teks == "":
                return None
            gaji = storage.validasi_gaji(gaji_teks)
        except ValueError as e:
            pesan_error(f"{e} Silakan masukkan gaji yang benar.")
        else:
            return gaji

def ubah_karyawan():
    tampilkan_tabel_karyawan()
    id_ubah = baca_id_berulang()
    if id_ubah is None:
        return

    pesan_info("Kosongkan (Enter) jika tidak diubah.")
    nama = baca_nama_baru()
    jabatan = baca_jabatan_baru()
    gaji_baru = baca_gaji_baru()

    if nama is None and jabatan is None and gaji_baru is None:
        pesan_info("Tidak ada data yang diubah.")
    else:
        if nama is not None:
            storage.karyawan[id_ubah]["nama"] = nama
        if jabatan is not None:
            storage.karyawan[id_ubah]["jabatan"] = jabatan
        if gaji_baru is not None:
            storage.karyawan[id_ubah]["gaji"] = gaji_baru
        pesan_sukses("Data berhasil diubah.")
    jeda()