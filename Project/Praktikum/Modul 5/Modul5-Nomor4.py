import matplotlib.pyplot as plt  # Memanggil extension matplotlib

# membuat koordinat dari segitiga
x = [0, 1, 3]
y = [0, 2, 3]
dx = [1, 2, -3]
dy = [2, 1, -3]

# membuat segitiga
for i in range(len(x)-1):
    plt.arrow(x[i], y[i], dx[i], dy[i], color='r', head_width=0.1,
              head_length=0.2, length_includes_head=True)  # membuat garis dengan kepala panah

# Membuat koordinat dan garis tanpa panah
plt.arrow(x[2], y[2], dx[2], dy[2], color='b')
# Menambahkan title
plt.title("Chart Garis")
# mengubah limit sumbu x dan y
plt.ylim(-0.5, 3.5)
plt.xlim(-1, 4)
# memberi nama sumbu x dan y
plt.xlabel("Sumbu x")
plt.ylabel("Sumbu y")
# menampilkan tabel
plt.show()
