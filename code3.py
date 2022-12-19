'''
Functions

A function is like a miniprogram within a program.
A major purpose of functions is to group code that gets executed multiple times
Without functions, you would have to copy and paste the code each time!
'''

def hello():
		print("Howdy!")
		print("Howdy!!!!")
		print("Hello there.")
hello()
hello()

'''
Def Statements with Parameters

A parameter is the variable(s) inside the parentheses in the function definition
An argument is the value that is sent to the function
'''

def hello(name):
		print("Hello, " + name)
hello('Alice')
hello('Bob')