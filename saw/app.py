from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Data alternatif dalam bentuk DataFrame
data = {
    'Laptop': ['Laptop A', 'Laptop B', 'Laptop C'],
    'Harga': [5, 7, 6],
    'Spesifikasi': [8, 9, 7],
    'Berat': [3, 4, 2]
}

df = pd.DataFrame(data)

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    try:
        # Ambil bobot dari input form
        weight_harga = float(request.form['weight_harga'])
        weight_spesifikasi = float(request.form['weight_spesifikasi'])
        weight_berat = float(request.form['weight_berat'])

        # Pastikan total bobot = 1
        total_weight = weight_harga + weight_spesifikasi + weight_berat
        if total_weight != 1:
            raise ValueError("Total bobot harus berjumlah 1.")

        # Bobot kriteria dalam array numpy
        weights = np.array([weight_harga, weight_spesifikasi, weight_berat])

        # Hitung skor
        df['Skor'] = calculate_saw_scores(df, weights)

        # Format skor dengan 2 angka di belakang koma
        df['Skor'] = df['Skor'].round(2)

        # Menentukan alternatif terbaik
        best_laptop = df.loc[df['Skor'].idxmax()]

        # Buat grafik
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(df['Laptop'], df['Skor'], color=['blue', 'green', 'orange'])
        ax.set_title('Perbandingan Skor Laptop')
        ax.set_xlabel('Alternatif Laptop')
        ax.set_ylabel('Skor')
        ax.set_ylim(0, 1)
        ax.axhline(y=best_laptop['Skor'], color='r', linestyle='--', label='Skor Terbaik')
        ax.legend()
        ax.grid(axis='y', linestyle='--', alpha=0.7)

        # Simpan grafik ke dalam buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plot_url = base64.b64encode(buf.getvalue()).decode()

        return render_template('result.html', table=df.to_html(), best_laptop=best_laptop['Laptop'], best_score=round(best_laptop['Skor'], 2), plot_url=plot_url)

    except ValueError as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True)
