import math

def estimate_pi():
	coefficient = 2 * math.sqrt(2) / 9801
	sum = 0.0
	previousTerm = 1.0
	k = 0
	print(previousTerm > 1e-15)
	while previousTerm > 1e-15:
		numerator = math.factorial(4*k) * (1103 + 26390 * k)
		denominator = (math.factorial(k)**4) * (396 ** (4 * k))
		previousTerm = coefficient * numerator/denominator
		sum = sum + previousTerm
		k = k + 1
	return 1/sum
	
print(estimate_pi())
print(estimate_pi() - math.pi)