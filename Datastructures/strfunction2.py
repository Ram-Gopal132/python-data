# String validation function


value=input("enter something")

#test
if value.isnumeric():
    print("only number:",value.isnumeric())
if value.isalpha():
    print("only alphabet",value.isalpha())
if value.isspace():
    print("space",value.isspace())
if value.isupper():
    print("uppercase alphabet",value.isupper())
if value.isalnum():
    print("only alphabet & num",value.isalnum())
if value.islower():
    print("lowercase alphabet",value.islower())

