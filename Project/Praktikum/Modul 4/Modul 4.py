def angkaI(list):
    for i in range(2,6):
        arr = []
        for j in range(1,len(list)+1):
            temp = j**i
            arr.append(temp)
        print(arr)

Angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
angkaI(Angka)