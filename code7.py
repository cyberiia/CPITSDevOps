'''
Local and Global Scope
'''

def spam():
		print(eggs)
eggs = 42
spam()
print(eggs)