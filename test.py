import streamlit as st
import time
import datetime
import datetime 
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
	href = f'<a href="data:file/jpg;base64,{img_str}" download="cirtificate.jpg">Download result</a>'
	return href



x = datetime.datetime.now()

msg=st.text_input("Enter name")
typ=st.selectbox("Select Training or Internship",('Training','Internships'))
if typ=="Training":
	prg=st.selectbox("Select Training Program",('Python Developer Training','Java Developer Training','Graphic Designer Training','Web Developer Training','Full Stack Developer Training','Social Media Manager Training'))
elif typ=="Internships":
	prg=st.selectbox("Select Internship Program",('Python Developer Internship','Java Developer Internship','Graphic Designer Internship','Web Developer Internship','Full Stack Developer Internship','Social Media Manager Internship'))

start=st.date_input('Enter start date')
end=st.date_input('Enter end date')
# issue=end
W, W1, W2,W3 = (1129,1289,510,1530)
font = ImageFont.truetype('arial.ttf',80)
font2 = ImageFont.truetype('Alegreya-Regular.ttf',31)
font4 = ImageFont.truetype('Alegreya-Regular.ttf',31)
font3 = ImageFont.truetype('Allura-Regular.ttf',35)
font5 = ImageFont.truetype('arial.ttf',28)
img = Image.open('test1.jpeg')
draw = ImageDraw.Draw(img)
w, h = draw.textsize(msg)
w1, h1 = draw.textsize('{} AT LS TRAINEESHIP'.format(prg))
draw.text(((W-w)/2,442),text='{}'.format(msg),fill=(255, 153, 0),font=font,anchor="mm",stroke_width=1,stroke_fill=(255, 153, 0))
draw.text(((W1-w1)/2,565),text='{} AT LS Traineeship'.format(prg),fill=(51, 51, 51),font=font4,anchor="mm")
draw.text((1060/2,605),f'From  {start.strftime("%d/%m/%Y")}  To  {end.strftime("%d/%m/%Y")}',fill=(51, 51, 51),font=font2,anchor="mm")
draw.text((520/2,700),f'{x.strftime("%d/%m/%Y")}',fill=(0, 0, 0),font=font5,anchor="mm")
draw.text((1608/2,695),'L. Sanjana',fill=(0, 0, 0),font=font3,anchor="mm")


# img.show()
st.image(img)

st.markdown(get_image_download_link(img), unsafe_allow_html=True)



# print(start.strftime("%d/%m/%Y"))