
print('Register your detials: ')
name=input('enter your name: ')
email=input('enter your email: ')
passward=input('enter your passward: ')
cPassward=input('enter confirm passward: ')
gender=input('enter your gender(m/f): ')
if len(name) >4 and len(name)<24:
    if '@' in email:

        if passward==cPassward:
            print('you are registerd')
        else:
            print(' password do not match')
    else:
        print('email is invalid')
else:
    print("user must be between 4 and 25 chars")