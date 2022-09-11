# string validation

file=input("enter file name")
if file.endswith('.png'):
    print(("its a png file"))
    
if file.endswith('.jpg'):
    print(("its a jpg file"))
    
if file.endswith('.docx'):
    print(("its a document file"))

elif file.endswith('.py'):
    print(("its a py file"))
else:
    print("un identified file,")

    