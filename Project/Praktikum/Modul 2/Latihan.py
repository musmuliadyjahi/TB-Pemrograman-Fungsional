# #Map Function
# def kuadrat(jumlah_perulangan):
#     for x in jumlah_perulangan:
#         print(x*x)
# jumlah_perulangan = range(6)
# kuadrat(jumlah_perulangan) 

kuadrat = lambda x: print(x*x)
jumlah_perulangan = range(6) # 0 s/d 5
list(map(kuadrat, jumlah_perulangan))

alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if(alphabet in vowels):
        return True
    else:
        return False
        
mappedVowels = map(filterVowels, alphabets)
filteredVowels = filter(filterVowels, alphabets)
print('The filtered vowels are:')
print(list(filteredVowels))
print(list(mappedVowels))