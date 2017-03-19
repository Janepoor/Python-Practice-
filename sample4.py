'''
input1= Hello Watson
input2= thou art thyself though not a montague - from Romeo and Juliet

'''
input1= 'Hello Watson'
input2= 'thou art thyself though not a montague - from Romeo and Juliet'

array=input2.lower()
output=array[::-1]
char=[]
for i in array:
    char.append(i)
char.reverse()
char[0]=char[0].upper()
for i in range(len(char)):
    if char[i] == " ":
        char[i+1]=char[i+1].upper()
char = ''.join(char)
print char