import time
import tkinter as tk
import random

top = tk.Tk()
top.resizable(False, False)
top.geometry('300x300')

#Functions
def clear_entry():
	input_box.delete(0, 'end')
	
def quit():
	top.destroy()

def play_again():
	input_box.delete(0, 'end')
	result.delete(1.0, 'end')

def ask():
	if input_box.get() != '':
		result.insert('end','thinking....')
		result.after(2000, result_delay )
	else:
		result.delete(1.0, 'end')
		result.insert('insert','thinking....')
		result.config(state='disabled')

def result_delay():
	responses = ['thank you', 'that\' a good one', 'seems good', 'i don\'t care', 'true that!', 'mind you language', 'hahah thats funny', 'pretty good', 'soon..', 'you are a dog person', 'cat do bite', 'hey!!', 'false', 'not true', 'true']
	result.delete(1.0, 'end')
	result.insert('insert', responses[random.randint(0, 15)])
	result.config(state='disabled')




label = tk.Label(top, text = '8 Ball', font='Helvetica 24 bold' )
label.place(x = 120, y = 5)

question_label = tk.Label(top, text = 'question->', font='Helvetica 16 bold')
question_label.place(x = 10, y = 40)

input_box = tk.Entry(top, bd = 3)
input_box.place(x = 100, y = 40)

ask_button = tk.Button(top, text = 'ask', command = ask, padx = 4, pady = 4)
ask_button.place(x = 30, y = 80)

clear_button = tk.Button(top, text = 'clear', command = clear_entry, padx = 4, pady = 4)
clear_button.place(x = 70, y = 80)

play_again_button = tk.Button(top, text = 'play again', command = play_again, padx = 4, pady = 4)
play_again_button.place(x = 120, y = 80)

quit_button = tk.Button(top, text = 'quit', command = quit, padx = 4, pady = 4)
quit_button.place(x = 210, y = 80)

result = tk.Text(top)
result.place(x = 30, y = 120, width = 220, height = 100)


top.mainloop()