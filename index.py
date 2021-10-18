from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
msg='Niladri Samanta'
W, H = (1120,300)
font = ImageFont.truetype('arial.ttf',60)
img = Image.open('My Post.jpg')
draw = ImageDraw.Draw(img)
w, h = draw.textsize(msg)
draw.text(((W-w)/2,335),text='{}'.format(msg),fill=(0,0,0),font=font,anchor="mm",stroke_width=1,stroke_fill="black")
img.show()