# Load library
library(matlib)

# Matriks perbandingan kriteria
CR <- matrix(c(1, 4, 2,
               1/4, 1, 1/3,
               1/2, 3, 1), nrow = 3, byrow = TRUE)

# Matriks perbandingan alternatif terhadap kriteria
CAC <- matrix(c(5, 4, 3,
                1, 1, 2,
                1/3, 1/2, 1), nrow = 3, byrow = TRUE)

# Menghitung eigenvalue dan eigenvector matriks CR
eig_CR <- eigen(CR)
eigenvector_CR <- eig_CR$vectors[, 1]

# Menghitung eigenvector untuk setiap kriteria pada CAC
eig_CAC <- eigen(CAC)
eigenvector_H <- eig_CAC$vectors[, 1]
eigenvector_M <- eig_CAC$vectors[, 2]
eigenvector_K <- eig_CAC$vectors[, 3]

# Menghitung prioritas akhir untuk setiap kriteria
prioritas_H <- eigenvector_CR[1] * eigenvector_H
prioritas_M <- eigenvector_CR[1] * eigenvector_M
prioritas_K <- eigenvector_CR[1] * eigenvector_K

# Matriks perbandingan alternatif terhadap kriteria
CAC_alternatif <- matrix(c(5, 4, 3,
                           1, 1, 2,
                           1/3, 1/2, 1), nrow = 3, byrow = TRUE)

# Menghitung skor total untuk setiap alternatif
skor_total_E <- sum(prioritas_H[1] * CAC_alternatif[1, 1],
                    prioritas_M[1] * CAC_alternatif[1, 2],
                    prioritas_K[1] * CAC_alternatif[1, 3])

skor_total_S <- sum(prioritas_H[1] * CAC_alternatif[2, 1],
                    prioritas_M[1] * CAC_alternatif[2, 2],
                    prioritas_K[1] * CAC_alternatif[2, 3])

skor_total_C <- sum(prioritas_H[1] * CAC_alternatif[3, 1],
                    prioritas_M[1] * CAC_alternatif[3, 2],
                    prioritas_K[1] * CAC_alternatif[3, 3])

# Menampilkan skor total
print("Skor Total untuk Alternatif Elizabeth:")
print(Re(skor_total_E))
print("Skor Total untuk Alternatif Sophie Martin:")
print(Re(skor_total_S))
print("Skor Total untuk Alternatif Charles & Keith:")
print(Re(skor_total_C))

