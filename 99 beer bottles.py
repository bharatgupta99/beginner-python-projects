numbers = [x for x in range(99, -1, -1)]


for i in numbers:

	if i == 1 :
		l1 = str(i) + ' bottle of beer on the wall, ' + str(i) + ' bottle of beer.'
		l2 = 'Take one down and pass it around, ' + 'no more' + ' bottles of beer on the wall.'

	elif i == 0:
		l1 = 'No more bottles of beer on the wall, no more bottles of beer.'
		l2 = 'Go to the store and buy some more, 99 bottles of beer on the wall.'

	else:	
		l1 =  str(i) + ' bottles of beer on the wall, ' + str(i) + ' bottles of beer.'
		l2 = 'Take one down and pass it around, ' + str(i-1) + ' bottles of beer on the wall.'
		
	print(l1 + '\n' + l2 + '\n')