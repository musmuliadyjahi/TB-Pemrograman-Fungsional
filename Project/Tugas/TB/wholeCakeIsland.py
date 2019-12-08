import random, time

def bogMomProfile(dmgRecived):
    global enemyHP, enemyMP, dodge  # deklarasi agar bisa dipakai global
    # logika menghindar serangan setiap 3 turn
    if dodge == 0:
        dmgRecived = 0  # mengubah dmg yang diterima menjadi 0
        enemyHP -= dmgRecived
        print("Enemy Dodge")
        dodge = 3
        time.sleep(3)
    elif dodge > 0:
        enemyHP -= dmgRecived  # mengurangi darah musuh
        dodge -= 1  # mengurangi count untuk menghindar
    enemyRemHP = enemyHP  # mendeklarasi darah musuh ke lokal
    # memanggil method musuh untuk mengaktifkan skill
    bigMom(enemyRemHP, enemyMP)
    if enemyMP > 0:
        enemyMP -= dmgSend  # mengurangi MP musuh
        enemyRemMP = enemyMP  # mendeklarasi MP musuh ke lokal
    else:
        print("Enemy out of MP, can't fight anymore")
        time.sleep(3)
        
    if enemyHP<0:
        enemyHP -= enemyHP
    print("Enemy", enemyHP, enemyMP)
    time.sleep(3)
    return enemyHP, enemyMP  # mengembalikan sisa HP & MP musuh


def bigMom(enemyHP, enemyMP):
    global dmgSend
    if enemyHP > 0:
        if enemyMP > 0:
            MPs = random.randint(1, 3)
            if MPs == 1:
                if enemyMP >= 10:
                    print("enemy attack with 10 MP")
                    time.sleep(3)
                    dmgSend = 10
                else:
                    print("enemy Failed attack because low MP")
                    time.sleep(3)
                    dmgSend = 0
            elif MPs == 2:
                if enemyMP >= 20:
                    print("enemy Attack with 20 MP")
                    time.sleep(3)
                    dmgSend = 20
                else:
                    print("enemy Failed attack because low MP")
                    time.sleep(3)
                    dmgSend = 0
            elif MPs == 3:
                if enemyMP >= 30:
                    print("enemy Attack with 30 MP")
                    time.sleep(3)
                    dmgSend = 30
                else:
                    print("enemy Failed attack because low MP")
                    time.sleep(3)
                    dmgSend = 0
        else:
            dmgSend = 0
    else:
        print("Enemy Lose")
        time.sleep(3)
    return dmgSend, enemyMP


# global profile
global dodge, enemyHP, enemyMP, dmgSend
dmgSend = 0
dodge = 3
enemyHP = enemyMP = 1000
