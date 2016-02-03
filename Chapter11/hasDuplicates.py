#take a list and determine if it has duplicates
def has_duplicates(t):
	d = dict()
	for c in t:
		d[c] = d.get(c,0) + 1
		if d[c] > 1:
			return True
	return False

print(has_duplicates([1,2,2]))
print(has_duplicates([1,2,3,3,4,5,2]))
print(has_duplicates([1,2,3,4,5]))