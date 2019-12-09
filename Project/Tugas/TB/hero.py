import sys
import time
import random
import pygame
import wholeCakeIsland as WCI
import dressrosa as DS
import dmgBar as dB
import story as SL
import sabaodyPacifista as sP
import matplotlib.pyplot as plt


# global defnie
global heroDmg, heroHP, heroMP, dmgToDoffy, dmgToBigMom
heroDmg = 0
dmgToDoffy = []
dmgToBigMom = []
dmgToPaci = []
# hero Profile
heroHP = 1000
heroMP = 1500

hero = {'name': 'Luffy'}


def pacifista(heroHP, heroMP):  # Pacifista
    global heroDmg
    if sP.enemyHP > 0:
        if heroHP > 0:
            if heroMP > 0:
                MPs = random.randint(1, 4)
                if MPs == 1:
                    if heroMP >= 80:
                        print("hero attack with 80 MP")
                        heroMP -= 80
                        heroDmg = 80
                        dmgToPaci.append(heroDmg)
                        # send dmg to enemy profile
                        sP.pacifistaProfile(heroDmg)
                        heroHP -= sP.dmgSend
                        if heroHP < 0:
                            heroHP -= heroHP
                        print(hero['name'], heroHP, heroMP)
                        pacifista(heroHP, heroMP)
                    else:
                        print(
                            "Because Low MP, hero attack with basic attack and recover MP")
                        heroMP += 20  # menambah MP hero
                        heroDmg = 10
                        # send dmg to enemy profile
                        sP.pacifistaProfile(heroDmg)
                        heroHP -= sP.dmgSend
                        if heroHP < 0:
                            heroHP -= heroHP
                        print(hero['name'], heroHP, heroMP)
                        pacifista(heroHP, heroMP)
                elif MPs == 2:
                    if heroMP >= 90:
                        print("hero attack with 90 MP")
                        heroMP -= 90
                        heroDmg = 90
                        dmgToPaci.append(heroDmg)
                        # send dmg to enemy profile
                        sP.pacifistaProfile(heroDmg)
                        heroHP -= sP.dmgSend
                        if heroHP < 0:
                            heroHP -= heroHP
                        print(hero['name'], heroHP, heroMP)
                        pacifista(heroHP, heroMP)
                    else:
                        print(
                            "Because Low MP, hero attack with basic attack and recover MP")
                        heroMP += 20  # menambah MP hero
                        heroDmg = 10
                        # send dmg to enemy profile
                        sP.pacifistaProfile(heroDmg)
                        heroHP -= sP.dmgSend
                        if heroHP < 0:
                            heroHP -= heroHP
                        print(hero['name'], heroHP, heroMP)
                        pacifista(heroHP, heroMP)
                elif MPs == 3:
                    if heroMP >= 100:
                        print("hero attack with 100 MP")
                        heroMP -= 100
                        heroDmg = 100
                        dmgToPaci.append(heroDmg)
                        # send dmg to enemy profile
                        sP.pacifistaProfile(heroDmg)
                        heroHP -= sP.dmgSend
                        if heroHP < 0:
                            heroHP -= heroHP
                        print(hero['name'], heroHP, heroMP)
                        pacifista(heroHP, heroMP)
                    else:
                        print(
                            "Because Low MP, hero attack with basic attack and recover MP")
                        heroMP += 20  # menambah MP hero
                        heroDmg = 10
                        # send dmg to enemy profile
                        sP.pacifistaProfile(heroDmg)
                        heroHP -= sP.dmgSend
                        if heroHP < 0:
                            heroHP -= heroHP
                        print(hero['name'], heroHP, heroMP)
                        pacifista(heroHP, heroMP)
                elif MPs == 4:
                    if heroMP >= 200:
                        print("hero attack with 200 MP")
                        heroMP -= 200
                        heroDmg = 200
                        dmgToPaci.append(heroDmg)
                        # send dmg to enemy profile
                        sP.pacifistaProfile(heroDmg)
                        heroHP -= sP.dmgSend
                        if heroHP < 0:
                            heroHP -= heroHP
                        print(hero['name'], heroHP, heroMP)
                        pacifista(heroHP, heroMP)
                    else:
                        print(
                            "Because Low MP, hero attack with basic attack and recover MP")
                        heroMP += 20  # menambah MP hero
                        heroDmg = 10
                        # send dmg to enemy profile
                        sP.pacifistaProfile(heroDmg)
                        heroHP -= sP.dmgSend
                        if heroHP < 0:
                            heroHP -= heroHP
                        print(hero['name'], heroHP, heroMP)
                        pacifista(heroHP, heroMP)
            else:
                print("hero out of MP, can't fight anymore")
                heroHP -= heroHP
                pacifista(heroHP, heroMP)
        else:
            print("hero lose")
            sys.exit(0)
    else:
        sP.enemyHP -= sP.enemyHP  # Anti Minus
        print("I win and my HP is", heroHP,
              "and my MP is", heroMP)
        time.sleep(3)


paci = pacifista


def dofflaminggo(heroHP, heroMP):  # Doflaminggo
    global heroDmg  # deklarasi global
    if DS.enemyHP > 0:
        if heroHP > 0:
            if heroMP > 0:
                MPs = random.randint(1, 4)
                if MPs == 1:
                    if heroMP >= 80:
                        print("hero attack with 80 MP")
                        heroMP -= 80
                        heroDmg = 80
                        dmgToDoffy.append(heroDmg)
                        # send dmg to enemy profile
                        DS.dofflaminggoProfile(heroDmg)
                        heroHP -= DS.dmgSend
                        if heroHP < 0:
                            heroHP -= heroHP
                        print(hero['name'], heroHP, heroMP)
                        dofflaminggo(heroHP, heroMP)
                    else:
                        print(
                            "Because Low MP, hero attack with basic attack and recover MP")
                        heroMP += 20  # menambah MP hero
                        heroDmg = 10
                        DS.dofflaminggoProfile(heroDmg)
                        heroHP -= DS.dmgSend
                        if heroHP < 0:
                            heroHP -= heroHP
                        print(hero['name'], heroHP, heroMP)
                        dofflaminggo(heroHP, heroMP)
                if MPs == 2:
                    if heroMP >= 90:
                        print("hero attack with 90 MP")
                        heroMP -= 90
                        heroDmg = 90
                        dmgToDoffy.append(heroDmg)
                        # send dmg to enemy profile
                        DS.dofflaminggoProfile(heroDmg)
                        heroHP -= DS.dmgSend
                        if heroHP < 0:
                            heroHP -= heroHP
                        print(hero['name'], heroHP, heroMP)
                        dofflaminggo(heroHP, heroMP)
                    else:
                        print(
                            "Because Low MP, hero attack with basic attack and recover MP")
                        heroMP += 20  # menambah MP hero
                        heroDmg = 10
                        DS.dofflaminggoProfile(heroDmg)
                        heroHP -= DS.dmgSend
                        if heroHP < 0:
                            heroHP -= heroHP
                        print(hero['name'], heroHP, heroMP)
                        dofflaminggo(heroHP, heroMP)
                if MPs == 3:
                    if heroMP >= 100:
                        print("hero attack with 100 MP")
                        heroMP -= 100
                        heroDmg = 100
                        dmgToDoffy.append(heroDmg)
                        # send dmg to enemy profile
                        DS.dofflaminggoProfile(heroDmg)
                        heroHP -= DS.dmgSend
                        if heroHP < 0:
                            heroHP -= heroHP
                        print(hero['name'], heroHP, heroMP)
                        dofflaminggo(heroHP, heroMP)
                    else:
                        print(
                            "Because Low MP, hero attack with basic attack and recover MP")
                        heroMP += 20  # menambah MP hero
                        heroDmg = 10
                        DS.dofflaminggoProfile(heroDmg)
                        heroHP -= DS.dmgSend
                        if heroHP < 0:
                            heroHP -= heroHP
                        print(hero['name'], heroHP, heroMP)
                        dofflaminggo(heroHP, heroMP)
                if MPs == 4:
                    if heroMP >= 200:
                        print("hero attack with 200 MP")
                        heroMP -= 200
                        heroDmg = 200
                        dmgToDoffy.append(heroDmg)
                        # send dmg to enemy profile
                        DS.dofflaminggoProfile(heroDmg)
                        heroHP -= DS.dmgSend
                        if heroHP < 0:
                            heroHP -= heroHP
                        print(hero['name'], heroHP, heroMP)
                        dofflaminggo(heroHP, heroMP)
                    else:
                        print(
                            "Because Low MP, hero attack with basic attack and recover MP")
                        heroMP += 20  # menambah MP hero
                        heroDmg = 10
                        DS.dofflaminggoProfile(heroDmg)
                        heroHP -= DS.dmgSend
                        if heroHP < 0:
                            heroHP -= heroHP
                        print(hero['name'], heroHP, heroMP)
                        dofflaminggo(heroHP, heroMP)
            else:
                print("hero out of MP, can't fight anymore")
                heroHP -= heroHP
                dofflaminggo(heroHP, heroMP)
        else:
            print("hero lose")
            sys.exit(0)
    else:
        DS.enemyHP -= DS.enemyHP
        print("I win and my HP is", heroHP,
              "and my MP is", heroMP)
        time.sleep(3)


doffy = dofflaminggo


def bigMom(heroHP, heroMP):  # bigMOM
    global heroDmg  # deklarasi global
    print("1. Skill\n2. Basic")
    if WCI.enemyHP > 0:
        if heroHP > 0:
            if heroMP > 0:
                # MPs = int(input("Silahkan Masukkan pilihan [1,2]"))
                MPs = random.randint(1, 5)
                if MPs == 1:
                    if heroMP >= 80:
                        print("hero attack with 80 MP")
                        heroMP -= 80  # mengurangi MP hero
                        heroDmg = 80  # mendeklarasi dmg untuk musuh
                        dmgToBigMom.append(heroDmg)
                        WCI.bogMomProfile(heroDmg)  # send dmg to enemy profile
                        heroHP -= WCI.dmgSend  # mengurangi darah hero
                        if heroHP < 0:
                            heroHP -= heroHP  # anti minus HP
                        # print status hero
                        print(hero['name'], heroHP, heroMP)
                        # memanggil method hero kembali dengan
                        # status yang sudah di perbaharui
                        bigMom(heroHP, heroMP)
                    else:
                        print(
                            "Because Low MP, hero attack with basic attack and recover MP")
                        heroMP += 20  # menambah MP hero
                        heroDmg = 10
                        WCI.bogMomProfile(heroDmg)
                        heroHP -= DS.dmgSend
                        if heroHP < 0:
                            heroHP -= heroHP
                        print(hero['name'], heroHP, heroMP)
                        bigMom(heroHP, heroMP)
                elif MPs == 2:
                    if heroMP >= 90:
                        print("hero attack with 90 MP")
                        heroMP -= 90  # mengurangi MP hero
                        heroDmg = 90  # mendeklarasi dmg untuk musuh
                        dmgToBigMom.append(heroDmg)
                        WCI.bogMomProfile(heroDmg)  # send dmg to enemy profile
                        heroHP -= WCI.dmgSend  # mengurangi darah hero
                        if heroHP < 0:
                            heroHP -= heroHP  # anti minus HP
                        # print status hero
                        print(hero['name'], heroHP, heroMP)
                        # memanggil method hero kembali dengan
                        # status yang sudah di perbaharui
                        bigMom(heroHP, heroMP)
                    else:
                        print(
                            "Because Low MP, hero attack with basic attack and recover MP")
                        heroMP += 20  # menambah MP hero
                        heroDmg = 10
                        WCI.bogMomProfile(heroDmg)
                        heroHP -= DS.dmgSend
                        if heroHP < 0:
                            heroHP -= heroHP
                        print(hero['name'], heroHP, heroMP)
                        bigMom(heroHP, heroMP)
                elif MPs == 3:
                    if heroMP >= 100:
                        print("hero attack with 100 MP")
                        heroMP -= 100  # mengurangi MP hero
                        heroDmg = 100  # mendeklarasi dmg untuk musuh
                        dmgToBigMom.append(heroDmg)
                        WCI.bogMomProfile(heroDmg)  # send dmg to enemy profile
                        heroHP -= WCI.dmgSend  # mengurangi darah hero
                        if heroHP < 0:
                            heroHP -= heroHP  # anti minus HP
                        # print status hero
                        print(hero['name'], heroHP, heroMP)
                        # memanggil method hero kembali dengan
                        # status yang sudah di perbaharui
                        bigMom(heroHP, heroMP)
                    else:
                        print(
                            "Because Low MP, hero attack with basic attack and recover MP")
                        heroMP += 20  # menambah MP hero
                        heroDmg = 10
                        WCI.bogMomProfile(heroDmg)
                        heroHP -= DS.dmgSend
                        if heroHP < 0:
                            heroHP -= heroHP
                        print(hero['name'], heroHP, heroMP)
                        bigMom(heroHP, heroMP)
                elif MPs == 4:
                    if heroMP >= 200:
                        print("hero attack with 200 MP")
                        heroMP -= 200  # mengurangi MP hero
                        heroDmg = 200  # mendeklarasi dmg untuk musuh
                        dmgToBigMom.append(heroDmg)
                        WCI.bogMomProfile(heroDmg)  # send dmg to enemy profile
                        heroHP -= WCI.dmgSend  # mengurangi darah hero
                        if heroHP < 0:
                            heroHP -= heroHP  # anti minus HP
                        # print status hero
                        print(hero['name'], heroHP, heroMP)
                        # memanggil method hero kembali dengan
                        # status yang sudah di perbaharui
                        bigMom(heroHP, heroMP)
                    else:
                        print(
                            "Because Low MP, hero attack with basic attack and recover MP")
                        heroMP += 20  # menambah MP hero
                        heroDmg = 10
                        WCI.bogMomProfile(heroDmg)
                        heroHP -= DS.dmgSend
                        if heroHP < 0:
                            heroHP -= heroHP
                        print(hero['name'], heroHP, heroMP)
                        bigMom(heroHP, heroMP)
                elif MPs == 5:
                    print("hero attack with basic attack and recover 20 MP")
                    heroMP += 20  # menambah MP hero
                    heroDmg = 10  # mendeklarasi dmg untuk musuh
                    dmgToBigMom.append(heroDmg)
                    WCI.bogMomProfile(heroDmg)  # send dmg to enemy profile
                    if WCI.enemyHP <= 0:  # cek dara musuh, jika darah musuh 0 maka selesai
                        WCI.enemyHP -= WCI.enemyHP  # anti minus
                        print("I win and my HP is", heroHP,
                              "and my MP is", heroMP)
                        time.sleep(5)
                    elif heroHP > 0:
                        heroHP -= WCI.dmgSend  # mengurangi darah hero
                        if heroHP < 0:
                            heroHP -= heroHP  # anti minus HP
                        # print status hero
                        print(hero['name'], heroHP, heroMP)
                        # memanggil method hero kembali dengan
                        # status yang sudah di perbaharui
                        bigMom(heroHP, heroMP)
            else:
                print("hero out of MP, can't fight anymore")
                heroHP -= heroHP
        else:
            print("hero lose")
            sys.exit(0)
    else:
        WCI.enemyHP -= WCI.enemyHP
        print("I win and my HP is", heroHP,
              "and my MP is", heroMP)
        time.sleep(3)


Mom = bigMom

SL.one()
import alabasta
SL.two()
paci(heroHP, heroMP)
dB.pacifista(dmgToPaci)
import sabaodyKizaru 
SL.two5()
SL.three()
doffy(heroHP, heroMP)
dB.doffy(dmgToDoffy)
SL.four()
print("1.lanjut\n2.menyelamatkan teman")
a = int(input("Jawabanmu : "))
if a  == 1 :
    print("menuju wano....")
    time.sleep(5)
    print("dan luffy di cap tidak setia kawan")
    time.sleep(5)
    print("Cerita berakhir")
    sys.exit(0)
else:
    time.sleep(5)
    print("luffy pergi menyelamatkan temenya")
    time.sleep(5)
SL.five()
Mom(heroHP, heroMP)
dB.bigMom(dmgToBigMom)
SL.six()
