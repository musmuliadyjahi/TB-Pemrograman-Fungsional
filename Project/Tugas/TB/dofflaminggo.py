import random, sys


def enemyProfile(dmgRecived):
    global enemyHP, enemyMP
    enemyHP -= dmgRecived
    enemyRemHP = enemyHP
    dressrosa(heroHP, enemyRemHP, enemyMP, dmgRecived)
    enemyMP -= dmgSend
    enemyRemMP = enemyMP
    enemyMP +=enemyMPR
    enemyHP+=enemyHPR
    
    return enemyHP, enemyMP



def dressrosa(heroHP, enemyHP, enemyMP, dmgRecived):
    global dmgSend,enemyMPR,enemyHPR
    # global heroHP
    if heroHP > 0:
        if enemyHP > 0:
            if enemyMP > 0:
                MPs =random.randint(1,3)
                if MPs == 1:
                    if enemyMP >= 10:
                        print("terima ini....!!!! Parasite !!!!")
                        dmgSend = 10
                        enemyMPR= 0
                        enemyHPR=0
                        print("Enemy", enemyHP, enemyMP)
                    else:
                        print("enemy Failed attack because low MP")
                elif MPs == 2:
                     if enemyMP >= 20:
                         print("terima ini....!!!! Overheat !!!!")
                         dmgSend = 20
                         enemyMPR= 0
                         enemyHPR=0
                         print("Enemy", enemyHP, enemyMP)
                elif MPs == 3:
                     print("aku harus segera memulihkan keadaanku...Sufaku Agyo" )
                     dmgSend=0
                     enemyMPR = 5
                     enemyHPR = 10
                     print("Enemy", enemyHP, enemyMP)
            else:
                print("Enemy out of MP, can't fight anymore")
                enemyHP -= enemyHP
        else:
            print("I Lose")
    return dmgSend, enemyMPR,enemyMP,enemyHPR


def luffy(heroHP, heroMP):
    global heroDmg
    if heroHP > 0:
        if heroMP > 0:
            MPs = 1  # random.randint(1, 5)
            if MPs == 1:
                if heroMP >= 20:
                    print("hero attack with 20 MP")
                    heroMP -= 20
                    heroDmg = 20
                    # send dmg to enemy profile
                    enemyProfile(heroDmg)
                    if enemyHP == 0:
                        print("I win and my HP is", heroHP, "and my MP is", heroMP)
                        sys.exit(0)
                    else:
                        heroHP -= dmgSend
                        print("hero", heroHP, heroMP)
                        luffy(heroHP, heroMP)
                else:
                    print("hero Failed attack because low MP")
        else:
            print("hero out of MP, can't fight anymore")
            heroHP -= heroHP
    else:
        print("hero lose")


#global profile
global dmgSend, heroDmg,enemyMPR,enemyHPR
heroDmg = dmgSend = enemyMPR=enemyHPR=0

# enemy Profile
global enemyHP, enemyMP
enemyHP = enemyMP = 100

# hero Profile
global heroHP, heroMP
heroHP = heroMP = 100

luffy(heroHP, heroMP)
