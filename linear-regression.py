import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Data
data = {
    'Jam_Studi': [2, 3, 4, 5, 6, 7, 8, 9, 10, 5],
    'Skor_Ujian': [65, 70, 75, 80, 85, 90, 95, 100, 105, 82]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Langkah 2: Analisis Regresi
X = df[['Jam_Studi']]  # Predictor
y = df['Skor_Ujian']    # Response

# Membuat model regresi
model = LinearRegression()
model.fit(X, y)

# Koefisien regresi
b = model.coef_[0]
a = model.intercept_

# Input dari pengguna untuk prediksi
try:
    jam_studi_input = float(input("Masukkan jumlah jam studi: "))
    prediksi_skor = model.predict(pd.DataFrame([[jam_studi_input]], columns=['Jam_Studi']))  # Menggunakan DataFrame
    print(f"Prediksi skor ujian untuk {jam_studi_input} jam studi adalah: {prediksi_skor[0]:.2f}")

except ValueError:
    print("Input tidak valid. Silakan masukkan angka.")
    exit()

# Menghitung prediksi untuk seluruh data untuk grafik
y_pred = model.predict(X)

# Membuat grafik
plt.figure(figsize=(10, 6))
plt.scatter(df['Jam_Studi'], df['Skor_Ujian'], color='blue', label='Data Siswa')
plt.plot(df['Jam_Studi'], y_pred, color='red', linewidth=2, label='Garis Regresi')
plt.scatter(jam_studi_input, prediksi_skor, color='green', label='Prediksi', s=100, edgecolor='black')  # Titik prediksi
plt.title('Hubungan antara Jam Studi dan Skor Ujian Matematika')
plt.xlabel('Jumlah Jam Studi')
plt.ylabel('Skor Ujian Matematika')
plt.legend()
plt.grid(True)
plt.show()
