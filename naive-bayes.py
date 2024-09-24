# Import library yang dibutuhkan
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

# Data cuaca
data = {
    'Payung': ['Ya', 'Tidak', 'Tidak', 'Ya'],
    'Topi': ['Ya', 'Ya', 'Ya', 'Tidak'],
    'Cuaca': ['Hujan', 'Cerah', 'Cerah', 'Cerah']
}

# Konversi kategori ke dalam bentuk numerik menggunakan LabelEncoder
le_payung = LabelEncoder()
le_topi = LabelEncoder()
le_cuaca = LabelEncoder()

X = list(zip(le_payung.fit_transform(data['Payung']), le_topi.fit_transform(data['Topi'])))
y = le_cuaca.fit_transform(data['Cuaca'])

# Membuat model Gaussian Naive Bayes
model = GaussianNB()

# Melatih model dengan data
model.fit(X, y)

# Input dari pengguna
payung_input = input("Apakah ada payung? (ya/tidak): ").capitalize()
topi_input = input("Apakah ada topi? (ya/tidak): ").capitalize()

# Konversi input pengguna menjadi format numerik
input_data = [[le_payung.transform([payung_input])[0], le_topi.transform([topi_input])[0]]]

# Melakukan prediksi
prediksi = model.predict(input_data)

# Menampilkan hasil prediksi
cuaca_prediksi = le_cuaca.inverse_transform(prediksi)
print(f"Prediksi Cuaca: {cuaca_prediksi[0]}")
