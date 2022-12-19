'''
"While" Loop Statements

You can make a block of code execute over and over again using a "while" statement.
The code in a "while" clause will be executed as long as the "while" statement’s condition is True.
'''

spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1

'''
"For" Loops and the Range() Function

If you want to execute a block of code only a certain number of times
'''

print('My name is')
for i in range(5):
        print('Jimmy Five Times (' + str(i) + ')')

for i in range(5):
    print('Hello, world.')