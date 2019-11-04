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
def cube(x,y):
    return y**x

def my_map(method, argument_list):
    print("Angka = ", argument_list)
    for x in range(2,6):
        arr = []
        for y in argument_list:
            arr.append(method(x,y))
        print("Hasil Pangkat",x, "=",arr)
    return arr
my_list = my_map(cube, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

my_list