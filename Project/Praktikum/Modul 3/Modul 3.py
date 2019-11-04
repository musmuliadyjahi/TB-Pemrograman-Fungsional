# Nomor 1
All = {
    'Akmal': {
        "nama": "Akmal Dzaky Hafidhuddin",
        "nim": "201710370311223",
        "Kelas": "Pemrograman Fungsional"
    },
    'Agus': {
        "nama": "Agus Hendryawan",
        "nim": "201710370311221",
        "Kelas": "Pemrograman Fungsional"
    },
    'Dika': {
        "nama": "Dika Surya",
        "nim": "201710370311220",
        "Kelas": "Pemrograman Fungsional"
    }
}


def ca(x):
    if x in All.keys():
        print(All[x])
    else:
        print("Nama salah")


print("Nomor 1 \n 1. Akmal", "2. Agus", "3. Dika")
print(ca(input("masukkan nama : ")))


# Nomor 2
buku = [
    {'judul': 'anoboy', 'harga': 410000, 'pengarang': 'wahyu'},
    {'judul': 'naruto', 'harga': 350000, 'pengarang': 'william'},
    {'judul': 'Big Hero', 'harga': 380000, 'pengarang': 'angel'},
]

def cari(buku, subsring):
    return buku['judul'] in substring['judul']\
        and buku['harga'] in substring['harga']\
        and buku['pengarang'] in substring['pengarang']

def tampil(key, value):
    if value == True:
        print(key, value)


print("Nomor 2")
asd = input("Masukkan judul buku : ")
dsa = input("Masukkan pengarang : ")
substring = {'judul': asd, 'harga': list(
    range(200000, 500000)), 'pengarang': dsa}
x = list(map(cari, buku, [substring]*len(buku)))
list(map(tampil, buku, x))

# Nomor 3
Pegawai = {
    'Akmal': {
        "nama": "Akmal Dzaky Hafidhuddin",
        "nim": "201710370311223",
        "Kelas": "Pemrograman Fungsional"
    },
    'Agus': {
        "nama": "Agus Hendryawan",
        "nim": "201710370311221",
        "Kelas": "Pemrograman Fungsional"
    },
    'Dika': {
        "nama": "Dika Surya",
        "nim": "201710370311220",
        "Kelas": "Pemrograman Fungsional"
    }
}

print("Nomor 3 \n Perintah : \n 1. Tampilkan \n 2. Tambah Data \n 3. Ubah Data")
A = int(input("Masukkan nomor pilihan : "))
if A == 1:
    print("1. Akmal", "2. Agus", "3. Dika")
    x = input("masukkan nama : ")
    if x in Pegawai.keys():
        print(Pegawai[x])
    else:
        print("Nama salah")
elif A == 2:
    print("List : \n 1. Akmal \n 2. Agus \n 3. Dika")
    nama = input("Masukkan nama yang akan di tambah datanya : ")
    baru = input("Masukkan nama kategori data : ")
    isi = input("Masukkan isi dari data : ")
    Pegawai[nama][baru] = isi
    print(Pegawai[nama])
elif A == 3:
    print("List : \n 1. Akmal \n 2. Agus \n 3. Dika")
    nama = input("Masukkan nama yang akan di ubah isi datanya : ")
    kategori = input("masukkan kategori yang akan di ubah isi datanya : ")
    baru = input("Masukkan isi data baru : ")
    Pegawai[nama][kategori] = baru
    print(Pegawai[nama])
