
def word_counter(s):
    words=s.split()
    return len(words)

def area(l,b):
    return l*b
def circumference(r):
    return 2*3.14*r
   

print(word_counter('this is an example'))
print(word_counter('welcome to srmu'))
print(word_counter('my name is ram gopal gupta'))
 
 
# call area and circumference
#1.direct method
print(area(12,10))
#2. user input
l=int(input("enter the num"))
b=int(input("enter the num"))
out=area(l,b)
print("area",out)

#3. shorter user inpit
out=area(int(input("length")),int(input("breadth")))
print("area",out)
print(circumference(4))