
fin = open('words.txt')

def count_long_words():
	for line in fin:
		word = line.strip()
		if len(word) > 20:
			print(word)

count_long_words()

fin.seek(0)
		
def has_no_e(word):
	for letter in word:
		if letter.lower() == 'e':
			return False
	return True
	
def count_no_e():
	total_count = 0
	e_count = 0
	for word in fin:
		if has_no_e(word):
			e_count += 1
		total_count += 1
	print( str(e_count / total_count) )
	
count_no_e()

fin.seek(0)

def avoids(word, forbidden):
	for letter in word:
		for forbid in forbidden:
			if letter == forbid:
				return False
	return True

def censor_list():
	forbidden = input('> ')
	for word in fin:
		if avoids(word, forbidden):
			print(word)

censor_list()

fin.seek(0)

def uses_only(word, good_letters):
	check = False
	for letter in word:
		for good in good_letters:
			if letter == good:
				check = True
		if check == False:
			return False
		check = False
	return True

print(uses_only('aaa', 'a'))
print(uses_only('aaabbba', 'a'))
print(uses_only('aaabbba', 'ab'))
print(uses_only('aaabbba', 'abc'))

def uses_all(word, required_letters):
	passes = False
	for required in required_letters:
		for letter in word:
			if letter == required:
				passes = True
		if passes == False:
			return False
		passes = False
	return True
		
print(uses_all('aaa', 'a'))
print(uses_all('aaabbba', 'a'))
print(uses_all('aaabbba', 'ab'))
print(uses_all('aaabbba', 'abc'))

def is_abecedarian(word):
	for i in range(len(word)-1):
		if word[i] > word[i+1]:
			return False
	return True
	
print(is_abecedarian('aaa'))
print(is_abecedarian('abc'))
print(is_abecedarian('acb'))