print('a' + 'b')
print('a'.capitalize() + 'b'.capitalize())
# length of string or array
print(len('I want to bite ya'))
print(len([1, 2, 3]))

x = 2
if x == 3:
  print('it is true')
else:
  print('it is not true')

# all log true
print(type('haaah') is str)
print(type(1) is int)
print(type(1.32) is float)
print(type(True) is bool)
print(isinstance(123, int))

# print the name of the type
print(type('string').__name__) # logs str
print(type(print).__name__) # logs builtin_function_or_method

# similar to javascript
a, b = 3, 4
print(a, b)
