def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d
	
def histogram2(s):
	d = dict()
	for c in s:
		d[c] = d.get(c,0) + 1
	return d

print(histogram("abcccdeef"))
print(histogram2("abcccdeef"))

def reverse_lookup(d, v):
	for k in d:
		if d[k] == v:
			return k
	raise LookupError('value does not appear in the dictionary')
	
def invert_dict(d):
	inverse = dict()
	for key in d:
		val = d[key]
		if val not in inverse:
			inverse[val] = [key]
		else:
			inverse[val].append(key)
	return inverse
	
#memoized version of fibonacci	
known = {0:0, 1:1}
def fibonacci(n):
	if n in known:
		return known[n]
	res = fibonacci(n-1) + fibonacci(n-2)
	known[n] = res
	return res
	
#note that while mutable global variables can be changed
#in a local scope in a function
#immutable values like below have to be explicitly assigned
#to deal with the global variable before adjustments can be
#made at the global scope
#otherwise it creates a local and just lets it go away after
been_called = False
def example2():
	global been_called
	been_called = True