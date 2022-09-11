from PIL import Image

im=Image.open(r'C:\Users\RAM GOPAL\OneDrive\Pictures\Photos\Dolfen_w.jpg')
im2=Image.open(r'C:\Users\RAM GOPAL\OneDrive\Pictures\Photos\Snapchat-1837200910.jpg')
print(im2)
print(im)
im.rotate(45).show()
im2.rotate(120).show()
