
def find(word, letter, index=0):
	while index < len(word):
		if word[index] == letter:
			return index
		index = index + 1
	return -1
	
def count(word, findLetter):
	count = 0
	for letter in word:
		if letter == findLetter:
			count = count + 1
	print(count)
	
def count2(word, findLetter):
	count = 0
	location = 0
	location = find(word, findLetter, location)
	while location != -1:
		location = location + 1
		location = find(word, findLetter, location)
		count = count + 1
	print(count)
	
count('aabbaa', 'a')
count2('aabbaa', 'a')
count('aabbaa', 'b')
count2('aabbaa', 'b')