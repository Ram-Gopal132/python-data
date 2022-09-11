x=[1,2,3]
x.append(54)
print(x)

data="" #global variable
def data_appender(s):  # argument or parameter
    global data     # this line tell data_appenderthat we have a global var data
    if len(s)>0:
        data+=s
        
# call
data_appender('hello')
data_appender("world:  ")
data_appender("my name is ramgopal:  ")
data_appender("i am from mca31")
print(data)
    