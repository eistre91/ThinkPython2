
def sed(pat, rep, i, o):
	fin = open(i)
	fout = open(o,'w')
	s = ''
	
	for line in fin:
		s = line
		if s == pat:
			s = rep
		fout.write(s)
	
	fin.close()
	fout.close()
	
sed('test\n', 'yep\n', 'test.txt', 'yep.txt')