import sys
import time
import random
import pygame
import wholeCakeIsland as WCI
import dressrosa as DS
import sabaodyPacifista as sP


def pacifista(heroHP, heroMP):  # Pacifista
    global heroDmg
    if heroHP > 0:
        if heroMP > 0:
            MPs = random.randint(1, 4)
            if MPs == 1:
                if heroMP >= 80:
                    print("hero attack with 80 MP")
                    heroMP -= 80
                    heroDmg = 80
                    # send dmg to enemy profile
                    sP.pacifistaProfile(heroDmg)
                    if sP.enemyHP == 0:
                        print("I win and my HP is", heroHP,
                              "and my MP is", heroMP)
                        time.sleep(3)
                    elif heroHP > 0:
                        heroHP -= sP.dmgSend
                        if heroHP < 0:
                            print("minus")
                            heroHP -= heroHP
                        print("hero", heroHP, heroMP)
                        pacifista(heroHP, heroMP)
                elif MPs == 2:
                    if heroMP >= 90:
                        print("hero attack with 90 MP")
                        heroMP -= 90
                        heroDmg = 90
                        # send dmg to enemy profile
                        sP.pacifistaProfile(heroDmg)
                        if sP.enemyHP == 0:
                            print("I win and my HP is", heroHP,
                                  "and my MP is", heroMP)
                            time.sleep(3)
                        elif heroHP > 0:
                            heroHP -= sP.dmgSend
                            if heroHP < 0:
                                print("minus")
                                heroHP -= heroHP
                            print("hero", heroHP, heroMP)
                            pacifista(heroHP, heroMP)
                elif MPs == 3:
                    if heroMP >= 100:
                        print("hero attack with 100 MP")
                        heroMP -= 100
                        heroDmg = 100
                        # send dmg to enemy profile
                        sP.pacifistaProfile(heroDmg)
                        if sP.enemyHP == 0:
                            print("I win and my HP is", heroHP,
                                  "and my MP is", heroMP)
                            time.sleep(3)
                        elif heroHP > 0:
                            heroHP -= sP.dmgSend
                            if heroHP < 0:
                                print("minus")
                                heroHP -= heroHP
                            print("hero", heroHP, heroMP)
                            pacifista(heroHP, heroMP)
                elif MPs == 4:
                    if heroMP >= 200:
                        print("hero attack with 200 MP")
                        heroMP -= 200
                        heroDmg = 200
                        # send dmg to enemy profile
                        sP.pacifistaProfile(heroDmg)
                        if sP.enemyHP == 0:
                            print("I win and my HP is", heroHP,
                                  "and my MP is", heroMP)
                            time.sleep(3)
                        elif heroHP > 0:
                            heroHP -= sP.dmgSend
                            if heroHP < 0:
                                print("minus")
                                heroHP -= heroHP
                            print("hero", heroHP, heroMP)
                            pacifista(heroHP, heroMP)
                else:
                    print("hero Failed attack because low MP")
        else:
            print("hero out of MP, can't fight anymore")
            heroHP -= heroHP
    else:
        print("hero lose")


def dofflaminggo(heroHP, heroMP):  # Doflaminggo
    global heroDmg, hpR, mpR  # deklarasi global
    hpR = mpR = 0
    if heroHP > 0:
        if heroMP > 0:
            MPs = 1  # random.randint(1, 5)
            if MPs == 1:
                if heroMP >= 80:
                    print("hero attack with 80 MP")
                    heroMP -= 80
                    heroDmg = 80
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
                        dofflaminggo(heroHP, heroMP)
                if MPs == 2:
                    if heroMP >= 90:
                        print("hero attack with 90 MP")
                        heroMP -= 90
                        heroDmg = 90
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
                            dofflaminggo(heroHP, heroMP)
                if MPs == 3:
                    if heroMP >= 100:
                        print("hero attack with 100 MP")
                        heroMP -= 100
                        heroDmg = 100
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
                            dofflaminggo(heroHP, heroMP)
                if MPs == 4:
                    if heroMP >= 200:
                        print("hero attack with 200 MP")
                        heroMP -= 200
                        heroDmg = 200
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
                            dofflaminggo(heroHP, heroMP)
                else:
                    print("hero Failed attack because low MP")
        else:
            print("hero out of MP, can't fight anymore")
            heroHP -= heroHP
    else:
        print("hero lose")
    return hpR, mpR


def bigMom(heroHP, heroMP):  # bigMOM
    global heroDmg, hpR, mpR  # deklarasi global
    hpR = mpR = 0
    print("1. Skill\n2. Basic")
    if heroHP > 0:
        if heroMP > 0:
            # MPs = int(input("Silahkan Masukkan pilihan [1,2]"))
            MPs = random.randint(1, 2)
            if MPs == 1:
                if heroMP >= 80:
                    print("hero attack with 80 MP")
                    heroMP -= 80  # mengurangi MP hero
                    heroDmg = 80  # mendeklarasi dmg untuk musuh
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
                        bigMom(heroHP, heroMP)
                else:
                    print("hero Failed attack because low MP")
            elif MPs == 2:
                if heroMP >= 90:
                    print("hero attack with 90 MP")
                    heroMP -= 90  # mengurangi MP hero
                    heroDmg = 90  # mendeklarasi dmg untuk musuh
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
                        bigMom(heroHP, heroMP)
                elif MPs == 3:
                    if heroMP >= 100:
                        print("hero attack with 100 MP")
                        heroMP -= 100  # mengurangi MP hero
                        heroDmg = 100  # mendeklarasi dmg untuk musuh
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
                            bigMom(heroHP, heroMP)
                elif MPs == 4:
                    if heroMP >= 200:
                        print("hero attack with 200 MP")
                        heroMP -= 200  # mengurangi MP hero
                        heroDmg = 200  # mendeklarasi dmg untuk musuh
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
                            bigMom(heroHP, heroMP)
                else:
                    print("hero Failed attack because low MP")
        else:
            print("hero out of MP, can't fight anymore")
            heroHP -= heroHP
    else:
        print("hero lose")
    return hpR, mpR


# global defnie
global heroDmg, hpR, mpR, heroHP, heroMP
heroDmg = mpR = hpR = 0
# hero Profile
heroHP = heroMP = 1000
pygame.mixer.init()
pygame.mixer.music.load("KDA.mp3")
pygame.mixer.music.play()

import alabasta
print("Musuh : Crocodile")
time.sleep(2)
print("Musuh : Pacifista & kizaru")
time.sleep(2)
pacifista(heroHP, heroMP)
import sabaodyKizaru
pygame.mixer.music.stop()
print("Luffy 2")
dofflaminggo(heroHP, heroMP)
print("Luffy 1")
bigMom(heroHP, heroMP)
