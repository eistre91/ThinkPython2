
fin = open('words.txt')

def build_anagram_dict(length = -1):
	d = dict()
	s = ''
	for line in fin:
		word = line.strip()
		if length != -1 and len(word) != length:
			continue
		s = list(word)
		s.sort()
		d.setdefault(tuple(s), []).append(word)
	return d
	
def sort_by_length(d):
	length_tuples = []
	for key, value in d.items():
		length_tuples.append( (len(value), value) )
	length_tuples.sort(reverse = True)
	return length_tuples
	
anagrams = build_anagram_dict()
#for key, value in anagrams.items():
#	print(value)
ordered_anagrams = sort_by_length(anagrams)
for num, x in ordered_anagrams:
	if num > 3:
		print(x)
		
fin.seek(0)
		
restricted_anagrams = build_anagram_dict(length=8)
ordered_restricted = sort_by_length(restricted_anagrams)
for num, x in ordered_restricted:
	if num > 3:
		print(x)
