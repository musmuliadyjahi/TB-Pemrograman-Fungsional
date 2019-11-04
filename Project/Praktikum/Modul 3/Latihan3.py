Akmal = {
    "nama": "Akmal Dzaky Hafidhuddin",
    "nim": "201710370311223",
    "Kelas": "Pemrograman Fungsional"
}
Agus = {
    "nama": "Agus Hendryawan",
    "nim": "201710370311221",
    "Kelas": "Pemrograman Fungsional"
}
Dika = {
    "nama": "Dika Surya",
    "nim": "201710370311220",
    "Kelas": "Pemrograman Fungsional"
}
All = {
    0: Akmal,
    1: Agus,
    2: Dika
}

print("0. Akmal", "1. Akmal", "2. Dika")
x = int(input("masukkan angka : "))
if x in All.keys():
    print(All[x])
else:
    print("gagal")
