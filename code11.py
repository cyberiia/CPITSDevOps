# Using for Loops with Lists

for i in [0, 1, 2, 3]:
			print(i)
# Outputs:
# 1
# 2
# 3
# 4

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
	print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# Outputs:
# Index 0 in supplies is: pens
# Index 1 in supplies is: staplers
# Index 2 in supplies is: flamethrowers
# Index 3 in supplies is: binders

'''
 The In and Not In Operators

>>> 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
True
>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> 'cat' in spam
False
>>> 'howdy' not in spam
False
>>> 'cat' not in spam
True
'''