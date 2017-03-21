''''
(S(NP(NNP James)))((VBZ is))(NP(NP(DT a) (NN boy)))(VP(VBG eating))


'''

input1='(NNS sausage)'
input2 ='(NP(DT a) (NN boys))'
input3='(S(NP(NNP James))) ((VBZ is)) (NP(NP(DT a) (NN boy))) (VP(VBG eating))'


def parse(str):
    array = str.split(' ')
    array2=[]
    for i in array:
        if'(' in i:
            array.remove(i)
    print array
    for i in array:
        i=i.rstrip(')')
        array2.append(i)
    output=' '.join(array2)
    print output

parse(input3)
