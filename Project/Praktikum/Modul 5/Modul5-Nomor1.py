#Memanggil extension matplotlib dan string, string digunakan untuk membuat alfabet
import matplotlib.pyplot as plt
import string

alpha = string.ascii_lowercase #membuat variabel string yang isinya alfabet dari extension string
y = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0] #membuat list sesuai dengan
Yrange = [10,20,30,40,50,60,70,80,90,100] #membuat range pada sumbu-Y sebesar 10
label = y #membuat list yang isinya sama dengan y untuk dijadikan label 
x = [] #membuat list kosong untuk isi alfabet

for i in range(len(y)):
    x.append(alpha[i])

for label, x_count, y_count in zip(label, x, y):
    plt.annotate(label, xy=(x_count, y_count),
                 xytext=(5, -5), textcoords='offset points')

plt.bar(x, y)
plt.yticks(Yrange)
plt.title("Nomor 1")
plt.xlabel("Anggota")
plt.ylabel("Range")
plt.show()
