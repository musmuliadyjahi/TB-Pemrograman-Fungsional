import random
import playsound
playsound.playsound('D:/Python/Project/Tugas/TB/KDA.mp3', True)

def a():
    global hp  # deklarasi global 2
    hp -= 10  # pengurangan nilai 3
    localHP = hp  # deklarasi local 4
    print(localHP)
    return hp  # return nilai global 5


global hp  # deklarasi 1
hp = 100  # deklarasi 1
a()
a()