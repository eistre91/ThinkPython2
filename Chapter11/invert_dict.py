def invert_dict(d):
	new_dict = dict()
	for key in d:
		new_dict[d[key]] = new_dict.setdefault(d[key], []) + [key]
	return new_dict

d = dict()
d['a'] = 1
d['b'] = 1
d['c'] = 2
d['d'] = 3
print(invert_dict(d))

