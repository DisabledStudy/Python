from PIL import Image
img = Image.open('oreilly.png')
print(img.format)
print(img.size)
print(img.mode)

crop = (55,70, 85, 100)
img2 = img.crop(crop)
img2.save('cropped.gif', 'GIF')

img3 = Image.open('cropped.gif')
print(img3.format)
print(img3.size)
