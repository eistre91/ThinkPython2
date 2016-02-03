known = {}
def ack(m, n):
	if (not isinstance(m, int)) or (not isinstance(n, int)):
		return None
	elif (m < 0) or (n < 0):
		return None
	if (m,n) in known:
		return known[(m,n)]
	if m == 0:
		known[(m,n)] = n+1
		return n + 1
	elif m > 0 and n == 0:
		return ack(m-1, 1)
	elif m > 0 and n > 0:
		known[(m,n)] = ack(m-1, ack(m, n-1))
		return known[(m,n)]
		
print(ack(3,4))
print(known)