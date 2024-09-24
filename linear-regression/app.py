import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression  # Pastikan untuk menambahkan ini

app = Flask(__name__)

# Data
data = {
    'Jam_Studi': [2, 3, 4, 5, 6, 7, 8, 9, 10, 5],
    'Skor_Ujian': [65, 70, 75, 80, 85, 90, 95, 100, 105, 82]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Membuat model regresi
X = df[['Jam_Studi']]
y = df['Skor_Ujian']
model = LinearRegression()
model.fit(X, y)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediksi_skor = None
    jam_studi_input = None
    plot_url = None

    if request.method == 'POST':
        try:
            jam_studi_input = float(request.form['jam_studi'])
            prediksi_skor = model.predict(pd.DataFrame([[jam_studi_input]], columns=['Jam_Studi']))[0]

            # Membuat grafik
            y_pred = model.predict(X)
            plt.figure(figsize=(10, 6))
            plt.scatter(df['Jam_Studi'], df['Skor_Ujian'], color='blue', label='Data Siswa')
            plt.plot(df['Jam_Studi'], y_pred, color='red', linewidth=2, label='Garis Regresi')
            plt.scatter(jam_studi_input, prediksi_skor, color='green', s=100, edgecolor='black', label='Prediksi')
            plt.title('Hubungan antara Jam Studi dan Skor Ujian Matematika')
            plt.xlabel('Jumlah Jam Studi')
            plt.ylabel('Skor Ujian Matematika')
            plt.legend()
            plt.grid(True)

            # Simpan grafik ke dalam memori dan konversi ke format base64
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            plot_url = base64.b64encode(buf.getvalue()).decode('utf8')
            plt.close()

        except ValueError:
            prediksi_skor = "Input tidak valid. Silakan masukkan angka."

    return render_template('index.html', prediksi_skor=prediksi_skor, jam_studi_input=jam_studi_input, plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
