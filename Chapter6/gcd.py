
def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)
	
#gcd(a, 0) = a
#gcd(a, b) = gcd(b, r) when r = a % b

print(gcd(36, 4))
print(gcd(4, 36))
print(gcd(2, 44))
print(gcd(18, 36))
print(gcd(36, 45))