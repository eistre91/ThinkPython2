fin = open('words.txt')

words = dict()

for line in fin:
	words[line.strip()] = 0
	
print('summerier' in words)

