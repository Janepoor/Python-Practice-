
import math

def isPrime(n):

    for i in range(2, int(math.sqrt(n))):
        if (n%i == 0):
            return False
        return True



def numberPrime(N):
    number = 2
    count = 0
    while count < N:
        if isPrime(number) and str(number).startswith('1'):
            print(str(number) + " ")
            count += 1
        number += 1


if __name__ == '__main__':
    N = 20
    numberPrime(N)