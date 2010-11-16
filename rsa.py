#!/Library/Frameworks/Python.framework/Versions/Current/bin/python

import sys, getopt

def usage():
	print("Here's usage info...")

 # Simple factoring  
def factor(n):  
	intn = int(n)  
	factors = {}  
	lastfactor = n   
	i = 0   

	# 1 is a special case  
	if n == 1:  
		return {1: 1}  

	while 1:  
		i += 1   

		# stop when i is bigger than n  
		# or we have hit more than halfway
		if i > n or i > n**0.5:  
			break  

		if n % i == 0:  
			factors[i] = n / i   
			lastfactor = n / i   

	return factors

def main(argv):
	try:
		opts, args = getopt.getopt(argv, "m:k:n:", ["message=", "key=", "modulus="])
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	message = None
	key = 0
	modulus = 0
	cipher = 0
	cipherNew = 0
	for o,a in opts:
		if o in ("m", "--message"):
			message = int(a)
		elif o in ("key", "--key"):
			key = int(a)
		elif o in ("n", "--modulus"):
			modulus = int(a)
	#
	# All of the above is just structure. Below is the implementation
	# of the alogirthm.
	#
	cipher = message

	# First, find how much we can factor out of the differences between the
	# modulus and the message.
	difference = message - modulus

	# Find the factors for difference
	factors = factor(difference)

	# Find the best one to use. We'll use the median value:
	factorOne = len(factors)/2

	# And find the other factor at that spot
	factorTwo = factors[factorOne]	

	# The original formula is cipher = message^key % modulus 
	# To avoid rounding/overflow errors, we will instead do this:
	#	message % modulus * message % modulus ... message % modulus
	# doing this key times
	for i in range((key*2)-1):
		if i % 2 == 0:
			print "cipher = %d mod %d = %d" % (cipher, modulus, (cipher % modulus))
			cipher = cipher % modulus	
		else:
			print "cipher = %d * %d = %d" % (cipher, message, (cipher * message))
			cipher = cipher * message

	#
	# Just a sanity check so we can compare the results to the
	# "proper" formula.
	#
	cipherNew = (message ** key) % modulus

	#
	# And now, debugging info.
	#
	print "Message = '%s', key=%d, modulus=%d, cipher: %d, " \
	"cipherNew: %d" % (message, key, modulus, cipher, cipherNew)

main(sys.argv[1:])

