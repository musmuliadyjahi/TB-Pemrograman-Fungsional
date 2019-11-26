#Memanggil extension matplotlib dan string, string digunakan untuk membuat alfabet
import matplotlib.pyplot as plt
import string

#Menyiapkan variabel
alpha = string.ascii_uppercase #Isi variabel adalah alfabet dari extension string
y = [83, 95, 91, 87, 70, 0, 85, 82, 200, 67, 73, 77, 0] #membuat list sesuai dengan modul
Yrange = [10,20,30,40,50,60,70,80,90,100] #membuat range pada sumbu-Y sebesar 10
label = y #isi list sama dengan y, untuk dijadikan label
x = [] #list kosong untuk isi alfabet

#perulangan untuk memasukkan alfabet sesuai dengan jumlah anggota y
for i in range(len(y)):
    x.append(alpha[i])
#perulangan untuk memberikan label nilai diatas box
for label, x_count, y_count in zip(label, x, y):
    plt.annotate(label, xy=(x_count, y_count), xytext=(5, -5), textcoords='offset points')

#memasukan nilai ke extension matplotlib
plt.bar(x, y) #memasukan sumbu x dan y
plt.yticks(Yrange) #mengubah nilai default sumbu y
plt.title("Nomor 1") #nama tabel
plt.xlabel("Anggota") #nama sumbu X
plt.ylabel("Range") #nama sumbu y
plt.show() #menampilkan tabel