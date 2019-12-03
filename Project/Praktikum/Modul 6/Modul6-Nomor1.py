import skimage.io as io
from copy import deepcopy
import matplotlib.pyplot as plt

img = io.imread(r'D:/Python/Project/Praktikum/Modul 6/a.jpg')

red = deepcopy(img)
green = deepcopy(img)
blue = deepcopy(img)

red[:, :, 1] = 0
red[:, :, 2] = 0
green[:, :, 0] = 0
green[:, :, 2] = 0
blue[:, :, 0] = 0
blue[:, :, 1] = 0

fig, ax = plt.subplots(ncols=2, nrows=2)

ax[0, 0].imshow(img)
ax[0, 0].set_title('ori')
ax[0, 0].axis('off')
ax[0, 1].imshow(red)
ax[0, 1].set_title('red')
ax[0, 1].axis('off')
ax[1, 0].imshow(green)
ax[1, 0].set_title('green')
ax[1, 0].axis('off')
ax[1, 1].imshow(blue)
ax[1, 1].set_title('blue')
ax[1, 1].axis('off')

plt.show()