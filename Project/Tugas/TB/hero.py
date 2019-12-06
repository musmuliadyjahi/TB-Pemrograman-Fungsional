import sys
import time
import random
import pygame
import wholeCakeIsland as WCI
import dressrosa as DS
import sabaodyPacifista as sP
from PIL import Image

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
                        time.sleep(5)
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
                        time.sleep(5)
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
                            time.sleep(5)
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
                            time.sleep(5)
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
pygame.mixer.music.load("./Backsound/Luffy Berhasil.mp3")

pygame.mixer.music.play()
print("Luffy beserta team pergi berlayar sebagai seorang bajak laut untuk menemukan one piece dan menjadi raja bajak laut.")
time.sleep(8)
print("Sampailah dia di sebuah negeri yang bernama alabasta")
time.sleep(5)
pygame.mixer.music.stop()
pygame.mixer.music.load("./Backsound/Luffy Fighting.mp3")
pygame.mixer.music.play()
print("negeri itu sedang berada dalam masalah karna seseorang yang bernama crocodile menguasai negeri itu dari bayang-bayang. Untuk membebaskan negeri itu luffy pun melawannya.")
time.sleep(10)

print("Musuh : Crocodile")
img = Image.open("./Pict/Dofflaminggo.jpeg")
img.show()
time.sleep(5)
import alabasta
time.sleep(5)
print("Luffy pun dapat membebaskan negeri itu dan melanjutkan perjalanannya untuk mencari one piece.")
time.sleep(10)
print("Sampailah dia di negeri selanjutnya yaitu sambody. Di pulau itu dia mendapat masalah dari Admiral Kizaru dan Pacifista.")
time.sleep(10)
print("Musuh : Pacifista & kizaru")
time.sleep(5)
pacifista(heroHP, heroMP)
import sabaodyKizaru
print("Dia pun kalah telak tapi dia tidak menyerah hingga dia dilatih oleh seorang legenda hidup, salah satu dari kru bajak laut sebelumnya yaitu Reyleg.")
time.sleep(10)
print("Setelah dia selesai pembelajarannya dan melanjutkan perjalanannya, dia kembali berhadapan dengan masalah di pulau dresarosa, dia bertempur melawan Doflaminggo.")
dofflaminggo(heroHP, heroMP)
print("Setelah itu,")
time.sleep(10)
print("dia pergi berlayar lagi namun dia di hadapi oleh sebuah pilihan yaitu mau ke wano atau menyelamatkan temannya di Whole Cake Island.")

a = int(input("1.lanjut\n2.menyelamatkan teman"))
if a  == 1 :
    print("menuju wano dan luffy di cap tidak setia kawan")
    print("Cerita berakhir")
    sys.exit(0)
else:
    print("luffy pergi menyelamatkan temenya")


print("Luffy berhasil menyelamatkan temannya namun Bigmom sang penguasa Whole Cake Island tidak mau melepaskannya diapun dikejar dan akhirnya terjadilah berhadap-hadapan.")
time.sleep(10)
bigMom(heroHP, heroMP)
time.sleep(10)
print("Akhirnya luffy pun berhasil menyelamatkan temannya dan mereka kembali berlayar menuju wano dan melanjutkan pencariannya menujur one piece.")