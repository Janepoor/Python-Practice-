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