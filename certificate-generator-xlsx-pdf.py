#Import of libraries
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

#Name of the excel file, if you have it in another location on your hard drive, 
#specify the path, for example: '/home/user/Documents/my_file.xlsx' (don't forget the ')
data = pd.read_excel (r'gen.xlsx')
#Creation of the list
name_list = data["Nombres"].tolist() 
for i in name_list:
    im = Image.open(r'certificate-empty.jpg') #As well as the name of the excel file, place here the jpg image of the empty image file or certificate model
    d = ImageDraw.Draw(im)
    location = (100, 250) #X & Y coordinates where the list data will be printed
    text_color = (0, 137, 209) #Enter the color code in (R,G,B) format
    font = ImageFont.truetype("arial.ttf", 30) #Put the path of the ttf font file to use, the number is its size.
    d.text(location, i, fill = text_color, font = font)
    im.save("./pdf/certificate_" + i + ".pdf") 

