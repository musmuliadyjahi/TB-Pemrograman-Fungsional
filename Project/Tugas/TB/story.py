import time
import pygame
import cv2
from PIL import Image

def one():
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
    cv2.waitKey(0)

def two():
    time.sleep(5)
    print("Luffy pun dapat membebaskan negeri itu dan melanjutkan perjalanannya untuk mencari one piece.")
    time.sleep(10)
    print("Sampailah dia di negeri selanjutnya yaitu sambody. Di pulau itu dia mendapat masalah dari Admiral Kizaru dan Pacifista.")
    time.sleep(10)
    print("Musuh : Pacifista & kizaru")
    time.sleep(5)

def three():
    print("Dia pun kalah telak tapi dia tidak menyerah hingga dia dilatih oleh seorang legenda hidup, salah satu dari kru bajak laut sebelumnya yaitu Reyleg.")
    time.sleep(10)
    print("Setelah dia selesai pembelajarannya dan melanjutkan perjalanannya")
    time.sleep(5)
    print("dia kembali berhadapan dengan masalah di pulau dresarosa, dia bertempur melawan Doflaminggo.")
    time.sleep(6)

def four():
    print("Setelah itu,")
    time.sleep(5)
    print("dia pergi berlayar lagi namun dia di hadapi oleh sebuah pilihan yaitu mau ke wano atau menyelamatkan temannya di Whole Cake Island.")

def five():
    print("Luffy berhasil menyelamatkan temannya.")
    time.sleep(5)
    print("Namun Bigmom sang penguasa Whole Cake Island tidak mau melepaskannya diapun dikejar dan akhirnya terjadilah berhadap-hadapan.")
    time.sleep(10)

def six():
    time.sleep(10)
    print("Akhirnya luffy pun berhasil menyelamatkan temannya dan mereka kembali berlayar menuju wano dan melanjutkan pencariannya menujur one piece.")