###
# Prints a greeting
#
name = ''

while name.strip() == '':
    name = input('Enter your name: ').strip()

print(f'Hello {name}')
