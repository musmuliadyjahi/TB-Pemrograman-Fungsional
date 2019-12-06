from PIL import Image

# convert ke garayscale
img = Image.open("D:/Python/Project/Praktikum/Modul 6/a.jpg").convert('L')
# im.draft("L", (im.width // 3, im.height // 3))
img.show()
