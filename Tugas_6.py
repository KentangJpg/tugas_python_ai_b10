import numpy as np
import pandas as pd
np.random.seed(42)

array = np.random.randint(50, 100, size=10)

rata_rata = np.mean(array)
median = np.median(array)
std = np.std(array)
min = np.min(array)
max = np.max(array)


data = {
    "nama": ["Kennedi Yeo", "Styven", "Calvin Tan", "Joven", "Benebel"],
    "npm" : ["2331039" , "2331165", "2331206", "2331126", "2331027"],
    "nilai": array[:5]
}

df = pd.DataFrame(data)

df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")

with open("ringkasan_tugas6.txt", "w") as file:
    file.write("=== RINGKASAN NUMPY ===\n")
    file.write(f"Rata-rata: {rata_rata}\n")
    file.write(f"Median: {median}\n")
    file.write(f"Std Dev: {std}\n")
    file.write(f"Min: {min}\n")
    file.write(f"Max: {max}\n\n")

    file.write("=== RINGKASAN DATAFRAME ===\n")
    file.write(f"Jumlah data: {len(df)}\n")
    file.write(f"LULUS: {(df['status'] == 'LULUS').sum()}\n")
    file.write(f"TIDAK LULUS: {(df['status'] == 'TIDAK LULUS').sum()}\n")


class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return self.df["nilai"].mean()
    
    def pass_rate(self, threshold: float = 70.0) -> float:
        total = len(self.df)
        lulus = (self.df["nilai"] >= threshold).sum()
        return (lulus / total) * 100

    def save_summary(self, path: str):
        with open(path, "a") as file: 
            file.write("\n=== GRADEBOOK ===\n")
            file.write(f"Average: {self.average()}\n")
            file.write(f"Pass rate: {self.pass_rate()}%\n")

    def __str__(self):
        return f"GradeBook: {len(self.df)} data, rata-rata = {self.average():.2f}"

if __name__ == "__main__":
    print("=== NUMPY ===")
    print("Data:", array)
    print("Rata-rata:", rata_rata)
    print("Median:", median)
    print("Std Dev:", std)
    print("Min:", min)
    print("Max:", max)

    print("\n=== PANDAS ===")
    print(df.head())

    print("\n=== OOP: GRADEBOOK ===")
    gb = GradeBook(df)
    print(gb)
    print("Average:", gb.average())
    print("Pass Rate:", gb.pass_rate(), "%")

    gb.save_summary("ringkasan_tugas6.txt")

