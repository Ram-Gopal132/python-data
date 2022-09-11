# string validation

value=input("enter your name")
if value.startswith("Mr"):
    print("welcome gopal")
elif value.startswith("Ms"):
    print("welcome ram")
elif value.startswith("Md"):
    print("welcome sir")
elif value.startswith("Dr"):
    print("welcome si")
else:
    print("you are not invited")