# Install library jika belum terpasang
# install.packages("e1071")

# Load library
library(e1071)

# Membuat data frame dari tabel data
data <- data.frame(
  Iklan = c("ya", "tidak", "ya", "tidak"),
  Harga = c("rendah", "tinggi", "sedang", "rendah"),
  Kesuksesan = c("berhasil", "tidak berhasil", "berhasil", "tidak berhasil")
)

# Membangun model Naive Bayes
classifier <- naiveBayes(Kesuksesan ~ Iklan + Harga, data)

# Menampilkan informasi model
print(classifier)

# Data testing untuk prediksi
data_testing <- data.frame(
  Iklan = c("ya"),
  Harga = c("rendah")
)

# Melakukan prediksi
prediksi <- predict(classifier, data_testing, type = "raw")

# Menampilkan hasil prediksi
print(prediksi)

# Mencetak probabilitas dari setiap kelas
probabilitas <- attr(prediksi, "prob")
print(probabilitas)
