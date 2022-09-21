day={"monday","tuesday","wedenesday"}
day.remove("monday")
print(day)

#day.remove("ram")   # key error
day.discard("ram")
print(day)

day1={"friday","saturday","sunday","monday","tuesday","ram"}
print(day|day1)  #union

print(day&day1) #intersection

print(day-day1) # difference
print(day1-day) #difference
a={5,8,9,58,5,8,5,8,5}   
b={9,858,85,8,9,5}
print(a^b)   # Symmetric differenc jo dono mai common n ho
print(a>b)   # commparison number of element
print(a<b)