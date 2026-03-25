Nama = "Kennedi Yeo"
Umur = 20
tinggi = 160.4
Student = True
nama_buah = ["Apel", "Jeruk", "Pisang", "Mangga", "Strawberry"]

# ===================== DATA DIRI =====================
print("=== DATA DIRI ===")
print(f"Nama        : {Nama}")
print(f"Umur        : {Umur}")
print(f"Tinggi      : {tinggi} cm")
print(f"Student     : {Student}") 

# ===================== OPERASI STRING & MATH =====================
JumlahHuruf = len(Nama)
UpperCaseNama = Nama.upper()

print("\n=== INFORMASI TAMBAHAN ===")
print(f"Nama (Upper)        : {UpperCaseNama}")
print(f"Jumlah Huruf        : {JumlahHuruf}")
print(f"Umur + 5 tahun      : {Umur + 5}")
print(f"Tinggi (meter)      : {tinggi / 100} m")
print(f"Umur x Tinggi       : {Umur * tinggi}")
print(f"Tinggi // 10        : {tinggi // 10}")
print(f"Tinggi % 3          : {tinggi % 3}")

# ===================== LIST BUAH =====================
print("\n=== LIST BUAH (AWAL) ===")
print(nama_buah)

nama_buah.append("Anggur")
print("\nSetelah tambah (append 'Anggur'):")
print(nama_buah)

nama_buah.remove("Pisang")
print("\nSetelah hapus (remove 'Pisang'):")
print(nama_buah)

print("\n=== DAFTAR BUAH (PER ITEM) ===")
for buah in nama_buah:
    print(f"- {buah}")

# ===================== INPUT USER =====================
print("\n=== INPUT USER ===")
nama_user = input("Masukkan nama: ")
umur_user = int(input("Masukkan umur: "))

print(f"\nHalo, nama saya {nama_user} dan umur saya {umur_user} tahun.")
