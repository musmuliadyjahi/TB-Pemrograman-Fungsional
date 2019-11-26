#Memanggil extension matplotlib dan string, string digunakan untuk membuat alfabet
import matplotlib.pyplot as plt
import string

#Menyiapkan variabel
alpha = string.ascii_lowercase #Isi variabel adalah alfabet dari extension string
y = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0] #nilai asli
#membuat list kosong untuk di isi dengan alfabet dan hasil perhitungan nilai sumbu Y
x, y1, y2 = [], [], []

#membuat perulangan sesuai dengan anggota y
for i in range(len(y)):
    y1.append(y[i]*1.5) #membuat anggota y1 = 1.5y
    y2.append(y[i]*-1) #membuat anggota y1 = -1y
    x.append(alpha[i]) #manggabungkan alfabet ke list x

plt.scatter(x, y, s=100,  marker='^') #plot 1 dengan model titik segitiga
plt.scatter(x, y1, s=150, marker='1') #plot 2 dengan model titik 'tiga garis'
plt.scatter(x, y2, s=200, marker='s') #plot 3 dengan model titik segi-5
plt.show() #menampilkan tabel