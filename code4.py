'''
Return Values and Return Statements

When an expression is used with a return statement, the return value is what this expression evaluates to.
Example: The len() function with an argument such as 'Hello' evaluates to the integer value 5, the length of the string.
'''

import random

def getAnswer(answerNumber):
		if answerNumber == 1:
				return 'It is certain'
		elif answerNumber == 2:
				return 'It is decidedly so'
		elif answerNumber == 3:
				return 'Yes'
		elif answerNumber == 4:
				return 'Reply hazy try again'
		elif answerNumber == 5:
				return 'Ask again later'
		elif answerNumber == 6:
				return 'Concentrate and ask again'
		elif answerNumber == 7:
				return 'My reply is no'
		elif answerNumber == 8:
				return 'Outlook not so good'
		elif answerNumber == 9:
				return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
# What's the output?
# You can also try...
print(getAnswer(random.randint(1, 9)))