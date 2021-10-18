import streamlit as st
import time
import datetime
from datetime import datetime, date, time
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import base64

def get_image_download_link(img):
	"""Generates a link allowing the PIL image to be downloaded
	in:  PIL image
	out: href string
	"""
	buffered = BytesIO()
	img.save(buffered, format="JPEG")
	img_str = base64.b64encode(buffered.getvalue()).decode()
	href = f'<a href="data:file/jpg;base64,{img_str}">Download result</a>'
	return href





msg=st.text_input("Enter name")
st.header("Official Date Picker")
start=st.date_input('start date')
end=st.date_input('end date')
issue=end
W, W1, W2 = (1119,1100,580)
font = ImageFont.truetype('arial.ttf',70)
font2 = ImageFont.truetype('arial.ttf',17)
img = Image.open('My Post.jpg')
draw = ImageDraw.Draw(img)
w, h = draw.textsize(msg)
draw.text(((W-w)/2,335),text='{}'.format(msg),fill=(255, 153, 0),font=font,anchor="mm",stroke_width=1,stroke_fill=(255, 153, 0))
draw.text(((W1-w)/2,455),f'From  {start}  To  {end}',fill=(51, 51, 51),font=font2,anchor="mm")
draw.text(((W2-w)/2,600),f'{issue}',fill=(51, 51, 51),font=font2,anchor="mm")

# img.show()
st.image(img)
img.save('test.jpg')
st.markdown('<a href="test.jpg" download="cirtificate.jpg">Dowload</a>', unsafe_allow_html=True)



print(start)