import random
import time
import sys
import dmgBar as dB
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

dmgKizaru = []
def setup():
    global name, HP, MP
    
    name = ("Luffy")
    MP = 1000
    HP = 1000


def enemy2():
    global enemyHP, enemyMP, enemyname2

    enemyHP = 2000
    enemyMP = 1500
    enemyname2 = "Admiral Kizaru"
    time.sleep(3)
    print(enemyname2 + "nya punya " + " " + 
            str(enemyHP) + " " + "Total HP")
    time.sleep(3)
    print(enemyname2 + "nya punya " + " " +
            str(enemyMP) + " " + "Total MP")
    time.sleep(3)
    print("\nAdmiral Kizaru mempunyai skill:")
    time.sleep(3)
    print(" 1. Light Beam = 10 Kerusakan\n 2. Speed of Light = 20 Kerusakan \n 3. Haki = 30 Kerusakan")
    time.sleep(3)



global name, HP, MP, enemyHP, enemyMP, enemyname2
name = "hero"
enemyname2 = "enemy"
HP = MP = 0
enemyHP = enemyMP = 0
setup()
print("\nTotal HP" + " " + str(HP))
print("Total MP" + " " + str(MP))
time.sleep(3)
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
            time.sleep(3)
        else:
            # A = input("pilih skill musuh : ")
            A = random.randint(1, 3)
            print("Musuh memilih Skill ", A)
            time.sleep(3)
            if A == 1:
                enemyhitskill1 = 20
                enemyhitskill1mp = 10
                print("Giliran Musuhnya Menyerang Dengan Light Beam " +
                    str(enemyhitskill1) + " Kerusakan ")
                time.sleep(3)
                HP -= enemyhitskill1
                enemyMP -= enemyhitskill1mp
                print("Sisa Nyawa " + name + " " + str(HP)+"HP")
                time.sleep(3)
            elif A == 2:
                enemyhitskill2 = 35
                enemyhitskill2mp = 20
                print("Giliran Musuhnya Menyerang Dengan Speed of Light " +
                    str(enemyhitskill2) + " Kerusakan ")
                time.sleep(3)
                HP -= enemyhitskill2
                enemyMP -= enemyhitskill2mp
                print("Sisa Nyawa " + name + " " + str(HP)+"HP")
                time.sleep(3)
            elif A == 3:
                enemyhitskill3 = 200
                enemyhitskill3mp = 150
                print("Giliran Musuhnya Menyerang Dengan Haki " +
                    str(enemyhitskill3) + " Kerusakan ")
                time.sleep(3)
                HP -=  enemyhitskill3
                enemyMP -= enemyhitskill3mp
                print("Sisa Nyawa " + name + " " + str(HP)+"HP")
                time.sleep(3)

        # time.sleep(2)
        Hits = random.randint(1, 4)
        #HERO ATTACK
        if HP <= 0:
            print("\nkarna kekuatan kizaru yang begitu kuat")
            time.sleep(5)
            print("\nluffy harus menerima kekalahan....")
            time.sleep(3)
            print("Tiba-tib.....")
            plt.imshow(mpimg.imread("./Pict/KizaruDanRey.jpg"))
            plt.axis('off')
            plt.show()
            time.sleep(8)
            enemyHP -= enemyHP
            HP -= HP
        else:
            if Hits == 1:
                if MP >= 80:
                    hit = 80
                    MP -= hit
                    dmgKizaru.append(hit)
                    print(name + " Menyerang Mengakibatkan " +
                        str(hit) + " Kerusakan")
                    time.sleep(3)
                    enemyHP -= hit
                    print("hero" , HP,  MP)
                    if enemyHP < 0:
                        enemyHP -= enemyHP
                    print("Sisa HP Admiral Kizaru = " + str(enemyHP) +
                        " Dan MP Admiral Kizaru " + str(enemyMP))
                    time.sleep(2)
                else :
                    print("Karena MP Rendah, Luffy menyerang dengan Basic Attack dan memulihkan MP")
                    time.sleep(3)
                    hit = 10
                    MP += 20
                    dmgKizaru.append(hit)
                    print(name + " Menyerang Mengakibatkan " +
                        str(hit) + " Kerusakan")
                    time.sleep(3)
                    enemyHP -= hit
                    print("hero" , HP,  MP)
                    time.sleep(3)
                    if enemyHP < 0:
                        enemyHP -= enemyHP
                    print("Sisa HP Admiral Kizaru = " + str(enemyHP) +
                        " Dan MP Admiral Kizaru " + str(enemyMP))
                    time.sleep(2)
            if Hits == 2:
                if MP >= 90:
                    hit = 90
                    MP -= hit
                    dmgKizaru.append(hit)
                    print(name + " Menyerang Mengakibatkan " +
                        str(hit) + " Kerusakan")
                    time.sleep(3)
                    enemyHP -=  hit
                    print("hero" , HP,  MP)
                    time.sleep(3)
                    if enemyHP < 0:
                        enemyHP -= enemyHP
                    print("Sisa HP Admiral Kizaru = " + str(enemyHP) +
                        " Dan MP Admiral Kizaru " + str(enemyMP))
                    time.sleep(2)
                else :
                    print("Karena MP Rendah, Luffy menyerang dengan Basic Attack dan memulihkan MP")
                    time.sleep(3)
                    hit = 10
                    MP += 20
                    dmgKizaru.append(hit)
                    print(name + " Menyerang Mengakibatkan " +
                        str(hit) + " Kerusakan")
                    time.sleep(3)
                    enemyHP -= hit
                    print("hero" , HP,  MP)
                    time.sleep(3)
                    if enemyHP < 0:
                        enemyHP -= enemyHP
                    print("Sisa HP Admiral Kizaru = " + str(enemyHP) +
                        " Dan MP Admiral Kizaru " + str(enemyMP))
                    time.sleep(2)
            if Hits == 3:
                if MP >= 100:
                    hit = 100
                    MP -= hit
                    dmgKizaru.append(hit)
                    print(name + " Menyerang Mengakibatkan " +
                        str(hit) + " Kerusakan")
                    time.sleep(3)
                    enemyHP -=  hit
                    print("hero" , HP,  MP)
                    time.sleep(3)
                    if enemyHP < 0:
                        enemyHP -= enemyHP
                    print("Sisa HP Admiral Kizaru = " + str(enemyHP) +
                        " Dan MP Admiral Kizaru " + str(enemyMP))
                    time.sleep(2)
                else :
                    print("Karena MP Rendah, Luffy menyerang dengan Basic Attack dan memulihkan MP")
                    time.sleep(3)
                    hit = 10
                    MP += 20
                    dmgKizaru.append(hit)
                    print(name + " Menyerang Mengakibatkan " +
                        str(hit) + " Kerusakan")
                    time.sleep(3)
                    enemyHP -= hit
                    print("hero" , HP,  MP)
                    time.sleep(3)
                    if enemyHP < 0:
                        enemyHP -= enemyHP
                    print("Sisa HP Admiral Kizaru = " + str(enemyHP) +
                        " Dan MP Admiral Kizaru " + str(enemyMP))
                    time.sleep(2)
            if Hits == 4:
                if MP >= 200:
                    hit = 200
                    MP -= hit
                    dmgKizaru.append(hit)
                    print(name + " Menyerang Mengakibatkan " +
                        str(hit) + " Kerusakan")
                    time.sleep(3)
                    enemyHP -=  hit
                    print("hero" , HP,  MP)
                    time.sleep(3)
                    if enemyHP < 0:
                        enemyHP -= enemyHP
                    print("Sisa HP Admiral Kizaru = " + str(enemyHP) +
                        " Dan MP Admiral Kizaru " + str(enemyMP))
                    time.sleep(2)
                else :
                    print("Karena MP Rendah, Luffy menyerang dengan Basic Attack dan memulihkan MP")
                    time.sleep(3)
                    hit = 10
                    MP += 20
                    dmgKizaru.append(hit)
                    print(name + " Menyerang Mengakibatkan " +
                        str(hit) + " Kerusakan")
                    time.sleep(3)
                    enemyHP -= hit
                    print("hero" , HP,  MP)
                    time.sleep(3)
                    if enemyHP < 0:
                        enemyHP -= enemyHP
                    print("Sisa HP Admiral Kizaru = " + str(enemyHP) +
                        " Dan MP Admiral Kizaru " + str(enemyMP))
                    time.sleep(3)
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
                time.sleep(3)
                HP -= enemyhitskill1
                enemyMP -= enemyhitskill1mp
                enemyHP += 5
                i += 1
        else:
            break

# else:
 #   time.sleep(2)
  #  print("Wah " + enemyname2 + " sudah mati, silakan melanjutkan perjalanan")
   # time.sleep(2)
print("\nTotal HP kamu saat ini" + " " + str(HP))
time.sleep(3)
print("Total MP kamu saat ini" + " " + str(MP))
time.sleep(3)
print("\n")

dB.kizaru(dmgKizaru)