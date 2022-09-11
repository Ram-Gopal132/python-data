# return value
def area():
    
    l=int(input('enter the length:  '))
    b=int(input('enter the breadth: '))
    area=l*b
    return area

# calling
# print(area())

# ans=area()
# print("area",ans)
# ans=area()+area()+area()
# print("total area",ans)

# input, len,type,open,eval,dict.get(),list.count()

def minmax():
    global minmax
    x=[23,5,9,8,7,8,9,6,1]
    return min(x), max(x)
value=minmax()
x,y=minmax
print(value)
print(x,y)
print (minmax())
