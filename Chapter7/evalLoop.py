def eval_loop():
	s = ''
	while True:
		s = input('> ')
		if s == 'done':
			break
		print(eval(s))

eval_loop()