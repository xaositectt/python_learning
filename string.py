# default libary
from string import Template

message = "hello world"
print(message)

# string interpolation
print(f'{message}')

# can be used for basic calculations as wel
print(f'3 * 4 is {3*4}')

# another way
print("%s %s" %('hello', 'world'))

# another way
name = 'Melinda'
date = 'today'
print('hello there {name}, what is up {date}'.format(name=name, date=date))

# another way
new_template = Template('Hello $name, wassup $date')
print(new_template.substitute(name=name, date=date))

