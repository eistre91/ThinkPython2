
def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]
	
def is_palindrome(word):
	if len(word) > 1 and first(word) == last(word):
		return True and is_palindrome(middle(word))
	elif len(word) == 1 or word == "":
		return True
	else:
		return False
		
print(is_palindrome("redivider"))
print(is_palindrome("noon"))
print(is_palindrome("notapalindrome"))
print(is_palindrome("aabca"))
print(is_palindrome("aabcaa"))