
msg='this is that and is this , that is and this is this'

start=0
query="this"
query1='is'
while True:
    idx=msg.find (query,start)
    if idx==-1:
        break
    print(f'{query} at {idx}')
    start=idx+1

while True:
    idx=msg.find (query1,start)
    if idx==-1:
        break
    print(f'{query1} at {idx}')
    start=idx+1