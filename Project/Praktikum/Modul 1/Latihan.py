#Latiham Modul
def multiply_by_3(angka):
    angka_baru = [] 
    for n in angka:
        angka_baru.append(n * 3)
    return angka_baru
original_numbers = [1, 3, 5, 10] 
changed_numbers = multiply_by_3(original_numbers)

print(original_numbers)
print(changed_numbers) 

def tambah(increment):
    def tambah_increment(angka):
        angka_baru = [] 
        for n in angka:
            angka_baru.append(n + increment)
        return angka_baru
    return tambah_increment 

tambahs = tambah(5)
print(tambahs([8, 13])) 
