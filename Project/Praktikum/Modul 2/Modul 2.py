# Nomor 1
print("Nomor 1 : ")
my_list = [1, 2, 3]
i = 0
ln = len(my_list)
new_list = list(map(lambda x: x * x, my_list))
while i < ln:
    print("Hasil Kuadrat dari", my_list[i], "adalah", new_list[i])
    i = i+1

# Nomor 2
print()
print("Nomor 2 : ")
ListA = ['teknik', 'pemograman', 'muhammadiyah', 'malang']
ListB = ['informatika', 'fungsional', 'malang', '2019']

print("tupples")  # tuples
print('{' + "'"+ListA[0]+ListB[0]+"'"+','+"'"+ListA[1]+ListB[1] +
      "'"+','+"'"+ListA[2]+ListB[2]+"'"+','+"'"+ListA[3]+ListB[3]+'}')

print("")
print("cupitalize Directory")  # cupitalize Directory
print('{' + "'" + ListA[0].capitalize() + ListB[0].capitalize() + "'"+','+"'"+ListA[1].capitalize() + ListB[1].capitalize() +
      "'"+','+"'"+ListA[2].capitalize() + ListB[2].capitalize() + "'"+','+"'"+ListA[3].capitalize() + ListB[3].capitalize() + '}')

print("")
print("Uppercase Dictionary")  # Uppercase Dictionary
print('{' + "'"+ListA[0].upper() + ListB[0].upper() + "'"+','+"'"+ListA[1].upper() + ListB[1].upper() +
      "'"+','+"'"+ListA[2].upper() + ListB[2].upper() + "'"+','+"'"+ListA[3].upper() + ListB[3].upper() + '}')

print("")
print("tupples info Dictionary")  # tuppel info Dictionary


def Convert(tupp, dic):
    dic = dict(tupp)
    return dic


tups = [(ListA[0], ListB[0]), (ListA[1], ListB[1]),
        (ListA[2], ListB[2]), (ListA[3], ListB[3]), ]
dictionary = {}
print(Convert(tups, dictionary))

# Nomor 3
print()
print("Nomor 3 : ")


def asd(x):
    for i in range(1, x+1):
        q = i**2
        w = i**3
        e = i**4
        my_tuple = (q, w, e)
        su = q+w+e
        print(i, " = ", my_tuple, " = ", su)


nm = int(input("Masukkan angka : "))
asd(nm)

# Nomor 4
print()
print("Nomor 4 : ")


def dup(A):
    arr = []
    for i in range(len(A)):
        arr.append([])
        for j in range(len(A)):
            Matrix = A[i][j]*A[i][j]
            arr[i].append(Matrix)
    return arr


A = [[1, 2], [3, 4]]
print("A = ", A)
print("B = ", dup(A))
