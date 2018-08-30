import time
import tkinter
import random

responses = ['thank you', 'that\' a good one', 'seems good', 'i don\'t care', 'true that!', 'mind you language', 'hahah thats funny', 'pretty good', 'soon..', 'you are a dog person', 'cat do bite', 'hey!!', 'false', 'not true', 'true']

while True :
	question = input('ask a question....\n')
	print('thinking....')
	time.sleep(2)
	print( responses[random.randint(0, 15)] )
	time.sleep(1)
	again = input('-----------\nwanna ask another one..y/n\n')
	if again == 'n' :
		break