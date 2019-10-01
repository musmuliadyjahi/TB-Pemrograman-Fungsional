# Nomor 1
def isprimer(x):
    a = True
    if x >= 2:
        for i in range (2,x):
            if x % i == 0:
                a = False
    else :
        a = False
    return  a

nm = int(input("1.  Masukkan angka : "))
print   (nm, "bilangan primer? ", isprimer(nm))

# Nomor 2
def fx(angka): #Percobaan 1
    gx = []
    for n in angka:
        fx = 2*n + 5
        gx.append(fx + 1)
    return gx
fxIn = int(input("2.    Masukkan NIM : "))
print   ("NIM setelah dimasukkan kedalam fungsi : ", fx([fxIn]))

def gx(x): #Percobaan 2
    def fx(x):
        a = 2*x + 5
        return a
    a = fx(x) + 1
    return a

In = int(input("Masukkan NIM : "))
print("Nilai Nim = ", gx(In))