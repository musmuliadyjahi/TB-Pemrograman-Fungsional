# 1
def tambah(x, y):
    return x+y


print(tambah(2, 4))

lainnya = tambah
print(lainnya(5, 5))
# 2


def potong(kata):
    return kata[10:17]


def menyapa(kata):
    return kata.replace("Hallo", "Hei")


def eksekusi(func):
    greeting = func("Hallo dunia dan Hallo praktikum Informatika")
    print(greeting)


eksekusi(potong)
eksekusi(menyapa)
# 3


def angkaI(a):
    def angkaII(b):
        return a*b

    return angkaII


dikali = angkaI(12)
print(dikali(2))
# 4
List = ['aa', 'bb', 35, dikali]
List.append(dikali(2))
print(List)
# 5
# def aFunction(text):
#     text = text

#     def bFunction():
#         print(text)

#     bFunction()
# aFunction('contoh Nested Function')
# 6


def aFunction(text):
    Text = text

    def bFunction():
        print(Text)

    return bFunction


myFunction = aFunction('Contoh Closure')
myFunction()
