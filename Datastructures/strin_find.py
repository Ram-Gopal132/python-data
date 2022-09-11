msg="i am ramgopal i am doing master of computer application"
print(msg.find('of'))

val=msg.find('computer')
if val==-1:
    print('weere not found')
else:
    print(f' were found at {val} index')
    
print('am:',msg.find('am'))

print('am ', msg.index('am'))

print("master:",msg.find("master",5))  # 


print("computer", msg.find("computer"))
print("computer", msg.rfind("computer"))    