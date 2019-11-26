#Judul = "Hikayat Kancil"
import random
import time
import os
import sys
from functools import partial


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def title():
    print("===========================================================")
    print("============= Kisah Si Kancil Pencuri Timun ===============")
    print("===========================================================")

# Tujuan


def north():
    print("tekan n untuk pergi ke hutan")


def east():
    print("tekan e untuk pergi ke sungai")


def south():
    print("tekan s untuk pergi ke jalan raya")


def west():
    print("tekan w untuk pergi ke gurun")

# Profile


def setup():

    global name
    global HP
    global MP

    name = input("Siapa nama kancilnya? ")

    HP = random.randint(20, 30)
    MP = random.randint(5, 20)


def status():

    print("Sedang Mengecek Status si Kancil, " + name)
    time.sleep(2)
    print("si Kancil, "+name + " masih punya " +
          " " + str(HP) + " " + "Total Darah")


def multiply(x, y):
    return x * y

# Enemy


def lastenemy():
    global enemyHP
    global enemyMP
    global lastenm
    enemyHP = random.randint(5, 10)
    enemyMP = random.randint(5, 10)

    lastenm = "Anjing"
    print("Sedang Mengecek Status si "+lastenm)
    time.sleep(2)
    print(lastenm + "nya punya " + " " + str(enemyHP) + " " + "Total Darah")
    print(lastenm + "nya punya " + " " + str(enemyMP) + " " + "Total Stamina")


def enemy():
    global enemyHP
    global enemyMP
    global enemynames
    enemyHP = random.randint(5, 20)
    enemyMP = random.randint(5, 20)

    enemyname = "Buaya"
    print("\nDatang Seekor Hewan "+enemyname+" Datang Ingin Memakanmu....")
    time.sleep(2)
    print("Sedang Mengecek Status si "+enemyname)
    time.sleep(2)
    print(enemyname + "nya punya " + " " + str(enemyHP) + " " + "Total Darah")
    print(enemyname + "nya punya " + " " +
          str(enemyMP) + " " + "Total Stamina")


def enemy2():
    global enemyHP
    global enemyMP
    global enemyname2
    enemyHP = random.randint(5, 20)
    enemyMP = random.randint(5, 20)

    enemyname2 = "Robot"
    print("\nDatang Sebuah "+enemyname2+" Datang Ingin Menghancurkanmu....")
    time.sleep(2)
    print("Sedang Mengecek Status si "+enemyname2)
    time.sleep(2)
    print(enemyname2 + "nya punya " + " " + str(enemyHP) + " " + "Total Darah")
    print(enemyname2 + "nya punya " + " " +
          str(enemyMP) + " " + "Total Stamina")


def enemy3():
    global enemyHP
    global enemyMP
    global enemyname3
    enemyHP = random.randint(5, 20)
    enemyMP = random.randint(5, 20)

    enemyname3 = "Kala njengking"
    print("\nDatang Seekor "+enemyname3+" Datang Ingin Memakanmu....")
    time.sleep(2)
    print("Sedang Mengecek Status si "+enemyname3)
    time.sleep(2)
    print(enemyname3 + "nya punya " + " " + str(enemyHP) + " " + "Total Darah")
    print(enemyname3 + "nya punya " + " " +
          str(enemyMP) + " " + "Total Stamina")


def death():
    print("\nYah, Si Kancil, "+name+" Mati")
    time.sleep(2)
    print("Game Over")
    time.sleep(2)
    sys.exit(0)


def farmer():

    global npcname
    global response

    responses = ["Sedang apa kamu disini?", "Mau ngapain?",
                 "Ada yang bisa saya bantu?", "Ada Apa ya?"]
    npcname = "Pak Tani"
    print("\n["+npcname+":] Halo, Aku"+npcname +
          ", Apakah kamu mau bicara dengan ku?(y/n)")

    random.shuffle(responses)
    if input() == "y":
        print("["+npcname+":] " + responses[0])
        time.sleep(2)
        list_answer = ["Saya ingin mencuri mentimun", "Bolehkah saya mengambil mentimun?",
                       "Saya numpang lewat saja", "Apa urusan pak tani menanyakan hal itu?"]
        print("0. Saya Ingin Mencuri Mentimun")
        print("1. Bolehkah saya mengambil mentimun?")
        print("2. Saya numpang lewat saja")
        print("3. Apa urusan pak tani menanyakan hal itu?")
        answer = input("Respon?[(0,1,2,3)/n]")
        if answer == '0':
            print(list_answer[0])
            time.sleep(2)
            print("["+npcname+":] Hmm, beraninya kamu")
            time.sleep(2)
            print("DOORR")
            print("========== - - - >")
            print("| )")
            print("--")
            death()
        elif answer == '1':
            time.sleep(2)
            print("["+npcname+":] Hmm.....")
            time.sleep(2)
            print("["+npcname+":] Boleh,")
            time.sleep(2)
            print("["+npcname+":] Hanya dengan satu syarat!!!")
            time.sleep(2)
            resp = input("Terima tantangan? (y/n) : ")
            if resp == 'y':
                laststory()
            else:
                print("["+npcname+":] Kalau Begitu Silahkan Pergi!!!")
                time.sleep(2)
                print(
                    "Si Kancil Tidak Memilih Untuk Mencuri Timun, Karena Takut Sama Pak Tani.")
                time.sleep(2)
                print("Game Over")
                time.sleep(2)
                sys.exit(0)
        elif answer == '2':
            print(list_answer[2])
            time.sleep(2)
            print("["+npcname+":] Owh, Oke silahkan lewat")
            time.sleep(2)
            print(".")
            time.sleep(2)
            print(".")
            time.sleep(2)
            print(".")
            time.sleep(2)
            print("Yasudah, si kancil cuma lewat kan :v")
            time.sleep(2)
            sys.exit(0)
        elif answer == '3':
            print(list_answer[3])
            time.sleep(2)
            print("["+npcname+":] Hmm, beraninya kamu")
            time.sleep(2)
            print("DOORR")
            print("========== - - - >")
            print("| )")
            print("--")
            death()
        time.sleep(2)

    else:
        print("["+npcname+":] Kalau Begitu Silahkan Pergi!!!")
        time.sleep(2)
        print("Si Kancil Tidak Memilih Untuk Mencuri Timun, Karena Takut Sama Pak Tani.")
        time.sleep(2)
        print("Game Over")
        time.sleep(2)
        sys.exit(0)


def laststory():
    print("Setelah si kancil, "+name +
          " memutuskan untuk menerima tantangan dari pak Tani, ")
    time.sleep(3)
    print("pak Tani menjelaskan, di luar sana terdapat sebuah GUA yang tersimpan harta karun")
    time.sleep(3)
    print("si kancil di tugas kan untuk mendapatkan harta karun tersebut")
    time.sleep(3)
    print("karena pak Tani baik hati, dia memberikan si Kacil berupa hadiah")
    time.sleep(3)
    print("___  ___   ___   ___   ___")
    print("|#|  |#|   |#|   |#|   |#|")
    print(" 1    2     3     4     5 ")
    print("[Pak Tani:] Silahkan Pilih!! (Hati Hati, ada yang Bad & Good)")
    time.sleep(3)


# Story Line
weapons = []
weapons.append("Sword")
weapons.append("Knife")
weapons.append("Tongkat Baseball")
weapons.append("Tangan Kosong")
weapons.append("Kayu")
weapons.append("Batu")

dbl = partial(multiply, 2)
print(dbl(random.randint(1, 5)))

clear_screen()
title()
setup()
global name
global HP
global MP
global move
global enemyHP
print("Selamat Datang Kancil Dengan Nama, " + name)

time.sleep(2)

print("\nTotal Darah Mu" + " " + str(HP))
print("Total Stamina Mu" + " " + str(MP))
print("Apakah Kamu Ingin Memulai Perencanaan Untuk Mencuri Timun di Kebun Pak Tani? (y/n)")

if input() == "y":
    print("Pada suatu hari, seperti biasa si kancil sedang bersiap siap memanen timun pak tani")
    time.sleep(3)
    print("Karena kebun petani sangat jauh, maka kancil harus melewati berbagai rintangan")
    time.sleep(3)
else:
    print("Si Kancil Tidak Memilih Untuk Mencuri Timun, Karena Sudah Tobat.")
    time.sleep(2)
    print("Game Over")
    time.sleep(2)
    sys.exit(0)

print("Jauh di utara sana kamu dapat melihat Hutan, di timur terlihat sungai dan barat terdapat gurun.")
time.sleep(3)

print("\n")
north()
east()
west()
south()
move = input("Kemana kamu mau pergi? ")
if move == 'n':
    print("\nKamu telah sampai di Hutan.")
    time.sleep(2)
    print("\nSi Kancil Mencoba Berjalan Memasuki Hutan.")
    time.sleep(3)
    print("\nTiba Tiba.")
    time.sleep(2)
    print("\nDUAAARRRR.")
    time.sleep(1)
    enemy()
elif move == 'e':
    print("\nKamu telah sampai di Sungai.")
    time.sleep(2)
    print("\nSi Kancil Mencoba Berjalan Memasuki Sungai.")
    time.sleep(3)
    print("\nTiba Tiba.")
    time.sleep(2)
    print("\nDUAAARRRR.")
    time.sleep(1)
    enemy()
elif move == 's':
    print("\nKamu telah sampai di Jalan Raya.")
    time.sleep(2)
    print("\nSi Kancil Mencoba Berjalan Memasuki Jalan Raya.")
    time.sleep(3)
    print("\nTiba Tiba.")
    time.sleep(2)
    print("\nDUAAARRRR.")
    time.sleep(1)
    enemy2()
elif move == 'w':
    print("\nKamu telah sampai di Gurun.")
    time.sleep(2)
    print("\nSi Kancil Mencoba Berjalan Memasuki Gurun.")
    time.sleep(3)
    print("\nTiba Tiba.")
    time.sleep(2)
    print("\nDUAAARRRR.")
    time.sleep(1)
    enemy3()

time.sleep(3)

fight = input("Apa kamu ingin bertarung?(y/n)")
weapons = ['Pedang', 'Tongkat Baseball',
           'Pisau', 'Tangan Kosong', 'Kayu', 'Batu']
if fight == "y":
    print(weapons)
    weap = input("Senjata apa yang ingin kamu gunakan?([0,1,2,3,4,5]/n)")
    if weap == '0':
        item = weapons[0]
    elif weap == '1':
        item = weapons[1]
    elif weap == '2':
        item = weapons[2]
    elif weap == '3':
        item = weapons[3]
    elif weap == '4':
        item = weapons[4]
    elif weap == '5':
        item = weapons[5]
    time.sleep(2)
    while enemyHP >= 0:
        enemyhit = random.randint(0, 5)
        print("Giliran Musuhnya Menyerang Mengakibatkan " +
              str(enemyhit) + " Kerusakan ")
        HP = HP - enemyhit
        print("Sisa Nyawa Kancil = " + str(HP))
        time.sleep(2)
        if HP <= 0:
            print("\nYah, Si Kancil, "+name+" Mati")
            time.sleep(2)
            print("Game Over")
            time.sleep(2)
            sys.exit(0)
        else:
            hit = random.randint(0, 5)
            print(name + " Si Kancil Menggunakan  " + item +
                  " Mengakibatkan " + str(hit) + " Kerusakan")
            enemyHP = enemyHP - hit
            print("Sisa Nyawa Musuh = " + str(enemyHP))
            time.sleep(2)
else:
    print("Si Kancil" + name +
          "Memilih untuk melarikan diri, karena merasa lemah dan memilih untuk kembali pulang")
    time.sleep(2)
    print("Game Over")
    time.sleep(2)
    sys.exit(0)

print("HOREE, si Kancil " + name + " Berhasil selamat dari ancaman yang berbahaya")
time.sleep(2)
status()
time.sleep(2)

phase = input("Ingin Melanjutkan Petualangan Ke Rumah Pak Tani?(y/n): ")

if phase == 'y':
    print("\nSetelah Menelusuri Berbagai Area.")
    time.sleep(2)
    print("\nTerlihat di Depan Ada Rumah Pak Tani.")
    time.sleep(2)
    print("\nDirumahnya terdapat banyak sekali Mentimun.")
    time.sleep(2)
    print("\nSi Kancil, "+name+" tanpa keraguan langsung mendatangi kebun tersebut")
    time.sleep(2)
    print("\nTetapi")
    time.sleep(2)
    print("\nKebunnya di jaga Anjing nya pak tani :(")
    time.sleep(2)

    sight = input("\nIngin Melawan?(y/n)")
    if sight == 'y':
        lastenemy()
        time.sleep(2)
        while enemyHP > 0:
            enemyhit = random.randint(0, 5)
            print("Giliran Si Anjing Menyerang Mengakibatkan " +
                  str(enemyhit) + " Kerusakan ")
            HP = HP - enemyhit
            print("Sisa Nyawa Kancil = " + str(HP))
            time.sleep(2)
            if HP <= 0:
                print("\nYah, Si Kancil, "+name+" Mati")
                time.sleep(2)
                print("Game Over")
                time.sleep(2)
                sys.exit(0)
            else:
                hit = random.randint(0, 5)
                print(name + " Si Kancil Menggunakan  " + item +
                      " Mengakibatkan " + str(hit) + " Kerusakan")
                enemyHP = enemyHP - hit
                print("Sisa Nyawa Musuh = " + str(enemyHP))
                time.sleep(2)
    else:
        print("Si Kancil" + name +
              "Memilih untuk melarikan diri, karena merasa lemah dan memilih untuk kembali pulang")
        time.sleep(2)
        print("Game Over")
        time.sleep(2)
        sys.exit(0)
else:
    print("Si Kancil" + name + " mager dan memilih untuk kembali pulang")
    time.sleep(2)
    print("Game Over")
    time.sleep(2)
    sys.exit(0)

print("HOREE, si Kancil " + name + " Berhasil selamat dari anjing yang berbahaya")
time.sleep(2)
status()
time.sleep(2)

print("\n")
print("Setelah si "+name +
      " melawan anjing penjaga kebun pak tani, si kancil pun mencoba mendekati kebunnya")
time.sleep(2)
print("Dan tiba tiba pak tani pun keluar")
farmer()


choose = input("Enaknya ambil yang mana ya? [(1,2,3,4,5)/n] : ")
choose = input("Enaknya ambil yang mana ya? [(1,2,3,4,5)/n] : ")
if (choose == '1' or choose == '2' or choose == '3' or choose == '4' or choose == '5'):
    box = random.randint(1, 5)
    if box == 1:
        print("Anda Mati")
    elif box == 2:
        print("Anda Mati")
    elif box == 3:
        print("Anda Mati")
    elif box == 4:
        print("Anda Mati")
    elif box == 5:
        print("Anda Mati")

f = open("demofile.txt", "rt")

print("Ini Adalah Akhir Dari Kisah Si Kancil, TERIMA KASIH TELAH BERMAIN")
