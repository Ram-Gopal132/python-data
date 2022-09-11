msg="journey before destination"

# formatting function

print("upper:",msg.upper())
print("lower:",msg.lower())
print("title:", msg.title())

print("title:",msg.capitalize())
print("title:",msg.swapcase())
print("title:",msg.casefold()) #same as lower
print("original",msg)
msg=msg.upper() #updating the msg variable to store upper cased
print("updated:",msg)

