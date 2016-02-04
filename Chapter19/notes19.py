def uses_all(word, needed):
	return all(letter in word for letter in needed)
	
def avoids(word, forbidden):
	return len(set(word) - set(forbidden)) == len(set(word))