'''input

IBM cognitive computing|IBM "cognitive" computing is a revolution|IBM cognitive  computing| 'IBM Cognitive Computing' is a Revolution?


"Computer Science Department"|Computer-Science-Department"|the "computer science department"

'''
import string

input1=' IBM cognitive computing |IBM "cognitive" computing is a revolution|IBM cognitive  computing| \'IBM Cognitive Computing\' is a Revolution?'
input2='"Computer    Science Department"|Computer-Science-Department"|the "computer science department"'

onearray=input2.split('|')
secondarray=[]


for i in onearray:
    i = i.lower()      # all in the lower case
    i = i.lstrip()    #delete the whitespace
    i = i.rstrip()   #delete the whitespace
    i = ' '.join(i.split())  # delete extra space
    i= ''.join([k for k in i if k.isalpha()or k==' '])  # remove non-alphanumeric

    if i not in secondarray:
        secondarray.append(i)
    else:
        i=i+str(1)
        secondarray.append(i)

print secondarray
dictionary=dict(zip(secondarray,onearray))
#########################################################

for m in secondarray:
    for n in secondarray:
        if (n.rstrip('1') in m.rstrip('1')):
            if n.rstrip('1')== m.rstrip('1'):
                if len(dictionary[n])> len(dictionary[m]):
                    secondarray.remove(n)
                elif secondarray.index(m)<secondarray.index(n):
                    secondarray.remove(n)
            else: ##not equal
                secondarray.remove(n)
print secondarray
output = '|'.join([dictionary[k] for k in secondarray ])
print output



