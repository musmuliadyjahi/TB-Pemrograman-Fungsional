import random


def dofflaminggoProfile(dmgRecived):
    global enemyHP, enemyMP, enemyHPR, enemyMPR
    enemyHP -= dmgRecived
    enemyRemHP = enemyHP
    dofflaminggo(enemyRemHP, enemyMP)
    enemyMP -= dmgSend
    enemyRemMP = enemyMP
    if enemyHPR > 0:
        enemyHP += enemyHPR  # Heal HP musuh
        enemyHPR = 0

    if enemyMPR > 0:
        enemyMP += enemyMPR  # Heal MP musuh
        enemyMPR = 0
    return enemyHP, enemyMP


def dofflaminggo(enemyHP, enemyMP):
    global dmgSend, enemyMPR, enemyHPR
    if enemyHP > 0:
        if enemyMP > 0:
            MPs = random.randint(1, 3)
            if MPs == 1:
                if enemyMP >= 10:
                    print("terima ini....!!!! Parasite !!!!")
                    dmgSend = 10
                    enemyMPR = enemyHPR = 0
                    print("Enemy", enemyHP, enemyMP)
                else:
                    print("enemy Failed attack because low MP")
            elif MPs == 2:
                if enemyMP >= 20:
                    print("terima ini....!!!! Overheat !!!!")
                    dmgSend = 20
                    enemyMPR = enemyHPR = 0
                    print("Enemy", enemyHP, enemyMP)
            elif MPs == 3:
                print("aku harus segera memulihkan keadaanku...Sufaku Agyo")
                dmgSend = 0
                enemyMPR = 5
                enemyHPR = 10
                print("Enemy", enemyHP, enemyMP)
        else:
            print("Enemy out of MP, can't fight anymore")
            enemyHP -= enemyHP
    else:
        print("Dofflaminggo Kalah")
        print("Dofflaminggopun mencari tau sipa luffy sebenarnya")
        student = {'nama': 'luffy', 'age': '19',
                   'status': 'jomblo', 'nama ayah': 'dragon'}
        # for key in student :
        #    print (key)
        print('========================')
        for key, value in student.items():
            print(key, value)
        print("doffy pun mengetahui siapa luffy sebenarnya")
        # time.sleep(4)
        print("dia ingin mengetahui berapa jumlah krunya")
        list_a = [1, 2, 3, 4, 5]
        # filter object <filter at 0x4e45890>
        filter_obj = filter(lambda x: x > 4, list_a)

        even_num = list(filter_obj)  # Converts the filer obj to a list

        print("dan jumlah krunya adalah", even_num)
    return dmgSend, enemyMPR, enemyMP, enemyHPR


#global profile
global dmgSend, heroDmg, enemyMPR, enemyHPR
heroDmg = dmgSend = enemyMPR = enemyHPR = 0

# enemy Profile
global enemyHP, enemyMP
enemyHP = enemyMP = 1000
