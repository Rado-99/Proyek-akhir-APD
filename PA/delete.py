import storage
from menu import baca_id_berulang, jeda, pesan_info, pesan_sukses, tampilkan_daftar_singkat

def hapus_karyawan():
    tampilkan_daftar_singkat()
    id_hapus = baca_id_berulang()
    if id_hapus is None:
        return

    nama = storage.karyawan[id_hapus]["nama"]
    del storage.karyawan[id_hapus]
    storage.lembur.pop(id_hapus, None)
    akun_dihapus = [u for u, data in storage.users.items()
                    if data.get("id_karyawan") == id_hapus]
    for username in akun_dihapus:
        del storage.users[username]
    pesan_sukses(f"Data {nama} berhasil dihapus.")
    for username in akun_dihapus:
        pesan_info(f"Akun '{username}' yang terhubung ikut dihapus.")
    jeda()