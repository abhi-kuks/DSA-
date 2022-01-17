def fibonaci(n):
	assert n>=0 and int(n)==n,"Fibonacci number cannot be negative or non integer"
	if n in [0,1]:
		return n
	else:
		return fibonaci(n-1)+fibonaci(n-2)
l = []
for x in range(25):
	l.append(fibonaci(x))
print(l)
