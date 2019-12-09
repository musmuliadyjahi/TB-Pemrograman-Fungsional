import random
import sys
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def pacifistaProfile(dmgRecived):
    global enemyHP, enemyMP, dodge
    if dodge == 0:
        dmgRecived = 0
        enemyHP -= dmgRecived
        time.sleep(3)
        print("Pacifista menghindari serangan")
        time.sleep(3)
        dodge = 3
    elif dodge > 0:
        enemyHP -= dmgRecived
        dodge -= 1
    enemyRemHP = enemyHP
    time.sleep(3)
    pacifista(enemyRemHP, enemyMP)
    if enemyMP > 0:
        enemyMP -= dmgSend  # mengurangi MP musuh
        enemyRemMP = enemyMP  # mendeklarasi MP musuh ke lokal
    else:
        time.sleep(3)
        print("Pacifista kehabisan MP")
        time.sleep(3)
        print("Pacifista Kalah")
        time.sleep(3)
        enemyHP -= enemyHP

    if enemyHP <0 : #anti minus HP
        enemyHP -= enemyHP
    print("Sisa HP Pacifista :", enemyHP, " dan MP Pacifista :", enemyMP)
    time.sleep(3)
    return enemyHP, enemyMP


def pacifista(enemyHP, enemyMP):
    global dmgSend
    # global heroHP
    if enemyHP > 0:
        if enemyMP > 0:
            MPs = random.randint(1, 4)
            if MPs == 1:
                if enemyMP >= 10:
                    print("Pacifista menyerang dengan Basic Attack")
                    time.sleep(3)
                    dmgSend = 10
                else:
                    print("Pacifista gagal menyerang karena kekurangan MP")
                    time.sleep(3)
                    dmgSend = 0
            elif MPs == 2:
                if enemyMP >= 15:
                    print("Pacifista menyerang dengan Laser Beam")
                    time.sleep(3)
                    dmgSend = 15
                else:
                    print("Pacifista gagal menyerang karena kekurangan MP")
                    time.sleep(3)
                    dmgSend = 0
            elif MPs == 3:
                if enemyMP >= 20:
                    print("Pacifista menyerang dengan Super Punch Steel")
                    time.sleep(3)
                    dmgSend = 20
                else:
                    print("Pacifista gagal menyerang karena kekurangan MP")
                    time.sleep(3)
                    dmgSend = 0
            elif MPs == 4:
                if enemyMP >= 50:
                    print("Pacifista menyerang dengan Special attack")
                    time.sleep(3)
                    dmgSend = 100
                else:
                    print("Pacifista gagal menyerang karena kekurangan MP")
                    time.sleep(3)
                    dmgSend = 0
    else:
        plt.imshow(mpimg.imread("./Pict/paciKalah.jpg"))
        plt.axis('off')
        plt.show()
        time.sleep(3)
        print("Berhasil mengalahkan Pacifista")
    return dmgSend, enemyMP


#global profile
global dmgSend, dodge
dmgSend = 0
dodge = 3

# enemy Profile
global enemyHP, enemyMP
enemyHP = enemyMP = 1000
