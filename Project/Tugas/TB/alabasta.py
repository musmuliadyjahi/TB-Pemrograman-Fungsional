import random
import time
import sys


def setup():  # set profile hero
    global name, HP, MP

    name = ("luffy")
    HP = 1000
    MP = 1000


def enemy3():
    global enemyHP
    global enemyMP
    global enemyname3
    enemyHP = 750
    enemyMP = 1000

    enemyname3 = "Crocodile"
    print(enemyname3 + "nya punya " + " " +
          str(enemyHP) + " " + "Total HP")
    print(enemyname3 + "nya punya " + " " +
          str(enemyMP) + " " + "Total MP")
    print("\n" + enemyname3 + " mempunyai Skill:")
    print(" 1. Bomb = 50 Kerusakan\n 2. Laser = 75 Kerusakan \n 3. Thunder = 100 Kerusakan")


# mulai
setup()
global name, HP, MP, enemyHP, enemyMP
print("\nTotal HP" + " " + str(HP))
print("Total MP" + " " + str(MP))
enemy3()

while enemyHP > 0:
    A = random.randint(1,5)
    print("Musuh memilih Skill", A)
#   enemy attack
    if A == 2:
        enemyhitskill1 = 50
        enemyhitskill1mp = 50
        print("Giliran Musuhnya Menyerang Dengan Skill Bomb " +
              str(enemyhitskill1) + " Kerusakan ")
        HP = HP - enemyhitskill1
        enemyMP = enemyMP - enemyhitskill1mp
    elif A == 3:
        enemyhitskill2 = 75
        enemyhitskill2mp = 75
        print("Giliran Musuhnya Menyerang Dengan Skill Laser " +
              str(enemyhitskill2) + " Kerusakan ")
        HP = HP - enemyhitskill2
        enemyMP = enemyMP - enemyhitskill2mp
    elif A == 4:
        enemyhitskill3 = 100
        enemyhitskill3mp = 100
        print("Giliran Musuhnya Menyerang Dengan Skill Thunder " +
              str(enemyhitskill3) + " Kerusakan ")
        HP = HP - enemyhitskill3
        enemyMP = enemyMP - enemyhitskill3mp
    else:
        enemyhit = 3
        enemyhitmp = 3
        HP = HP - enemyhit
        enemyMP = enemyMP + enemyhitmp
        print("Giliran Musuhnya Menyerang Biasa " +
              str(enemyhit) + " Kerusakan ")
#   hero attack
    print("Sisa Nyawa " + name + " " + str(HP)+"HP")
    time.sleep(5)
    Hits = random.randint(1, 4)
    if HP <= 0:
        print("\nKamu Mati silahkan kembali dengan kekuatan yang lebih kuat "+name+" Mati")
        time.sleep(5)
        print("Game Over")
        time.sleep(5)
        sys.exit(0)
    else:
        if Hits == 1:
            hit = 80
            print(name + " Menyerang Mengakibatkan " + str(hit) + " Kerusakan")
            enemyHP = enemyHP - hit
            if enemyHP < 0:
                enemyHP -= enemyHP
            print("Sisa HP  Crocodile = " + str(enemyHP) +
                  " Dan MP  Crocodile " + str(enemyMP))
            time.sleep(5)
        if Hits == 2:
            hit = 90
            print(name + " Menyerang Mengakibatkan " + str(hit) + " Kerusakan")
            enemyHP = enemyHP - hit
            if enemyHP < 0:
                enemyHP -= enemyHP
            print("Sisa HP  Crocodile = " + str(enemyHP) +
                  " Dan MP  Crocodile " + str(enemyMP))
            time.sleep(5)
        if Hits == 3:
            hit = 100
            print(name + " Menyerang Mengakibatkan " + str(hit) + " Kerusakan")
            enemyHP = enemyHP - hit
            if enemyHP < 0:
                enemyHP -= enemyHP
            print("Sisa HP  Crocodile = " + str(enemyHP) +
                  " Dan MP  Crocodile " + str(enemyMP))
            time.sleep(5)
        if Hits == 1:
            hit = 200
            print(name + " Menyerang Mengakibatkan " + str(hit) + " Kerusakan")
            enemyHP = enemyHP - hit
            if enemyHP < 0:
                enemyHP -= enemyHP
            print("Sisa HP  Crocodile = " + str(enemyHP) +
                  " Dan MP  Crocodile " + str(enemyMP))
            time.sleep(5)
else:
    time.sleep(5)
    print("\nWah " + enemyname3 + " Hidup kembali, kamu harus melawannya lagi")
    time.sleep(5)

# round 2
print("\nTotal HP kamu saat ini" + " " + str(HP))
print("Total MP kamu saat ini" + " " + str(MP))
print("\n")
enemy3()

while enemyHP > 0:
    A = random.randint(1,5)
    print("Musuh memilih Skill", A)
    if A == 2:
        enemyhitskill1 = 50
        enemyhitskill1mp = 50
        print("Giliran Musuhnya Menyerang Dengan Skill Bomb " +
              str(enemyhitskill1) + " Kerusakan ")
        HP = HP - enemyhitskill1
        enemyMP = enemyMP - enemyhitskill1mp
    elif A == 3:
        enemyhitskill2 = 75
        enemyhitskill2mp = 75
        print("Giliran Musuhnya Menyerang Dengan Skill Laser " +
              str(enemyhitskill2) + " Kerusakan ")
        HP = HP - enemyhitskill2
        enemyMP = enemyMP - enemyhitskill2mp
    elif A == 4:
        enemyhitskill3 = 100
        enemyhitskill3mp = 100
        print("Giliran Musuhnya Menyerang Dengan Skill Thunder " +
              str(enemyhitskill3) + " Kerusakan ")
        HP = HP - enemyhitskill3
        enemyMP = enemyMP - enemyhitskill3mp
    else:
        enemyhit = 3
        enemyhitmp = 3
        HP = HP - enemyhit
        enemyMP = enemyMP + enemyhitmp
        print("Giliran Musuhnya Menyerang Biasa " +
              str(enemyhit) + " Kerusakan ")

    print("Sisa Nyawa " + name + " " + str(HP)+"HP")
    time.sleep(5)
    Hits = random.randint(1, 4)
    if HP <= 0:
        print("\nKamu Mati silahkan kembali dengan kekuatan yang lebih kuat "+name+" Mati")
        time.sleep(5)
        print("Game Over")
        time.sleep(5)
        sys.exit(0)
    else:
        if Hits == 1:
            hit = 80
            print(name + " Menyerang Mengakibatkan " + str(hit) + " Kerusakan")
            enemyHP = enemyHP - hit
            if enemyHP < 0:
                enemyHP -= enemyHP
            print("Sisa HP  Crocodile = " + str(enemyHP) +
                  " Dan MP  Crocodile " + str(enemyMP))
            time.sleep(5)
        if Hits == 2:
            hit = 90
            print(name + " Menyerang Mengakibatkan " + str(hit) + " Kerusakan")
            enemyHP = enemyHP - hit
            if enemyHP < 0:
                enemyHP -= enemyHP
            print("Sisa HP  Crocodile = " + str(enemyHP) +
                  " Dan MP  Crocodile " + str(enemyMP))
            time.sleep(5)
        if Hits == 3:
            hit = 100
            print(name + " Menyerang Mengakibatkan " + str(hit) + " Kerusakan")
            enemyHP = enemyHP - hit
            if enemyHP < 0:
                enemyHP -= enemyHP
            print("Sisa HP  Crocodile = " + str(enemyHP) +
                  " Dan MP  Crocodile " + str(enemyMP))
            time.sleep(5)
        if Hits == 1:
            hit = 200
            print(name + " Menyerang Mengakibatkan " + str(hit) + " Kerusakan")
            enemyHP = enemyHP - hit
            if enemyHP < 0:
                enemyHP -= enemyHP
            print("Sisa HP  Crocodile = " + str(enemyHP) +
                  " Dan MP  Crocodile " + str(enemyMP))
            time.sleep(5)
else:
    print("Wah " + enemyname3 + " sudah mati, silakan melanjutkan perjalanan")
