import random, time, sys


def setup(): #set profile hero
    global name, HP, MP

    name = ("luffy")
    HP = random.randint(500, 501)
    MP = random.randint(30, 50)

def enemy3():
    global enemyHP
    global enemyMP
    global enemyname3
    enemyHP = random.randint(500, 600)
    enemyMP = random.randint(350, 450)

    enemyname3 = "Alabasta"
    print(enemyname3 + "nya punya " + " " +
          str(enemyHP) + " " + "Total HP")
    print(enemyname3 + "nya punya " + " " +
          str(enemyMP) + " " + "Total MP")
    print("\n" + enemyname3 + " mempunyai Skill:")
    print(" 1. Bomb = 10 Kerusakan\n 2. Laser = 20 Kerusakan \n 3. Thunder = 30 Kerusakan")

#mulai
setup()
global name, HP, MP, enemyHP, enemyMP
print("\nTotal HP" + " " + str(HP))
print("Total MP" + " " + str(MP))
enemy3()

while enemyHP > 0:
    A = random.choice([1, 2, 3])
    print("Musuh memilih Skill", A)
#     enemy attack
    if enemyMP < 5:
        enemyhit = 3
        enemyhitmp = 3
        HP = HP - enemyhit
        enemyMP = enemyMP + enemyhitmp
        print("Giliran Musuhnya Menyerang Biasa " +
              str(enemyhit) + " Kerusakan ")
    elif A < 2:
        enemyhitskill1 = 10
        enemyhitskill1mp = 5
        print("Giliran Musuhnya Menyerang Dengan Skill Bomb " +
              str(enemyhitskill1) + " Kerusakan ")
        HP = HP - enemyhitskill1
        enemyMP = enemyMP - enemyhitskill1mp
    elif A < 3:
        enemyhitskill2 = 20
        enemyhitskill2mp = 10
        print("Giliran Musuhnya Menyerang Dengan Skill Laser " +
              str(enemyhitskill2) + " Kerusakan ")
        HP = HP - enemyhitskill2
        enemyMP = enemyMP - enemyhitskill2mp
    elif A < 4:
        enemyhitskill3 = 30
        enemyhitskill3mp = 20
        print("Giliran Musuhnya Menyerang Dengan Skill Thunder " +
              str(enemyhitskill3) + " Kerusakan ")
        HP = HP - enemyhitskill3
        enemyMP = enemyMP - enemyhitskill3mp
#   hero attack
    print("Sisa Nyawa " + name + " " + str(HP)+"HP")
    time.sleep(2)
    if HP <= 0:
        print("\nKamu Mati silahkan kembali dengan kekuatan yang lebih kuat "+name+" Mati")
        time.sleep(2)
        print("Game Over")
        time.sleep(2)
        sys.exit(0)
    else:
        hit = 80
        print(name + " Menyerang Mengakibatkan " + str(hit) + " Kerusakan")
        if enemyHP < 0:
            enemyHP -= enemyHP
        else:
            enemyHP = enemyHP - hit
        print("Sisa HP Alabasta = " + str(enemyHP) +
              " Dan MP Alabasta " + str(enemyMP))
        time.sleep(2)
else:
    time.sleep(2)
    print("\nWah " + enemyname3 + " Hidup kembali, kamu harus melawannya lagi")
    time.sleep(2)

#round 2
print("\nTotal HP kamu saat ini" + " " + str(HP))
print("Total MP kamu saat ini" + " " + str(MP))
print("\n")
enemy3()

while enemyHP > 0:
    A = random.choice([1, 2, 3])
    print("Musuh memilih Skill", A)
    if enemyMP < 5:
        enemyhit = 3
        enemyhitmp = 3
        HP = HP - enemyhit
        enemyMP = enemyMP + enemyhitmp
        print("Giliran Musuhnya Menyerang Biasa " +
              str(enemyhit) + " Kerusakan ")
    elif A < 2:
        enemyhitskill1 = 10
        enemyhitskill1mp = 5
        print("Giliran Musuhnya Menyerang Dengan Skill Bomb " +
              str(enemyhitskill1) + " Kerusakan ")
        HP = HP - enemyhitskill1
        enemyMP = enemyMP - enemyhitskill1mp
    elif A < 3:
        enemyhitskill2 = 20
        enemyhitskill2mp = 10
        print("Giliran Musuhnya Menyerang Dengan Skill Laser " +
              str(enemyhitskill2) + " Kerusakan ")
        HP = HP - enemyhitskill2
        enemyMP = enemyMP - enemyhitskill2mp
    elif A < 4:
        enemyhitskill3 = 30
        enemyhitskill3mp = 20
        print("Giliran Musuhnya Menyerang Dengan Skill Thunder " +
              str(enemyhitskill3) + " Kerusakan ")
        HP = HP - enemyhitskill3
        enemyMP = enemyMP - enemyhitskill3mp

    print("Sisa Nyawa " + name + " " + str(HP)+"HP")
    time.sleep(2)
    if HP <= 0:
        print("\nKamu Mati silahkan kembali dengan kekuatan yang lebih kuat "+name+" Mati")
        time.sleep(2)
        print("Game Over")
        time.sleep(2)
        sys.exit(0)
    else:
        hit = 80
        print(name + " Menyerang Mengakibatkan " + str(hit) + " Kerusakan")
        if enemyHP < 0:
            enemyHP -= enemyHP
        else:
            enemyHP = enemyHP - hit
        print("Sisa HP Alabasta = " + str(enemyHP) +
              " Dan MP Alabasta " + str(enemyMP))
        time.sleep(2)
else:
    print("Wah " + enemyname3 + " sudah mati, silakan melanjutkan perjalanan")