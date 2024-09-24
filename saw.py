import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data alternatif dalam bentuk DataFrame
data = {
    'Laptop': ['Laptop A', 'Laptop B', 'Laptop C'],
    'Harga': [5, 7, 6],
    'Spesifikasi': [8, 9, 7],
    'Berat': [3, 4, 2]
}

df = pd.DataFrame(data)

# Input bobot kriteria dari pengguna
try:
    weight_harga = float(input("Masukkan bobot untuk kriteria Harga (0-1): "))
    weight_spesifikasi = float(input("Masukkan bobot untuk kriteria Spesifikasi (0-1): "))
    weight_berat = float(input("Masukkan bobot untuk kriteria Berat (0-1): "))

    # Pastikan total bobot = 1
    total_weight = weight_harga + weight_spesifikasi + weight_berat
    if total_weight != 1:
        raise ValueError("Total bobot harus berjumlah 1. Saat ini totalnya adalah {:.2f}".format(total_weight))

except ValueError as e:
    print(f"Error: {e}")
    exit()

# Bobot kriteria dalam array numpy
weights = np.array([weight_harga, weight_spesifikasi, weight_berat])

# Fungsi untuk normalisasi data
def normalize(df):
    norm_df = pd.DataFrame()
    for col in df.columns[1:]:
        if col in ['Harga', 'Berat']:
            norm_df[col] = df[col].min() / df[col]  # semakin baik semakin kecil
        else:
            norm_df[col] = df[col] / df[col].max()  # semakin baik semakin besar
    return norm_df

# Hitung skor SAW
def calculate_saw_scores(df, weights):
    norm_df = normalize(df)
    scores = np.dot(norm_df, weights)
    return scores

# Hitung skor
df['Skor'] = calculate_saw_scores(df, weights)

# Menampilkan hasil
print(df)

# Menentukan alternatif terbaik
best_laptop = df.loc[df['Skor'].idxmax()]
print(f"\nAlternatif terbaik: {best_laptop['Laptop']} dengan skor {best_laptop['Skor']:.3f}")

# Visualisasi skor menggunakan grafik batang
plt.figure(figsize=(8, 5))
plt.bar(df['Laptop'], df['Skor'], color=['blue', 'green', 'orange'])
plt.title('Perbandingan Skor Laptop')
plt.xlabel('Alternatif Laptop')
plt.ylabel('Skor')
plt.ylim(0, 1)  # Mengatur batas y untuk visualisasi
plt.axhline(y=best_laptop['Skor'], color='r', linestyle='--', label='Skor Terbaik')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
