# Aplikasi Daftar Nilai Siswa
# Kelas X SMK

# Dictionary untuk menyimpan data siswa
data_siswa = {}

def tambah_siswa():
    nama = input("Masukkan nama siswa: ")
    if nama in data_siswa:
        print("⚠️ Siswa sudah ada!")
    else:
        nilai = int(input("Masukkan nilai: "))
        data_siswa[nama] = nilai
        print(f"✅ Data {nama} berhasil ditambahkan.")

def lihat_siswa():
    if not data_siswa:
        print("📭 Belum ada data siswa.")
    else:
        print("\n=== Daftar Nilai Siswa ===")
        for nama, nilai in data_siswa.items():
            print(f"- {nama}: {nilai}")

def ubah_nilai():
    nama = input("Masukkan nama siswa yang ingin diubah: ")
    if nama in data_siswa:
        nilai_baru = int(input("Masukkan nilai baru: "))
        data_siswa[nama] = nilai_baru
        print(f"🔄 Nilai {nama} berhasil diubah.")
    else:
        print("❌ Siswa tidak ditemukan.")

def hapus_siswa():
    nama = input("Masukkan nama siswa yang ingin dihapus: ")
    if nama in data_siswa:
        del data_siswa[nama]
        print(f"🗑️ Data {nama} berhasil dihapus.")
    else:
        print("❌ Siswa tidak ditemukan.")

# Menu utama
while True:
    print("\n=== Aplikasi Daftar Nilai Siswa ===")
    print("1. Tambah Siswa")
    print("2. Lihat Daftar Nilai")
    print("3. Ubah Nilai Siswa")
    print("4. Hapus Siswa")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah_siswa()
    elif pilihan == "2":
        lihat_siswa()
    elif pilihan == "3":
        ubah_nilai()
    elif pilihan == "4":
        hapus_siswa()
    elif pilihan == "5":
        print("👋 Terima kasih, aplikasi ditutup.")
        break
    else:
        print("⚠️ Pilihan tidak valid, coba lagi!")
