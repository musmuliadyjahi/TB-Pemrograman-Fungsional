import random
import asd
from functools import reduce
arr = [10, 7, 6, 4, 5, 2, 3, 8, 1, 9]  # membuat list

# functools
def func(acc, x): #proses penukaran list
    if not acc:
        return [x]
    if acc[-1] < x:
        return acc+[x]
    else:
        return acc[:-1]+[x]+acc[-1:]

def my_sort(x):
    sorted = reduce(func, x, [])
    print(sorted)
    if x == sorted:
        return sorted
    else:
        return my_sort(sorted)

print('arr:', arr)
arr_sorted = my_sort(arr)
print('arr sorted:', arr_sorted)

# procedural
def bubbleSort3(arr):
    n = len(arr)  # mengetahui panjang list
    for i in range(n):  # membuat perulangan sesuai panjang list
        for j in range(0, n-i-1):  # membuat perulangan dari 0 hingga n-i-1
            # menukar angka jika yang kiri lebih besar dari yang kanan
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubbleSort3(arr)  # memanggil fungsi
print(arr)
# https://www.geeksforgeeks.org/bubble-sort/

# Imperative
Imp = []  # membuat list untuk menyimpan hasil fungsi dan di panggil
for x in range(len(arr)-1, 0, -1):  # membuat perulangan sesuai panjang list
    for i in range(x):  # membuat perulangan sesi ke-2 hingga akhir sesuai panjang list
        # menukar angka jika yang kiri lebih besar dari yang kanan
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
Imp.extend(arr)  # menyatukan hasil list dengan list yang di buat
print(Imp)
# https://www.yudana.id/contoh-penerapan-algoritma-sorting-dengan-menggunakan-python/

# OOP Program
def main():
    data = []
    for i in range(0, 10):
        data.append(random.randint(1, 10))
    asd.bubblesort(data)

main()
# http://www.codedrome.com/bubble-sort-in-python/
