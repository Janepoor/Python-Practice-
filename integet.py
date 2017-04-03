

def integertoword(num):
    """lv1 = "Zero One Two Three Four Five Six Seven Eight Nine Ten \
           Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
    lv2 = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
    lv3 = "Hundred"
    lv4 = "Thousand Million Billion".split()

    words= []
    digit= 0

    while num:

        token,num=num%1000, num/1000  ## token is last three digit  num is the front
        word=''
        if token>99: ### add hundured
            word+= lv1[int(token/100)] + ' ' + lv3+ ' '
            token%=100
        if token >19:  #### add ten
            word+= lv2[int(token/10) -2]+' '
            token%=10
        if token >0:
            word+=lv1[int(token)]+' '
        word=word.strip()

        if word:
            word += ' ' + lv4[digit - 1] if digit else ''
            words+=word,
        digit+=1

    result=' '.join(word[::-1])
    print(result)
    return words"""

    to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

    def words(n):
        n=int(n)
        if n < 20:
            return to19[n - 1:n]
        if n < 100:
            return [tens[int(n / 10) - 2]] + words(n % 10)
        if n < 1000:
            return [to19[int(n / 100) - 1]] + ['Hundred'] + words(n % 100)

        for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):  ##p is the number
            if n < 1000 ** (p +1):
                return words(n / 1000 ** p) + [w] + words(n % 1000 ** p)

    print(' '.join(words(num)) )

    return ' '.join(words(num)) or 'Zero'



integertoword(98764321)