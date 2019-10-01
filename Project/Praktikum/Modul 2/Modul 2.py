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
ListA = ['teknik', 'pemograman', 'muhammadiyah', 'Tahun']
ListB = ['informatika', 'fungsional', 'malang', '2019']
ListC = []
MatrixA = []
MatrixB = []
MatrixC = []

for i in range(len(ListA)):
    ListC = ListA[i]+ListB[i]
    MatrixA.append(ListC)
    MatrixC.append(ListC.upper())

for i in range(len(ListA)):
    ListC = ListA[i].capitalize()+ListB[i].capitalize()
    MatrixB.append(ListC)

print(MatrixA)
print(MatrixB)
print(MatrixC)

def Convert(tupp, dic):
    dic = dict(tupp)
    return dic

tups = [(ListA[0], ListB[0]), (ListA[1], ListB[1]),
        (ListA[2], ListB[2]), (ListA[3], ListB[3])]
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
