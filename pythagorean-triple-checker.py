a = int(input('enter side 1\n'))
b = int(input('enter side 2\n'))
c = int(input('enter side 3\n'))

hypo = 0
others = 0

if a > b:
	if a > c:
		hypo = a*a
		others = b*b + c*c
	else:
		hypo = c*c
		others = a*a + b*b
else:
	if b > c:
		hypo = b*b
		others = a*a + c*c
	else:
		hypo = c*c
		others = a*a + b*b

if hypo == others :
	print('congrats! it\'s a triplet ')
else :
	print('too bad')



