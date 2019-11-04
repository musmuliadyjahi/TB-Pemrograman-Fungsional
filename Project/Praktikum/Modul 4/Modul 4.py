# def angkaI(list):
#     for i in range(2, 6):
#         arr = []
#         for j in range(1, len(list)+1):
#             temp = j**i
#             arr.append(temp)
#         print(arr)


# Angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# angkaI(Angka)
# -------------------------------------------------------------------------------------------------------
def cube(x, y):
    return y**x


def my_map(method, argument_list):
    print("Angka = ", argument_list)
    for x in range(2, 6):
        arr = []
        for y in argument_list:
            arr.append(method(x, y))
        print("Hasil Pangkat", x, "=", arr)
    return arr


my_list = my_map(cube, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

my_list

# ==========================================================================================================
buku = [
    {'judul': 'anoboy', 'harga': 1, 'pengarang': 'wahyu'},
    {'judul': 'naruto', 'harga': 2, 'pengarang': 'william'},
    {'judul': 'Big Hero', 'harga': 3, 'pengarang': 'angel'},
]
arr = [
    {'kutipan': 'Gratis itu baik'}, 
    {'kutipan': 'Bar-bar adalah jalan ninjaku'}, 
    {'kutipan': 'Saya saja bisa menjadi hero, kenapa kamu tidak'},
]


def kutipan(arr, substring):
    arr = arr

    def cetak():
        print(arr['kutipan'])

    return cetak


def cari(buku, substring):
    return buku['judul'] in substring['judul']\
        and buku['harga'] in substring['harga']\
        and buku['pengarang'] in substring['pengarang']


def tampil(key, value):
    if value == True:
        print(key)


print("Nomor 2")
asd = input("Masukkan judul buku : ")
substring = {'judul': asd, 'harga': list(
    range(1, 5)), 'pengarang': 'wahyu, william, angel'}
x = list(map(cari, buku, [substring]*len(buku)))
list(map(tampil, buku, x))
