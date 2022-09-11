movies=['Spider man: no way home',
        "south:dj",
        "hindi:tringa"]
print(movies.index("south:dj"))
print(movies.index("hindi:tringa"))
print(movies.index("Spider man: no way home"))

# copy function 
list=['dgdg',445,'dfdf','hfhdfh',656]
duo_list=list.copy()
print(list)
print(duo_list)
val=list
val.append("ramgopal")
print(val)
print(list)
#list.clear()        # remove all element
print(list)

list.pop(2)  # given index number
print(list)
v=list.pop(3)
print(v)