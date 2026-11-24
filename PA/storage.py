BONUS_JAM_PERTAMA = 100000
BONUS_JAM_KEDUA = 200000

DAFTAR_JABATAN = {"1": "Manager", "2": "HRD", "3": "Karyawan", "4": "Cleaning Service"}

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "rado": {"password": "rado123", "role": "user", "id_karyawan": 3},
}

karyawan = {
    1: {"nama": "Andi Pratama", "jabatan": "Manager", "gaji": 12000000},
    2: {"nama": "Ahmad Rizki", "jabatan": "Staff", "gaji": 6000000},
    3: {"nama": "Rudi", "jabatan": "Programmer", "gaji": 8000000},
}

lembur = {}

def buat_id_baru():
    """Mengembalikan ID baru untuk karyawan."""
    if len(karyawan) == 0:
        return 1
    return max(karyawan) + 1

def validasi_gaji(teks):
    """Memvalidasi input gaji, mengembalikan gaji dalam bentuk int."""
    if not teks.isdecimal():
        raise ValueError("Gaji harus berupa angka bulat!")
    gaji = int(teks)
    if gaji <= 0:
        raise ValueError("Gaji harus lebih dari 0!")
    return gaji

def validasi_jam(teks):
    """Memvalidasi jam lembur, mengembalikan jam dalam bentuk float."""
    try:
        jam = float(teks)
    except ValueError:
        raise ValueError("Jam lembur harus berupa angka!")
    if not 0 < jam <= 12:
        raise ValueError("Jam lembur harus lebih dari 0 dan maksimal 12 jam!")
    return jam

def id_sudah_dipakai(id_k):
    """Mengembalikan True jika ID karyawan sudah terhubung dengan salah satu akun."""
    for data in users.values():
        if data.get("id_karyawan") == id_k:
            return True
    return False

def baca_id():
    """Meminta ID dari user, memvalidasi, lalu mengembalikan ID (int)."""
    teks = input("ID karyawan: ").strip()
    if not teks.isdecimal():
        raise ValueError("ID harus berupa angka!")
    id_k = int(teks)
    if id_k not in karyawan:
        raise KeyError(id_k)
    return id_k

def hitung_bonus_lembur(jam):
    """Jam pertama Rp100.000, jam kedua dan seterusnya Rp200.000 per jam."""
    if jam <= 1:
        return round(jam * BONUS_JAM_PERTAMA)
    return round(BONUS_JAM_PERTAMA + (jam - 1) * BONUS_JAM_KEDUA)

def total_jam_lembur(id_k):
    """Menjumlahkan semua jam lembur milik satu karyawan."""
    return sum(lembur.get(id_k, []))

def total_bonus_lembur(id_k):
    """Menjumlahkan bonus dari semua catatan lembur milik satu karyawan."""
    total = 0
    for jam in lembur.get(id_k, []):
        total += hitung_bonus_lembur(jam)
    return total