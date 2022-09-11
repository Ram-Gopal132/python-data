from string import punctuation

msg= 'ra@#$m *&gop$#al#$ g@#u&&p$t@#$!a'
for p in punctuation:
    
    msg=msg.replace(p,'')
print(msg)