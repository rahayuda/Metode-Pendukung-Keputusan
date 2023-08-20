data <- data.frame(payung=c("ya", "tidak", "tidak", "tidak"),
                   cuaca=c("hujan", "cerah", "cerah", "cerah"))

View(data)

library(e1071)

classifier <- naiveBayes(cuaca~payung, data)

classifier

data_testing <- data.frame(payung=c("ya"))

prediksi <- predict(classifier, data_testing, type="raw")

prediksi

data2 <- data.frame(payung=c("ya", "tidak", "tidak", "ya"),
                    topi=c("ya", "ya", "ya", "tidak"),
                    cuaca=c("hujan", "cerah", "cerah", "cerah"))

View(data2) 

classifier2 <- naiveBayes(cuaca~payung+topi, data2)

classifier2 

data_testing2 <- data.frame(payung=c("ya"),
                            topi=c("ya"))

prediksi2 <- predict(classifier2, data_testing2, type = "raw")

prediksi2
