fruit = 'banana'

print(fruit.count('a'))

def is_palindrome(s):
	return s == s[::-1]
	
print(is_palindrome('noon'))
print(is_palindrome('redivider'))
print(is_palindrome('notone'))

def rotate_word(s, rotation):
	new_s = ''
	beginLower = ord('a')
	beginUpper = ord('A')
	for letter in s:
		if letter.isupper():
			new_s = new_s + chr((ord(letter) - beginUpper + rotation) % 26 + beginUpper)
		elif letter.islower():
			new_s = new_s + chr((ord(letter) - beginLower + rotation) % 26 + beginLower)
		else:
			new_s = new_s + chr((ord(letter) + rotation))
	print(new_s)

rotate_word('IBM', -1)
rotate_word('cheer', 7)
rotate_word('melon', -10)