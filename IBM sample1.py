# Given a number N and p,q


N,p,q,=raw_input("input N and p and q, seperate by a space ").split(' ')


output=[]
for i in range(1,int(N)+1):
    indicator=0
    if i%int(p)==0 or i%int(q) ==0:
        indicator+=1
    if p in str(i)or q in str(i):
        indicator+=2
    if indicator==3:
        output.append("OUTTHINK")
        #print"OUTTHINK"
    elif indicator==2:
        output.append("THINK")
        #print"THINK"
    elif indicator==1:
        output.append("OUT")
        #print"OUT"
    else:
        output.append(i)

output = ','.join(str(k) for k in output)

print output
