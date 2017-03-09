############password generator
############ pretty straighforward

import random
import string

def gen_pw(size=8, availiable = string.ascii_letters+ string.digits+string.punctuation):

	return ''.join(random.choice(availiable)) for i in range(size)
	




size= raw_input("How long would you like the password to be ?")
print gen_pw(size)
