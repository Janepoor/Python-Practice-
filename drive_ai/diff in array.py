# [1,2,3,4,5,6,7,8]  [1.5, 3.5, 5.5, 7.5, -1, -1, -1, -1]



def f(a):
    n = len(a)
    res = [i for i in a]
    temp = [i for i in a]

    while n > 1:
        x = 0
        for i in range(0, int(n-1), 2):
            print(i)
            average = (temp[i] + temp[i + 1])/2
            res[x] = average
            x += 1

        for i in range(0, int(n-1), 2):
            dif = temp[i] - temp[i+1]
            res[x] = dif
            x += 1
        temp = res[:]
        n /= 2
        #print('n:{}'.format(n))

    return res[::-1]


if __name__ == '__main__':
    l = [1,2,3,4,5,6,7,8]
    print (f(l))