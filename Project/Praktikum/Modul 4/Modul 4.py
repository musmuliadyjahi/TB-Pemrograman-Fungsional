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

print("Nomor 1")

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
    {'judul': 'anoboy', 'harga': 1, 'pengarang': 'wahyu',
        'kutipan': 'Gratis itu baik'},
    {'judul': 'naruto', 'harga': 2, 'pengarang': 'william',
        'kutipan': 'Bar-bar adalah jalan ninjaku'},
    {'judul': 'Big Hero', 'harga': 3, 'pengarang': 'angel',
        'kutipan': 'Saya saja bisa menjadi hero, kenapa kamu tidak'},
]

def kutipan(buku, judul):
    Buku = buku
    Judul = judul

    def cetak():
        for x in range(len(buku)):
            if Buku[x]['judul'] == Judul:
                asd = Buku[x]['kutipan']
                print("Kutipan :", asd)
    return cetak

def cari(buku, substring):
    return buku['judul'] in substring['judul']\
        and buku['harga'] in substring['harga']\
        and buku['pengarang'] in substring['pengarang']\
        and buku['kutipan'] in substring['kutipan']

def tampil(key, value):
    if value == True:
        print("Judul buku :", key['judul'])

print("Nomor 2")
asd = input("Masukkan judul buku : ")
substring = {'judul': asd, 'harga': list(
    range(1, 5)), 'pengarang': 'wahyu, william, angel', 'kutipan': 'Gratis itu baik, Bar-bar adalah jalan ninjaku, Saya saja bisa menjadi hero, kenapa kamu tidak'}
x = list(map(cari, buku, [substring]*len(buku)))
list(map(tampil, buku, x))
ss = kutipan(buku, substring['judul'])
ss()