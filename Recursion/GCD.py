# GREATEST COMMON DIVISOR

def gcd(a,b):
	# unintentional constraints[only positive integers]
	assert int(a) ==a and int(b)==b ,"Both the numbers must be integers only"
	if a<0:
		a = -1*a
	if b<0:
		b=-1*b
	# base condition
	if b==0:
		return a
	else:
		# main logic using recursion[just Eucledian Algorithm nothing fancy]
		return gcd(b,a%b)
print(gcd(125,1.8))
print(gcd(-48,18))
