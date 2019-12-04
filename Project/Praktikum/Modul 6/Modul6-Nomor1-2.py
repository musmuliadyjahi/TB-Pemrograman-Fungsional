import cv2
import numpy as np

img = cv2.imread(r'D:/Python/Project/Praktikum/Modul 6/a.jpg')
print(img.shape)
percent = 30  # skala persen untuk resize gambar
w = int(img.shape[1]*percent/100)  # ukuran lebar
h = int(img.shape[0]*percent/100)  # ukuran tinggi
dim = (w, h)
resized = cv2.resize(img, dim)  # proses resize gambar
cv2.imshow('original image', resized)  # menampilkan gambar original
cv2.waitKey(0)  # tunggu hingga di close
row, col, plane = img.shape  # menyimpan ukuran gambar
# create a zero matrix of order same as
# original image matrix order of same dimension
temp = np.zeros((row, col, plane), np.uint8)
print(len(temp[0][0]))
# store blue plane contents or data of image matrix
# to the corresponding plane(blue) of temp matrix
temp[:, :, 0] = img[:, :, 0]
resized = cv2.resize(temp, dim)
cv2.imshow('Blue plane image', resized)
cv2.waitKey(0)
temp = np.zeros((row, col, plane), np.uint8)
temp[:, :, 1] = img[:, :, 1]
resized = cv2.resize(temp, dim)
cv2.imshow('Green plane image', resized)
cv2.waitKey(0)
temp = np.zeros((row, col, plane), np.uint8)
temp[:, :, 2] = img[:, :, 2]
resized = cv2.resize(temp, dim)
cv2.imshow('Red plane image', resized)
cv2.waitKey(0)
