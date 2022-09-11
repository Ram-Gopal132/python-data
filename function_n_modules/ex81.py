# variable argument
# keywords argument
def total(*values):
    t=0
    for i in values:
        if isinstance(i,(int,float)):
            t +=i
    return(t)
o=total(1,2,3,4)
print(o)
o=total()
o=total(1,3,454,2342,353,656,657,342,)
print(o)
o=total(1,32,'d',43)
print(o)


        