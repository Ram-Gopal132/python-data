def saveinfo(file='info.text',**kwargs):
    with open(file,'a') as f:
        for k,v in kwargs.items():
            f.write(f'{k}->{v}\n')
            
saveinfo(mobile='techno',price=21000,expiry='2024',model='spark 7 pro')