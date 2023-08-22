#!/usr/bin/env python3

from exif import Image

file_path = f'/home/rai/Downloads/balloon-fc416bf4b40d82bcaa2b941bd38a42cd.jpg'

with open(file_path, 'rb') as img_file:
    img = Image(img_file)
    
print(img.has_exif)