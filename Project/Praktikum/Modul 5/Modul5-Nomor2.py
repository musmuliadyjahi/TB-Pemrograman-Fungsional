#Memanggil extension matplotlib dan string, string digunakan untuk membuat alfabet
import matplotlib.pyplot as plt
import string

#Menyiapkan variabel
alpha = string.ascii_lowercase #Isi variabel adalah alfabet dari extension string
y = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0] #nilai asli
#membuat list kosong untuk di isi dengan alfabet dan hasil perhitungan nilai sumbu Y
x, y1, y2, y3 = [], [], [], [] 

#membuat perulangan sesuai dengan anggota y
for i in range(len(y)):
    y1.append(y[i]*1.5) #membuat anggota y1 = 1.5y
    y2.append(y[i]*-1) #membuat anggota y1 = -1y
    y3.append(y[i]*-1.5) #membuat anggota y1 = -1.5y
    x.append(alpha[i]) #manggabungkan alfabet ke list x

plt.plot(x, y, linestyle='-.') #plot 1 dengan style -.
plt.plot(x, y1, linestyle=':') #plot 2 dengan style :
plt.plot(x, y2, linestyle='--') #plot 3 dengan style --
plt.plot(x, y3, linestyle='-') #plot 4 dengan style garis
plt.grid(True) #membuat garis pada kotak
plt.show() #menampilkan tabel