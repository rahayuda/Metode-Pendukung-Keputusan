# Data
jumlah_jam_studi <- c(2, 3, 4, 5, 6, 7, 8, 9, 10, 5)
skor_ujian_matematika <- c(65, 70, 75, 80, 85, 90, 95, 100, 105, 82)

# Menghitung koefisien korelasi Pearson
correlation_coefficient <- cor(jumlah_jam_studi, skor_ujian_matematika)

# Analisis Regresi
regression_model <- lm(skor_ujian_matematika ~ jumlah_jam_studi)

# Menampilkan hasil korelasi
print(paste("Koefisien Korelasi Pearson:", correlation_coefficient))

# Menampilkan hasil regresi
summary(regression_model)

# Plot data dan garis regresi
plot(jumlah_jam_studi, skor_ujian_matematika, main = "Regresi dan Korelasi", xlab = "Jumlah Jam Studi", ylab = "Skor Ujian Matematika")
abline(regression_model, col = "red")
