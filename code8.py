'''
Exception Handling

Right now, getting an error, or exception, in your Python program means the entire program will crash.
You don't want this to happen in real-world programs.
You want the program to detect errors, handle them, and then continue to run.
'''

def spam(divideBy):
		try:
				return 42 / divideBy
		except ZeroDivisionError:
				print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))