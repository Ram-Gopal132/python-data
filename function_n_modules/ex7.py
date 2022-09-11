x=[2,3,5,6,21,41,12]
output=list(map(lambda i : i**2, x))
output1=tuple(map(lambda i : i**2, x))
print(output)
print(output1)

x1=[2,5,3,6,7,4,8,3,7,46,4]
s1=list(map(lambda i: i-5,x1))
print(s1)



y3=set(map(lambda i:i>3,x1))
print(y3)
y4=set(filter(lambda i:i>3,x1))
print(y4)

name=['raj singh','vijay singh','ram singh','ravi kumar']
name_singh=list(filter(lambda n:n.endswith('singh'),name))
print(name_singh)
name_s1=list(filter(lambda n:n.startswith('r'),name))
print(name_s1)
