# lambda, filter, map, first class object
# high order function, function as return value, closure, docorator
import functools

Arr = [1, 2, 3, 4, 5, 6, 7, 8]
A = list(map(lambda x: x+x, Arr))  # map, lambda

def jumlah():
    Lis = []
    for i in range(0, len(Arr)):
        jml = Arr[i]*2
        Lis.append(jml)
    print("Hasil Kali : ", Lis) #Decorator
    
    five = 5    #Closure
    def add(arg):
        return arg + five
    return add

def filters(x):
    num = [1, 2, 3, 4, 5]
    if(x in num):
        return True
    else:
        return False

print("Map dan Lambda : ")
print(A)

filtered = filter(filters, Arr)  # filter
print("Filter Arr terhadap num: ")
for num in filtered:
    print(num)

yell = filters  # first class object Function sebagai object
print("First Class Function : ")
print(yell(6))

def reverse_numeric(x, y):  # high order function
    return y - x    # function as return value

print("Reverse Sort : ", sorted([5, 2, 4, 1, 3],
                                key=functools.cmp_to_key(reverse_numeric)))

def Dec(x): #Decorator
    def one():
        jumlah()
    return one

use = Dec(jumlah)
use()

if __name__=='__name__': #Closure
    closure1 = jumlah()
    print(closure1(10))