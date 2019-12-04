import sys, time, random, pygame
import wholeCakeIsland as WCI
import dressrosa as DS
import sabaodyPacifista as sP

def luffy(heroHP, heroMP):
    global heroDmg, hpR, mpR  # deklarasi global
    hpR = mpR = 0
    print("1. Skill\n2. Basic")
    if heroHP > 0:
        if heroMP > 0:
            # MPs = int(input("Silahkan Masukkan pilihan [1,2]"))
            MPs = random.randint(1, 2)
            if MPs == 1:
                if heroMP >= 10:
                    print("hero attack with 10 MP")
                    heroMP -= 10  # mengurangi MP hero
                    heroDmg = 10  # mendeklarasi dmg untuk musuh
                    WCI.bogMomProfile(heroDmg)  # send dmg to enemy profile
                    if WCI.enemyHP <= 0:  # cek dara musuh, jika darah musuh 0 maka selesai
                        WCI.enemyHP -= WCI.enemyHP  # anti minus
                        print("I win and my HP is", heroHP,
                              "and my MP is", heroMP)
                        hpR = heroHP
                        mpR = heroMP
                        time.sleep(3)
                    elif heroHP > 0:
                        heroHP -= WCI.dmgSend  # mengurangi darah hero
                        if heroHP < 0:
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
                    WCI.bogMomProfile(heroDmg)  # send dmg to enemy profile
                    if WCI.enemyHP <= 0:  # cek dara musuh, jika darah musuh 0 maka selesai
                        WCI.enemyHP -= WCI.enemyHP  # anti minus
                        print("I win and my HP is", heroHP,
                              "and my MP is", heroMP)
                        hpR = heroHP
                        mpR = heroMP
                        time.sleep(3)
                    elif heroHP > 0:
                        heroHP -= WCI.dmgSend  # mengurangi darah hero
                        if heroHP < 0:
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
    return hpR, mpR


def luffy2(heroHP, heroMP):
    global heroDmg, hpR, mpR  # deklarasi global
    hpR = mpR = 0
    if heroHP > 0:
        if heroMP > 0:
            MPs = 1  # random.randint(1, 5)
            if MPs == 1:
                if heroMP >= 20:
                    print("hero attack with 20 MP")
                    heroMP -= 20
                    heroDmg = 20
                    # send dmg to enemy profile
                    DS.dofflaminggoProfile(heroDmg)
                    if DS.enemyHP <= 0:
                        DS.enemyHP -= DS.enemyHP  # anti minus
                        print("I win and my HP is", heroHP,
                              "and my MP is", heroMP)
                        hpR = heroHP
                        mpR = heroMP
                    else:
                        heroHP -= DS.dmgSend
                        if heroHP < 0:
                            heroHP -= heroHP
                        print("hero", heroHP, heroMP)
                        luffy2(heroHP, heroMP)
                else:
                    print("hero Failed attack because low MP")
        else:
            print("hero out of MP, can't fight anymore")
            heroHP -= heroHP
    else:
        print("hero lose")
    return hpR, mpR


def luffy3(heroHP, heroMP):
    global heroDmg
    if heroHP > 0:
        if heroMP > 0:
            MPs = 1  # random.randint(1, 5)
            if MPs == 1:
                if heroMP >= 10:
                    print("hero attack with 10 MP")
                    heroMP -= 10
                    heroDmg = 10
                    # send dmg to enemy profile
                    sP.pacifistaProfile(heroDmg)
                    if sP.enemyHP == 0:
                        print("I win and my HP is", heroHP,
                              "and my MP is", heroMP)
                        sys.exit(0)
                    elif heroHP > 0:
                        heroHP -= sP.dmgSend
                        if heroHP < 0:
                            print("minus")
                            heroHP -= heroHP
                        print("hero", heroHP, heroMP)
                        luffy(heroHP, heroMP)
                else:
                    print("hero Failed attack because low MP")
        else:
            print("hero out of MP, can't fight anymore")
            heroHP -= heroHP
    else:
        print("hero lose")


# global defnie
global heroDmg, hpR, mpR, heroHP, heroMP
heroDmg = mpR = hpR = 0
# hero Profile
heroHP = heroMP = 1000
pygame.mixer.init()
pygame.mixer.music.load("KDA.mp3")
pygame.mixer.music.play()

import alabasta
print("Luffy 3")
luffy3(heroHP, heroMP)
pygame.mixer.music.stop()
heroHP = hpR
heroMP = mpR
import sabaodyKizaru
print("Luffy 2")
luffy2(heroHP, heroMP)
heroHP = hpR
heroMP = mpR
print("Luffy 1")
luffy(heroHP, heroMP)