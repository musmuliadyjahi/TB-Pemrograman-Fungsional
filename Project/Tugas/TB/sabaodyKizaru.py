import random
import time
import sys


def setup():
    global name
    global HP
    global MP

    name = ("Luffy")

    MP = HP = 1000


def enemy2():
    global enemyHP
    global enemyMP
    global enemyname2
    enemyHP = 1000
    enemyMP = 1000

    enemyname2 = "Admiral Kizaru"
    print(enemyname2 + "nya punya " + " " + str(enemyHP) + " " + "Total HP")
    print(enemyname2 + "nya punya " + " " +
          str(enemyMP) + " " + "Total MP")
    print("\nAdmiral Kizaru mempunyai kill:")
    print(" 1. Light Beam = 10 Kerusakan\n 2. Speed of Light = 20 Kerusakan \n 3. Haki = 30 Kerusakan")


setup()
global name
global HP
global MP
global enemyHP
global enemyMP
print("\nTotal HP" + " " + str(HP))
print("Total MP" + " " + str(MP))
print("\n")
enemy2()

while enemyHP > 0:
    if enemyHP > 10:
        if enemyMP < 5:
            enemyhit = 3
            enemyhitmp = 3
            HP = HP - enemyhit
            enemyMP = enemyMP + enemyhitmp
            print("Giliran Musuhnya Menyerang Biasa " +
                  str(enemyhit) + " Kerusakan ")
        else:
            # A = input("pilih skill musuh : ")
            A = random.randint(1, 3)
            print("Musuh memilih Skill", A)
        if A == '1':
            enemyhitskill1 = 10
            enemyhitskill1mp = 5
            print("Giliran Musuhnya Menyerang Dengan Light Beam " +
                  str(enemyhitskill1) + " Kerusakan ")
            HP = HP - enemyhitskill1
            enemyMP = enemyMP - enemyhitskill1mp
            print("Sisa Nyawa " + name + " " + str(HP)+"HP")
        elif A == '2':
            enemyhitskill2 = 20
            enemyhitskill2mp = 10
            print("Giliran Musuhnya Menyerang Dengan Speed of Light " +
                  str(enemyhitskill2) + " Kerusakan ")
            HP = HP - enemyhitskill2
            enemyMP = enemyMP - enemyhitskill2mp
            print("Sisa Nyawa " + name + " " + str(HP)+"HP")
        elif A == '3':
            enemyhitskill3 = 30
            enemyhitskill3mp = 20
            print("Giliran Musuhnya Menyerang Dengan Haki " +
                  str(enemyhitskill3) + " Kerusakan ")
            HP = HP - enemyhitskill3
            enemyMP = enemyMP - enemyhitskill3mp
            print("Sisa Nyawa " + name + " " + str(HP)+"HP")

        time.sleep(2)
        Hits = random.randint(1, 4)
        if HP <= 0:
            print("\nkarna kekuatan kizaru yang begitu kuat")
            time.sleep(5)
            print("\nluffy harus menerima kekalahan....")
            time.sleep(3)
            print("namun dia tidak menyerah dan akan kembali dengan tenaga yang lebih kuat")

            time.sleep(8)
        else:
            if Hits == 1:
                hit = 80
                print(name + " Menyerang Mengakibatkan " +
                      str(hit) + " Kerusakan")
                enemyHP = enemyHP - hit
                print("Sisa HP Admiral Kizaru = " + str(enemyHP) +
                      " Dan MP Admiral Kizaru " + str(enemyMP))
                time.sleep(2)
            if Hits == 2:
                hit = 90
                print(name + " Menyerang Mengakibatkan " +
                      str(hit) + " Kerusakan")
                enemyHP = enemyHP - hit
                print("Sisa HP Admiral Kizaru = " + str(enemyHP) +
                      " Dan MP Admiral Kizaru " + str(enemyMP))
                time.sleep(2)
            if Hits == 3:
                hit = 100
                print(name + " Menyerang Mengakibatkan " +
                      str(hit) + " Kerusakan")
                enemyHP = enemyHP - hit
                print("Sisa HP Admiral Kizaru = " + str(enemyHP) +
                      " Dan MP Admiral Kizaru " + str(enemyMP))
                time.sleep(2)
            if Hits == 1:
                hit = 200
                print(name + " Menyerang Mengakibatkan " +
                      str(hit) + " Kerusakan")
                enemyHP = enemyHP - hit
                print("Sisa HP Admiral Kizaru = " + str(enemyHP) +
                      " Dan MP Admiral Kizaru " + str(enemyMP))
                time.sleep(2)
    else:
        if enemyHP > 0 and enemyMP > 0:
            print("Ilmu Kebal Aktif")
            i = 0
            while i < 3:
                enemyhitskill1 = 10
                enemyhitskill1mp = 5
                print("Giliran Musuhnya Menyerang Dengan Light Beam " +
                      str(enemyhitskill1) + " Kerusakan ")
                HP = HP - enemyhitskill1
                enemyMP = enemyMP - enemyhitskill1mp
                enemyHP = enemyHP - 5
                i += 1
        else:
            break
else:
    print("Admiral Mati")
# else:
 #   time.sleep(2)
  #  print("Wah " + enemyname2 + " sudah mati, silakan melanjutkan perjalanan")
   # time.sleep(2)
print("\nTotal HP kamu saat ini" + " " + str(HP))
print("Total MP kamu saat ini" + " " + str(MP))
print("\n")
