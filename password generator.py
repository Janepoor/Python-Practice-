############password generator
############ pretty straighforward

import random
import string

def gen_pw(size, availiable = string.ascii_letters+ string.digits+string.punctuation):

	return ''.join(random.choice(availiable) for i in range(int(size)))
	


passwordlen = raw_input("How long would you like the password to be ? ")

print gen_pw(passwordlen)


# generate a password with length "passlen" with no duplicate characters in the password


s = string.ascii_letters+ string.digits+string.punctuation
passlen = 8
p =  "".join(random.sample(s,passlen ))
print p



