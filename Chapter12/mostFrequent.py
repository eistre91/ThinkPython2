def most_frequent(s):
	h = histogram(s)
	
	inverse = []
	for c, num in h.items():
		inverse.append((num, c))
	
	inverse.sort(reverse = True)
	t = []
	for num, c in inverse:
		t.append(c)
	
	return t
	
def histogram(s):
	h = dict()
	for c in s:
		h[c] = h.get(c, 0) + 1
	return h
	
print(most_frequent('aaabbcddd'))