
fout = open('output.txt', 'w')

line1 = "This here's the wattle,\n"
fout.write(line1)

fout.close()

camels = 42
'I have spotted %d camels.' % camels
'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')

import os
cwd = os.getcwd()
cwd

def walk_alt(dirname):
	for name in os.listdir(dirname):
		path = os.path.join(dirname, name)
		if os.path.isfile(path):
			print(path)
		else:
			walk_alt(path)
			
def find_filenames(dirname):
	for root, dirs, files in os.walk(dirname):
		print(files)

find_filenames('/ThinkPython')

import dbm
db = dbm.open('captions', 'c')
db['cleese.png'] = 'Photo of John Cleese.'
db.close()

import pickle
t = [1, 2, 3]
pickle.dumps(t)
#b'\x80\x03]q\x00(K\x01K\x02K\x03e.'
t1 = [1, 2, 3]
s = pickle.dumps(t1)
t2 = pickle.loads(s)
t2
#[1, 2, 3]
#pickling and then unpickling would copy the object
#instead of giving it the same reference
#Quote from book
#You can use pickle to store non-strings in a database. In fact, this combination is so common
#that it has been encapsulated in a module called shelve

#Running shell commands in python
cmd = 'ls -l'
fp = os.popen(cmd)
#popen is deprecated, to be replaced with subprocess
res = fp.read()
stat = fp.close()
print(stat)
#None

import wc 
#takes in the py file as a module
#note the idiom in wc.py 
#of checking if the __name__ == '__main__'
#before running test code