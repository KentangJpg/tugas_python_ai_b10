def greet(nama):
    return f"Halo, {nama}!"


def tambah(a: float, b: float = 0.0) -> float:
    return a + b


def rata_rata(angka):
    if len(angka) == 0:
        return 0.0
    return round(sum(angka) / len(angka), 2)


class Student:
    def __init__(self, nama, NPM):
        self.nama = nama
        self.NPM = NPM
        self.nilai = []

    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    def rata_nilai(self):
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0):
        if self.rata_nilai() >= threshold:
            return "Lulus"
        else:
            return "Tidak Lulus"

    def __str__(self) -> str:
        return f"Student(nama='{self.nama}', nim='{self.NPM}', rata={self.rata_nilai()}, status={self.status()})"


if __name__ == "__main__":
    print("=== FUNCTIONS ===")
    print(greet("Kennedi Yeo"))
    print(tambah(5, 7))
    print(tambah(10))
    print(rata_rata([80, 90, 100]))
    print(rata_rata([]))

    print("\n=== CLASS STUDENT ===")
    student1 = Student("Kennedi Yeo", "2331039")
    student1.tambah_nilai(85)
    student1.tambah_nilai(90)
    student1.tambah_nilai(78)

    student2 = Student("Selina V Sim", "2341108")
    student2.tambah_nilai(80)
    student2.tambah_nilai(85)
    student2.tambah_nilai(90)

    print(student1)
    print(student2)

    print("\nDetail Student 1")
    print("Rata-rata:", student1.rata_nilai())
    print("Status:", student1.status())

    print("\nDetail Student 2")
    print("Rata-rata:", student2.rata_nilai())
    print("Status:", student2.status())
