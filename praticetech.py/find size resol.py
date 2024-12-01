import PIL
from PIL import Image

img=PIL.Image.open("C:\Users\aksha\Desktop\pictures")

width,height=img.size
print(width,"*",height)