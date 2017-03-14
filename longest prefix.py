


def longestCommonPrefix( strs):

    #strs=['abbbbbbbbbb','ab','abbbbc','abcd','abbsda']

    if len(strs) <= 1:
        return strs[0] if len(strs) == 1 else ""

    else:
        long = len(strs[0])

        shortest=long

        for i in strs:
            shortest=min(long,len(i))
            long=shortest


        initial=len(strs[0])

        for i in range(1,len(strs)):

            j = 0

            while (j< shortest and strs[0][j]  and strs[i][j]  and strs[0][j] == strs[i][j] ):
                print " j is " + str(j)
                print "strs[0]["+str(j)+"]" +"is " +str(strs[0][j])
                print "strs["+str(i)+"][" + str(j) + "]" + "is " + str(strs[i][j])
                print "initial is " +str(initial)
                j += 1
                print j

        print strs[0][0:j]

        return strs[0][0:j]



longestCommonPrefix(['ab','asadbss','abbbbc','abbbcs','abbbsda'])