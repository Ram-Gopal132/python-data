from PIL import Image,ImageFilter,ImageEnhance

im=Image.open(r'C:\Users\RAM GOPAL\OneDrive\Pictures\Photos\Dolfen_w.jpg')
im2=Image.open(r'C:\Users\RAM GOPAL\OneDrive\Pictures\Photos\Snapchat-1837200910.jpg')

#im.filter(ImageFilter.GaussianBlur(40)).show()
# im.filter(ImageFilter.EMBOSS).show()
# im.filter(ImageFilter.CONTOUR).show()
# im.filter(ImageFilter.FIND_EDGES).show()
# im.filter(ImageFilter.BLUR).show()
# im.filter(ImageFilter.SHARPEN).show()
# im.filter(ImageFilter.SMOOTH).show()
# im.filter(ImageFilter.MaxFilter(3)).show()
# im.filter(ImageFilter.MinFilter(3)).show()
# im.filter(ImageFilter.MedianFilter(5)).show()




imc=im.copy()
im2_s=im2.resize((100,100))
imc.paste(im2_s,(0,0))
imc.paste(im2_s,(0,700))
imc.paste(im2_s,(400,0))
imc.paste(im2)
imc.show()
