import random, sys


def enemyProfile(dmgRecived):
    global enemyHP, enemyMP
    enemyHP -= dmgRecived
    enemyRemHP = enemyHP
    alabasta(heroHP, enemyRemHP, enemyMP, dmgRecived)
    enemyMP -= dmgSend
    enemyRemMP = enemyMP
    return enemyHP, enemyMP



def alabasta(heroHP, enemyHP, enemyMP, dmgRecived):
    global dmgSend
    if heroHP > 0:
        if enemyHP > 0:
            if enemyMP > 0:
                MPs = 1  # random.randint(1, 5)
                if MPs == 1:
                    if enemyMP >= 10:
                        print("enemy attack with 10 MP")
                        dmgSend = 10
                        print("Enemy", enemyHP, enemyMP)
                    else:
                        print("enemy Failed attack because low MP")
            else:
                print("Enemy out of MP, can't fight anymore")
                enemyHP -= enemyHP
        else:
            print("I Lose")
    return dmgSend, enemyMP


def luffy(heroHP, heroMP):
    global heroDmg
    if heroHP > 0:
        if heroMP > 0:
            MPs = 1  # random.randint(1, 5)
            if MPs == 1:
                if heroMP >= 10:
                    print("hero attack with 10 MP")
                    heroMP -= 10
                    heroDmg = 10
                    enemyProfile(heroDmg) # send dmg to enemy profile
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
global dmgSend, heroDmg
heroDmg = dmgSend = 0

# enemy Profile
global enemyHP, enemyMP
enemyHP = enemyMP = 100

# hero Profile
global heroHP, heroMP
heroHP = heroMP = 100

luffy(heroHP, heroMP)
