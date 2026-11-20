import storage
from menu import (format_rupiah, jeda, pesan_error, pesan_info,
                tampilkan_tabel_karyawan, tampilkan_tabel_statistik)

def total_gaji(daftar_id):
    "Menjumlahkan gaji semua ID pada daftar_id secara rekursif."

    if len(daftar_id) == 0:
        return 0
    return storage.karyawan[daftar_id[0]]["gaji"] + total_gaji(daftar_id[1:])

def lihat_karyawan():
    try:
        if len(storage.karyawan) == 0:
            raise ValueError("Belum ada data.")
        tampilkan_tabel_karyawan()
    except ValueError as e:
        pesan_error(e)
    else:
        pesan_info(f"Total gaji pokok seluruh karyawan: {format_rupiah(total_gaji(list(storage.karyawan)))}")
    finally:
        jeda()

def cari_karyawan():
    try:
        kata = input("Cari nama/jabatan: ").strip().lower()
        if kata == "":
            raise ValueError("Kata kunci tidak boleh kosong!")
        hasil = []
        for id_k, k in storage.karyawan.items():
            if kata in k["nama"].lower() or kata in k["jabatan"].lower():
                hasil.append(id_k)
        if len(hasil) == 0:
            raise ValueError("Data tidak ditemukan.")
    except ValueError as e:
        pesan_error(e)
    else:
        tampilkan_tabel_karyawan(hasil, f"HASIL PENCARIAN ({len(hasil)} DATA)")
    finally:
        jeda()

def statistik_gaji():
    try:
        if len(storage.karyawan) == 0:
            raise ValueError("Belum ada data.")
        daftar_id = list(storage.karyawan)
        tertinggi = max(daftar_id, key=lambda i: storage.karyawan[i]["gaji"])
        terendah = min(daftar_id, key=lambda i: storage.karyawan[i]["gaji"])
        total = total_gaji(daftar_id)
        baris = [
            ("Jumlah karyawan", f"{len(daftar_id)} orang"),
            ("Total gaji pokok", format_rupiah(total)),
            ("Rata-rata gaji", format_rupiah(total / len(daftar_id))),
            ("Gaji tertinggi", f"{format_rupiah(storage.karyawan[tertinggi]['gaji'])} - {storage.karyawan[tertinggi]['nama']}"),
            ("Gaji terendah", f"{format_rupiah(storage.karyawan[terendah]['gaji'])} - {storage.karyawan[terendah]['nama']}"),
        ]
        per_jabatan = {}
        for k in storage.karyawan.values():
            per_jabatan[k["jabatan"]] = per_jabatan.get(k["jabatan"], 0) + 1
    except ValueError as e:
        pesan_error(e)
    else:
        tampilkan_tabel_statistik(baris, per_jabatan)
    finally:
        jeda()

def lihat_data_sendiri(username):
    """Untuk role user: hanya boleh melihat data karyawan miliknya sendiri."""
    try:
        if storage.users[username].get("id_karyawan") is None:
            raise ValueError("Akun Anda belum terhubung ke data karyawan. Hubungi admin.")
        teks = input("Masukkan ID karyawan Anda: ").strip()
        if not teks.isdecimal():
            raise ValueError("ID harus berupa angka!")
        id_k = int(teks)
        if id_k != storage.users[username]["id_karyawan"]:
            raise ValueError("ID tidak sesuai. Anda hanya dapat melihat data Anda sendiri!")
        if id_k not in storage.karyawan:
            raise ValueError("Data karyawan Anda sudah tidak ada. Hubungi admin.")
    except ValueError as e:
        pesan_error(e)
    else:
        tampilkan_tabel_karyawan([id_k], "DATA SAYA")
    finally:
        jeda()