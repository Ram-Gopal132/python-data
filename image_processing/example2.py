from PIL import Image

im=Image.open(r'C:\Users\RAM GOPAL\OneDrive\Pictures\Photos\Dolfen_w.jpg')
im2=Image.open(r'C:\Users\RAM GOPAL\OneDrive\Pictures\Photos\Snapchat-1837200910.jpg')
print("resolution",im.size)
print("height",im.height)
print("width",im.width)
print("mode",im.mode)
print("formet",im.format)
print("exif",im.info)

im.convert('L').show()

im.resize(2000,1200).show()

im.resize((im.width*4,im.height*5)).save(r"C:\Users\RAM GOPAL\OneDrive\Pictures\Photos\Dolfen_w.jpg")

# print("resolution",im2.size)
# print("height",im2.height)
# print("width",im2.width)
# print("mode",im2.mode)
# print("formet",im2.format)
# print("exif",im2.info)
