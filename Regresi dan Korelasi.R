# Generate random data
set.seed(123)
variabel_X <- runif(30, 1, 10)
variabel_Y <- 50 + 10 * variabel_X + rnorm(30, 0, 3)

# Membuat dataframe dari data
data <- data.frame(variabel_X, variabel_Y)

# Analisis Regresi
regression_model <- lm(variabel_Y ~ variabel_X, data = data)

# Menghitung koefisien korelasi Pearson
correlation_coefficient <- cor(data$variabel_X, data$variabel_Y)

# Plot data dan garis regresi
plot(data$variabel_X, data$variabel_Y, main = "Regresi dan Korelasi", xlab = "Variabel X", ylab = "Variabel Y")
abline(regression_model, col = "red")

# Menampilkan hasil korelasi
print(paste("Koefisien Korelasi Pearson:", correlation_coefficient))

# Menampilkan hasil regresi
summary(regression_model)
