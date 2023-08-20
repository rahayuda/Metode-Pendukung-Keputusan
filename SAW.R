# Matriks kriteria dan alternatif
kriteria <- c("Harga", "Spesifikasi", "Berat")
alternatif <- c("Laptop A", "Laptop B", "Laptop C")

# Nilai kriteria untuk setiap alternatif
nilai <- matrix(c(5, 8, 3,
                  7, 9, 4,
                  6, 7, 2), ncol = 3, byrow = TRUE)

# Normalisasi nilai kriteria
min_max_norm <- function(x) {
  return((x - min(x)) / (max(x) - min(x)))
}

nilai_norm <- apply(nilai, 2, min_max_norm)

# Bobot kriteria
bobot <- c(0.4, 0.3, 0.3)

# Menghitung skor alternatif
skor_alternatif <- colSums(nilai_norm * bobot)

# Menampilkan hasil
hasil <- data.frame(Alternatif = alternatif, Skor = skor_alternatif)
hasil <- hasil[order(hasil$Skor, decreasing = TRUE), ]
print(hasil)

