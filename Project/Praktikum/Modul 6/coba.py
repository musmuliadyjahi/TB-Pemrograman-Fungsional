from PIL import Image

# convert ke garayscale
img = Image.open("D:/Python/Project/Praktikum/Modul 6/a.jpg").convert('L')
# im.draft("L", (im.width // 3, im.height // 3))
WIDTH, HEIGHT = img.size
data = list(img.getdata())
data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]
for row in data:
    print(' '.join('{:3}'.format(value) for value in row))

chars = '@%#*+=-:. '  # Change as desired.
scale = (len(chars)-1)/255.
print()
for row in data:
    print(' '.join(chars[int(value*scale)] for value in row))
# im.show()
