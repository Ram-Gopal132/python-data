
from PIL import Image,ImageFont,ImageDraw

im=Image.open(r'C:\Users\RAM GOPAL\OneDrive\Pictures\Photos\Dolfen_w.jpg')
im2=Image.open(r'C:\Users\RAM GOPAL\OneDrive\Pictures\Photos\Snapchat-1837200910.jpg')


font=ImageFont.truetype(r"C:\Windows\Fonts\aparajbi.ttf",125)
font2=ImageFont.truetype(r"C:\Windows\Fonts\aparajbi.ttf",45)

imd=ImageDraw.Draw(im2)


imd.text((100,100),"Sun",fill=(255,255,255),font=font)
imd.text((300,300),"temp=45°C",fill=(0,-12,0),font=font2)
im2.show()
im2.save('Sun.jpg')