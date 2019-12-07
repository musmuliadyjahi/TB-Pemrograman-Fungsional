import random
import sys


def pacifistaProfile(dmgRecived):
    global enemyHP, enemyMP, dodge
    if dodge == 0:
        dmgRecived = 0
        enemyHP -= dmgRecived
        print("Evade")
        dodge = 3
    elif dodge > 0:
        enemyHP -= dmgRecived
        dodge -= 1
    enemyRemHP = enemyHP
    pacifista(enemyRemHP, enemyMP)
    if enemyMP > 0:
        enemyMP -= dmgSend  # mengurangi MP musuh
        enemyRemMP = enemyMP  # mendeklarasi MP musuh ke lokal
    else:
        print("Enemy out of MP, can't fight anymore")
        enemyHP -= enemyHP
    if enemyHP <0 : #anti minus HP
        enemyHP -= enemyHP
    print("Enemy", enemyHP, enemyMP)
    return enemyHP, enemyMP


def pacifista(enemyHP, enemyMP):
    global dmgSend
    # global heroHP
    if enemyHP > 0:
        if enemyMP > 0:
            MPs = random.randint(1, 4)
            if MPs == 1:
                if enemyMP >= 10:
                    print("Pacifista attack with Basic Attack")
                    dmgSend = 10
            elif MPs == 2:
                if enemyMP >= 15:
                    print("Pacifista attack with Laser Beam")
                    dmgSend = 15
            elif MPs == 3:
                if enemyMP >= 20:
                    print("Pacifista attack with Super Punch Steel")
                    dmgSend = 20
            elif MPs == 4:
                if enemyMP >= 50:
                    print("Pacifista attack with Special attack")
                    dmgSend = 100
                else:
                    print("enemy Failed attack because MP is low")
    else:
        print("I Lose -Pacifista")
    return dmgSend, enemyMP


#global profile
global dmgSend, dodge
dmgSend = 0
dodge = 3

# enemy Profile
global enemyHP, enemyMP
enemyHP = enemyMP = 1000
