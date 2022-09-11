# slice find the substring

s1='Ram Gopal Gupta'
slice1=s1[4:9]
slice2=s1[:3]
print(slice2)
print(slice1)


# last element find

slice3=s1[4:len(s1)]
print(slice3)


name='Ram Gopal Gupta'
fname=name[:3]
lname=name[-5:]
mname=name[4:9]
print(fname,mname,lname)

#reverse

rev_name=name[::-1]
print(rev_name)

#middle name reversed

mname_rev=name[4:9][::-1]
print(mname_rev)

# every even index character

even_name=name[::2]
#every odd index character

odd_name=name[1::2]
print(even_name,odd_name)
