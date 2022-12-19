'''
Keywords Arguments

Most arguments are identified by their position in the function call
However, rather than through their position, keyword arguments are identified by the keyword put before them in the function call.
For example, the print() function has the optional parameters end and sep
'''

print('Hello', end='')
print('World')
# Output: HelloWorld

print('cats', 'dogs', 'mice', sep=',')
# Output: cats,dogs,mice