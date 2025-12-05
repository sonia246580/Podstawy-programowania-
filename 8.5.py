###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#

swift = input('Enter SWIFT code: ')

bank = swift[:4]
country = swift[4:6]

print(f'Bank Code: {bank}')
print(f'Country Code: {country}')