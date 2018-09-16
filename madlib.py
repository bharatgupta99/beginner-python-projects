def checkVowel(s):
	if s[0] == 'a' or s[0] == 'e' or s[0] == 'i' or s[0] == 'o' or s[0] == 'u':
		return 1;
	else:
		return 0; 


animal = input('enter a type of animal ')
adjective1 = input('enter an adjective ')
verb1 = input('enter a verb ')
adjective2 = input('enter an adjective ')
adjective3 = input('enter an adjective ')
verb2 = input('enter a verb ')

pairs  = {
	'animal' : [animal, checkVowel(animal)],
	'adjective1' : [adjective1, checkVowel(adjective1)],
	'verb1' : [verb1, checkVowel(verb1)],
	'adjective2' : [adjective2, checkVowel(adjective2)],
	'adjective3' : [adjective3, checkVowel(adjective3)],
	'verb2' : [verb2, checkVowel(verb2)],
}

print(pairs)

print('A ' + animal + ' came at my door. He was so ' + adjective1 + '. I ' + verb1 + ' it. After few ays he became ' + adjective2 + ' and ' + adjective3 + '. One day it ' + verb2 + ' me.' )

#A _ came at my door. He was so _. I _ it. After few he became _ and _. One day it _ me.   