print("=========== DATA OLAHRAGA ===========")
data = ["Basket", 5, "Sepak Bola", 11, "Voli", 6, "Boxing", 2]
first = data[0]
last = data[-1]
specific = data[0:8:2]

print("Data lengkap:", data)
print("Data pertama:", first)
print("Data terakhir:", last)
print("Data jenis olahraga:", specific)


print("\n=========== MANIPULASI DATA ===========")
print("Sebelum:", data)

data.append("Renang")
data.insert(8, 1)
data.extend(["Badminton", 2])
data.pop(6)
data.remove(2)

print("Sesudah:", data)


print("\n=========== TUPLE ===========")
data_tuple = ("harimau", "singa", "gajah", "badak", "kuda", "monyet")

print("Panjang:", len(data_tuple))
print("Index 0:", data_tuple[0])
print("Index 2:", data_tuple[2])
print("Terakhir:", data_tuple[-1])

a, b, *rest = data_tuple
print("a:", a)
print("b:", b)
print("rest:", rest)


print("\n=========== SET ===========")
set1 = {1, 1, 2, 3, 4, 4, 5, 6}
set2 = {1, 2, 3, 7, 8, 4, 5, 6}

print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set2 - set1)
print("Symmetric Difference:", set2 ^ set1)


print("\n=========== DICTIONARY ===========")
data_mhs = {
    "nama": "Kennedi Yeo",
    "NPM": "2331039",
    "angkatan": "2023",
    "kota": "Batam"
}

print("Data:", data_mhs)

data_mhs["jurusan"] = "Sistem Informasi"
print("Tambah:", data_mhs)

data_mhs["kota"] = "Tanjung Pinang"
print("Update:", data_mhs)

del data_mhs["angkatan"]
print("Hapus:", data_mhs)

print("Keys:", list(data_mhs.keys()))
print("Values:", list(data_mhs.values()))
print("Items:", list(data_mhs.items()))

print("\nIterasi:")
for key, value in data_mhs.items():
    print(key + ":", value)


print("\n=========== NESTED STRUCTURE ===========")
buku = [
    {"judul": "Laskar Pelangi", "penulis": "Andrea Hirata", "tahun": 2005},
    {"judul": "Bumi", "penulis": "Tere Liye", "tahun": 2014},
    {"judul": "Negeri 5 Menara", "penulis": "Ahmad Fuadi", "tahun": 2009},
    {"judul": "Dilan 1990", "penulis": "Pidi Baiq", "tahun": 2014}
]

print("Judul buku:")
for item in buku:
    print("-", item["judul"])

tahun = 2010
filter = [item for item in buku if item["tahun"] >= tahun]

print("Buku >= 2010:")
for item in filter:
    print("-", item["judul"], "-", item["tahun"])


print("\n=========== COMPREHENSION ===========")
angka = list(range(1, 21))

genap = [x for x in angka if x % 2 == 0]
kuadrat = [x**2 for x in angka]

print("Angka:", angka)
print("Genap:", genap)
print("Kuadrat:", kuadrat)


mapping = {x: "genap" if x % 2 == 0 else "ganjil" for x in range(1, 11)}

print("Mapping:")
print(mapping)


kalimat = "Halo Kakak Mentor!"
huruf_unik = {char.lower() for char in kalimat if char.isalpha()}

print("Huruf unik:", huruf_unik)


print("\n=========== KEANGGOTAAN & PENCARIAN ===========")

buah = ["apel", "jeruk", "mangga", "pisang", "anggur", "melon", "semangka"]
angka_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print("apel ada:", "apel" in buah)
print("mangga ada:", "mangga" in buah)
print("5 ada di set:", 5 in angka_set)
print("11 ada di set:", 11 in angka_set)

if "pisang" in buah:
    print("pisang di index:", buah.index("pisang"))
else:
    print("pisang tidak ditemukan")

item = "anggur"
print(item, "di index:", buah.index(item) if item in buah else "tidak ditemukan")
