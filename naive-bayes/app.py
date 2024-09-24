from flask import Flask, render_template, request
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    payung_input = request.form['payung'].capitalize()  # Ambil input dari form
    topi_input = request.form['topi'].capitalize()      # Ambil input dari form
    
    # Konversi input pengguna menjadi format numerik
    input_data = [[le_payung.transform([payung_input])[0], le_topi.transform([topi_input])[0]]]
    
    # Melakukan prediksi
    prediksi = model.predict(input_data)
    
    # Menampilkan hasil prediksi dalam bentuk cuaca asli (Hujan/Cerah)
    cuaca_prediksi = le_cuaca.inverse_transform(prediksi)[0]
    
    return render_template('index.html', prediksi=f"Prediksi Cuaca: {cuaca_prediksi}")

if __name__ == '__main__':
    app.run(debug=True)
