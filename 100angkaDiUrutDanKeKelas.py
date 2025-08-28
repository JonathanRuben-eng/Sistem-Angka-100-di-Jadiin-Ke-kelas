# 1) Data angka 10x10 (100 angka)
data = [
    [77, 76, 83, 41, 45, 60, 32, 91, 99, 65],
    [57, 67, 88, 65, 70, 35, 39, 60, 85, 86],
    [73, 77, 91, 61, 81, 73, 63, 61, 93, 65],
    [42, 48, 70, 75, 65, 67, 52, 54, 50, 75],
    [44, 44, 50, 53, 63, 45, 75, 60, 81, 83],
    [86, 90, 60, 73, 74, 55, 57, 87, 52, 50],
    [32, 39, 40, 43, 56, 70, 75, 77, 79, 30],
    [33, 30, 34, 47, 80, 72, 43, 78, 53, 60],
    [42, 43, 45, 47, 82, 93, 95, 60, 63, 65],
    [67, 68, 96, 87, 40, 44, 43, 32, 31, 60]
]

# 2) Flatten jadi 1 list
numbers = [num for row in data for num in row]

# 3) Definisikan kelas (interval 10-an)
classes = [(i, i+9) for i in range(30, 100, 10)]

# 4) Buat dictionary untuk simpan frekuensi
freq_table = {}

for low, high in classes:
    # Ambil angka yang masuk interval
    group = [x for x in numbers if low <= x <= high]
    # Simpan dalam dict (label kelas: daftar angka)
    freq_table[f"{low}-{high}"] = group

# 5) Cetak hasil
print("Kelas\tFrekuensi\tAngka")
for kelas, group in freq_table.items():
    print(f"{kelas}\t{len(group)}\t\t{group}")

# Urutkan data
sorted_data = sorted(data)

# Cetak hasil
print("Data setelah diurutkan:")
print(sorted_data)