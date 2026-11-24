import storage
from menu import (baca_id_berulang, format_rupiah, jeda, pesan_error, pesan_info,
                pesan_sukses, tampilkan_tabel_karyawan)

def tambah_lembur():
    tampilkan_tabel_karyawan()
    id_k = baca_id_berulang()
    if id_k is None:
        return
    try:
        jam = storage.validasi_jam(input("Jam lembur: ").strip())
    except ValueError as e:
        pesan_error(e)
    else:
        storage.lembur.setdefault(id_k, []).append(jam)
        bonus = storage.hitung_bonus_lembur(jam)
        pesan_sukses(f"Lembur {jam:g} jam untuk {storage.karyawan[id_k]['nama']} dicatat.")
        pesan_info(f"Bonus lembur ini: {format_rupiah(bonus)}")
    finally:
        jeda()