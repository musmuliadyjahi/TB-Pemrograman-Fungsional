import random
import time
import sys
import dmgBar as dB

dmgKizaru = []
def setup():
    global name, HP, MP
    
    name = ("Luffy")
    MP = 1000
    HP = 1000


def enemy2():
    global enemyHP, enemyMP, enemyname2

    enemyHP = 1000
    enemyMP = 1000
    enemyname2 = "Admiral Kizaru"
    print(enemyname2 + "nya punya " + " " + 
            str(enemyHP) + " " + "Total HP")
    print(enemyname2 + "nya punya " + " " +
            str(enemyMP) + " " + "Total MP")
    print("\nAdmiral Kizaru mempunyai skill:")
    print(" 1. Light Beam = 10 Kerusakan\n 2. Speed of Light = 20 Kerusakan \n 3. Haki = 30 Kerusakan")



global name, HP, MP, enemyHP, enemyMP, enemyname2
name = "hero"
enemyname2 = "enemy"
HP = MP = 0
enemyHP = enemyMP = 0
setup()
print("\nTotal HP" + " " + str(HP))
print("Total MP" + " " + str(MP))
print("\n")
enemy2()

while enemyHP > 0:
    if enemyHP > 10:
        if enemyMP < 5:
            enemyhit = 3
            enemyhitmp = 3
            HP -= enemyhit
            enemyMP += enemyhitmp
            print("Giliran Musuhnya Menyerang Biasa " +
                  str(enemyhit) + " Kerusakan ")
        else:
            # A = input("pilih skill musuh : ")
            A = random.randint(1, 3)
            print("Musuh memilih Skill ", A)
            if A == 1:
                enemyhitskill1 = 10
                enemyhitskill1mp = 5
                print("Giliran Musuhnya Menyerang Dengan Light Beam " +
                    str(enemyhitskill1) + " Kerusakan ")
                HP -= enemyhitskill1
                enemyMP -= enemyhitskill1mp
                print("Sisa Nyawa " + name + " " + str(HP)+"HP")
            elif A == 2:
                enemyhitskill2 = 20
                enemyhitskill2mp = 10
                print("Giliran Musuhnya Menyerang Dengan Speed of Light " +
                    str(enemyhitskill2) + " Kerusakan ")
                HP -= enemyhitskill2
                enemyMP -= enemyhitskill2mp
                print("Sisa Nyawa " + name + " " + str(HP)+"HP")
            elif A == 3:
                enemyhitskill3 = 30
                enemyhitskill3mp = 20
                print("Giliran Musuhnya Menyerang Dengan Haki " +
                    str(enemyhitskill3) + " Kerusakan ")
                HP -=  enemyhitskill3
                enemyMP -= enemyhitskill3mp
                print("Sisa Nyawa " + name + " " + str(HP)+"HP")

        # time.sleep(2)
        Hits = random.randint(1, 4)
        #HERO ATTACK
        if HP <= 0:
            print("\nkarna kekuatan kizaru yang begitu kuat")
            # time.sleep(5)
            print("\nluffy harus menerima kekalahan....")
            # time.sleep(3)
            print("namun dia tidak menyerah dan akan kembali dengan tenaga yang lebih kuat")
            # time.sleep(8)
        else:
            if Hits == 1:
                if MP >= 80:
                    hit = 80
                    MP -= hit
                    dmgKizaru.append(hit)
                    print(name + " Menyerang Mengakibatkan " +
                        str(hit) + " Kerusakan")
                    enemyHP -= hit
                    print("hero" , HP,  MP)
                    if enemyHP < 0:
                        enemyHP -= enemyHP
                    print("Sisa HP Admiral Kizaru = " + str(enemyHP) +
                        " Dan MP Admiral Kizaru " + str(enemyMP))
                    # time.sleep(2)
                else :
                    print("Because Low MP, hero attack with basic attack and recover MP")
                    hit = 10
                    MP += 20
                    dmgKizaru.append(hit)
                    print(name + " Menyerang Mengakibatkan " +
                        str(hit) + " Kerusakan")
                    enemyHP -= hit
                    print("hero" , HP,  MP)
                    if enemyHP < 0:
                        enemyHP -= enemyHP
                    print("Sisa HP Admiral Kizaru = " + str(enemyHP) +
                        " Dan MP Admiral Kizaru " + str(enemyMP))
                    # time.sleep(2)
            if Hits == 2:
                if MP >= 90:
                    hit = 90
                    MP -= hit
                    dmgKizaru.append(hit)
                    print(name + " Menyerang Mengakibatkan " +
                        str(hit) + " Kerusakan")
                    enemyHP -=  hit
                    print("hero" , HP,  MP)
                    if enemyHP < 0:
                        enemyHP -= enemyHP
                    print("Sisa HP Admiral Kizaru = " + str(enemyHP) +
                        " Dan MP Admiral Kizaru " + str(enemyMP))
                    # time.sleep(2)
                else :
                    print("Because Low MP, hero attack with basic attack and recover MP")
                    hit = 10
                    MP += 20
                    dmgKizaru.append(hit)
                    print(name + " Menyerang Mengakibatkan " +
                        str(hit) + " Kerusakan")
                    enemyHP -= hit
                    print("hero" , HP,  MP)
                    if enemyHP < 0:
                        enemyHP -= enemyHP
                    print("Sisa HP Admiral Kizaru = " + str(enemyHP) +
                        " Dan MP Admiral Kizaru " + str(enemyMP))
                    # time.sleep(2)
            if Hits == 3:
                if MP >= 100:
                    hit = 100
                    MP -= hit
                    dmgKizaru.append(hit)
                    print(name + " Menyerang Mengakibatkan " +
                        str(hit) + " Kerusakan")
                    enemyHP -=  hit
                    print("hero" , HP,  MP)
                    if enemyHP < 0:
                        enemyHP -= enemyHP
                    print("Sisa HP Admiral Kizaru = " + str(enemyHP) +
                        " Dan MP Admiral Kizaru " + str(enemyMP))
                    # time.sleep(2)
                else :
                    print("Because Low MP, hero attack with basic attack and recover MP")
                    hit = 10
                    MP += 20
                    dmgKizaru.append(hit)
                    print(name + " Menyerang Mengakibatkan " +
                        str(hit) + " Kerusakan")
                    enemyHP -= hit
                    print("hero" , HP,  MP)
                    if enemyHP < 0:
                        enemyHP -= enemyHP
                    print("Sisa HP Admiral Kizaru = " + str(enemyHP) +
                        " Dan MP Admiral Kizaru " + str(enemyMP))
                    # time.sleep(2)
            if Hits == 4:
                if MP >= 200:
                    hit = 200
                    MP -= hit
                    dmgKizaru.append(hit)
                    print(name + " Menyerang Mengakibatkan " +
                        str(hit) + " Kerusakan")
                    enemyHP -=  hit
                    print("hero" , HP,  MP)
                    if enemyHP < 0:
                        enemyHP -= enemyHP
                    print("Sisa HP Admiral Kizaru = " + str(enemyHP) +
                        " Dan MP Admiral Kizaru " + str(enemyMP))
                    # time.sleep(2)
                else :
                    print("Because Low MP, hero attack with basic attack and recover MP")
                    hit = 10
                    MP += 20
                    dmgKizaru.append(hit)
                    print(name + " Menyerang Mengakibatkan " +
                        str(hit) + " Kerusakan")
                    enemyHP -= hit
                    print("hero" , HP,  MP)
                    if enemyHP < 0:
                        enemyHP -= enemyHP
                    print("Sisa HP Admiral Kizaru = " + str(enemyHP) +
                        " Dan MP Admiral Kizaru " + str(enemyMP))
                    # time.sleep(2)
    else:
        if enemyHP > 0 and enemyMP > 0:
            print("Ilmu Kebal Aktif")
            i = 0
            while i < 3:
                enemyhitskill1 = 10
                enemyhitskill1mp = 5
                print("Giliran Musuhnya Menyerang Dengan Light Beam " +
                      str(enemyhitskill1) + " Kerusakan ")
                HP -= enemyhitskill1
                enemyMP -= enemyhitskill1mp
                enemyHP += 5
                i += 1
        else:
            break
else:
    enemyHP -= enemyHP
    print("Admiral Mati")
# else:
 #   time.sleep(2)
  #  print("Wah " + enemyname2 + " sudah mati, silakan melanjutkan perjalanan")
   # time.sleep(2)
print("\nTotal HP kamu saat ini" + " " + str(HP))
print("Total MP kamu saat ini" + " " + str(MP))
print("\n")

dB.kizaru(dmgKizaru)