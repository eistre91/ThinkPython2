 
#reduce takes everything and brings it to one value
#map maps each individual element of a list
#filter takes out a sublist

def nested_sum(t):
	return sum(map((lambda x: sum(x)), t))
	
def cumsum(t):
	total = 0
	new_list = []
	for i in t:
		total += i
		new_list.append(total)
	return new_list
	
print(cumsum([1,2,3,4,5]))

def middle(t):
	return t[1:len(t)-1]
	
t = [1,2,3,4]
print(middle([1,2,3,4]))
t2 = middle(t)
print(t)
print(t2)

def chop(t):
	del t[0]
	del t[len(t)-1]
	return None
	
chop(t)
print(t)

def is_sorted(t):
	if len(t) < 2:
		return True
	for i in range(len(t)-1):
		if t[i] > t[i+1]:
			return False
	return True
	
print(is_sorted([1,2,3]))
print(is_sorted([1,2,1]))

def is_anagram(s1, s2):
	t1 = list(s1)
	t2 = list(s2)
	if len(t1) != len(t2):
		return False
	for i in t1:
		if i not in t2:
		 return False
		t2.remove(i)
	return True

print(is_anagram('aabbcc', 'abcabc'))
print(is_anagram('aabbcc', 'abcabd'))
	
	
	
	
	