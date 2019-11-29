import sys


def luffy(heroHP, heroMP):
    global heroDmg  # deklarasi global
    print("1. Skill")
    print("2. Basic")
    if heroHP > 0:
        if heroMP > 0:
            MPs = int(input("Silahkan Masukkan pilihan [1,2]"))
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
                            heroHP -= heroHP  # anti minus HP
                        print("hero", heroHP, heroMP)  # print status hero
                        # memanggil method hero kembali dengan
                        # status yang sudah di perbaharui
                        luffy(heroHP, heroMP)
                else:
                    print("hero Failed attack because low MP")
            if MPs == 2:
                if heroMP >= 1:
                    print("hero attack with 10 MP")
                    heroMP -= 1  # mengurangi MP hero
                    heroDmg = 1  # mendeklarasi dmg untuk musuh
                    enemyProfile(heroDmg)  # send dmg to enemy profile
                    if enemyHP == 0:  # cek dara musuh, jika darah musuh 0 maka selesai
                        print("I win and my HP is", heroHP,
                              "and my MP is", heroMP)
                        sys.exit(0)
                    elif heroHP > 0:
                        heroHP -= dmgSend  # mengurangi darah hero
                        if heroHP < 0:
                            print("minus")
                            heroHP -= heroHP  # anti minus HP
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


# global profile
global dmgSend, heroDmg, dodge
heroDmg = dmgSend = 0
dodge = 3

# hero Profile
global heroHP, heroMP
heroHP = heroMP = 100

luffy(heroHP, heroMP)
