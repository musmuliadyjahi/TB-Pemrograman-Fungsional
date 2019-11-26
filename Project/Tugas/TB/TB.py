import random
import sys


def enemyProfile(dmgRecived):
    global enemyHP, enemyMP  # deklarasi agar bisa dipakai global
    enemyHP -= dmgRecived  # mengurangi darah musuh
    enemyRemHP = enemyHP  # mendeklarasi darah musuh ke lokal
    # memanggil method musuh untuk mengaktifkan skill
    alabasta(enemyRemHP, enemyMP)
    enemyMP -= dmgSend  # mengurangi MP musuh
    enemyRemMP = enemyMP  # mendeklarasi MP musuh ke lokal
    return enemyHP, enemyMP  # mengembalikan sisa HP & MP musuh


def alabasta(enemyHP, enemyMP):
    global dmgSend
    if enemyHP > 0:
        if enemyMP > 0:
            MPs = random.randint(1, 3 )
            if MPs == 1:
                if enemyMP >= 10:
                    print("enemy attack with 10 MP")
                    dmgSend = 10
                    print("Enemy", enemyHP, enemyMP)
                else:
                    print("enemy Failed attack because low MP")
                    dmgSend = 0
            elif MPs == 2:
                if enemyMP >= 20:
                    print("enemy Attack with 20 MP")
                    dmgSend = 20
                    print("Enemy", enemyHP, enemyMP)
                else:
                    print("enemy Failed attack because low MP")
                    dmgSend = 0
            elif MPs == 3:
                if enemyMP >= 30:
                    print("enemy Attack with 30 MP")
                    dmgSend = 30
                    print("Enemy", enemyHP, enemyMP)
                else:
                    print("enemy Failed attack because low MP")
                    dmgSend = 0
        else:
            print("Enemy out of MP, can't fight anymore")
            enemyHP -= enemyHP
    else:
        print("Enemy Lose")
    return dmgSend, enemyMP


def luffy(heroHP, heroMP):
    global heroDmg  # deklarasi global
    if heroHP > 0:
        if heroMP > 0:
            MPs = 1  # random.randint(1, 5)
            if MPs == 1:
                if heroMP >= 10:
                    print("hero attack with 10 MP")
                    heroMP -= 10  # mengurangi MP hero
                    heroDmg = 10  # mendeklarasi dmg untuk musuh
                    enemyProfile(heroDmg)  # send dmg to enemy profile
                    if enemyHP == 0:  # cek dara musuh, jika darah musuh 0 maka selesai
                        print("I win and my HP is", heroHP,
                              "and my MP is", heroMP)
                        sys.exit(0)
                    elif heroHP > 0:
                        heroHP -= dmgSend  # mengurangi darah hero
                        if heroHP < 0:
                            print("minus")
                            heroHP -= heroHP #anti minus HP
                        print("hero", heroHP, heroMP)  # print status hero
                        # memanggil method hero kembali dengan
                        # status yang sudah di perbaharui
                        luffy(heroHP, heroMP)
                else:
                    print("hero Failed attack because low MP")
        else:
            print("hero out of MP, can't fight anymore")
            heroHP -= heroHP
    else:
        print("hero lose")


#global profile
global dmgSend, heroDmg
heroDmg = dmgSend = 0

# enemy Profile
global enemyHP, enemyMP
enemyHP = enemyMP = 100

# hero Profile
global heroHP, heroMP
heroHP = heroMP = 100

luffy(heroHP, heroMP)
