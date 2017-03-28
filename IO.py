##self define Exception
class myException(Exception):
    pass



##throw an Exception

def division(x,y):
    if y == 0:
        raise ZeroDivisionError('not allow for dividing 0')
    return x/y


try:
    division(1,0)
except ZeroDivisionError as e:
    print (e)

except (ZeroDivisionError,ValueError) as e:
    print (e)

except:
    print ("other problem")



import sys

file_name = sys.argv[1]
text = []

try:
    with open(file_name,'rb') as f:
        text = f.readline()

except IOError:
    print ('cannot open', file_name)

if text:
    print (text[1])




