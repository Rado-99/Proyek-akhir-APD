import storage
from menu import jeda, pesan_error, pesan_info, pesan_sukses, tampilkan_menu

def baca_nama():
    """Meminta nama terus-menerus sampai hanya berisi huruf (spasi boleh).
    Kosongkan (Enter) untuk membatalkan, fungsi mengembalikan None."""
    while True:
        try:
            nama = input("Nama    : ").strip()
            if nama == "":
                return None
            if not nama.replace(" ", "").isalpha():
                raise ValueError("Nama hanya boleh berisi huruf!")
        except ValueError as e:
            pesan_error(f"{e} Silakan masukkan nama yang benar.")
        else:
            return nama

def baca_jabatan():
    """Menampilkan pilihan jabatan lalu meminta pilihan terus-menerus sampai benar.
    Kosongkan (Enter) untuk membatalkan, fungsi mengembalikan None."""
    tampilkan_menu("PILIHAN JABATAN", list(storage.DAFTAR_JABATAN.items()))
    while True:
        try:
            pilih = input("Pilih jabatan (1-4): ").strip()
            if pilih == "":
                return None
            if pilih not in storage.DAFTAR_JABATAN:
                raise ValueError("Pilihan jabatan tidak valid!")
        except ValueError as e:
            pesan_error(f"{e} Silakan pilih angka 1-4.")
        else:
            return storage.DAFTAR_JABATAN[pilih]

def baca_gaji():
    """Meminta gaji terus-menerus sampai valid.
    Kosongkan (Enter) untuk membatalkan, fungsi mengembalikan None."""
    while True:
        try:
            gaji_teks = input("Gaji    : ").strip()
            if gaji_teks == "":
                return None
            gaji = storage.validasi_gaji(gaji_teks)
        except ValueError as e:
            pesan_error(f"{e} Silakan masukkan gaji yang benar.")
        else:
            return gaji

def tambah_karyawan():
    pesan_info("Tekan Enter pada isian kosong untuk kembali ke menu utama")
    nama = baca_nama()
    if nama is None:
        return
    jabatan = baca_jabatan()
    if jabatan is None:
        return
    gaji = baca_gaji()
    if gaji is None:
        return
    storage.karyawan[storage.buat_id_baru()] = {"nama": nama, "jabatan": jabatan, "gaji": gaji}
    pesan_sukses(f"Data berhasil ditambahkan dengan jabatan {jabatan}.")
    jeda()