### first non-repeat char


def firstchar(inputstring):

    hash={}
    for i in inputstring:
        if i not in hash:
            hash[i]=1
        else:
            hash[i]+=1
    for i in inputstring:
        if hash[i]==1:
            return i

    return ('##')


print (firstchar("hhelloworld"))