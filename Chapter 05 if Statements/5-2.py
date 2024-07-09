# More Conditional Tests
strings_0 = 'abc'
strings_1 = 'aBc'
print(strings_0 == strings_1)
print(strings_0 == strings_1.lower())

number_0 = 18
number_1 = 20
print(number_0 == 20)
print(number_0 != 20)
print(number_0 > 20)
print(number_0 < 20)
print(number_0 >= 20)
print(number_0 <= 20)

print(number_0 > 19 and number_1 > 19)
print(number_0 > 19 or number_1 > 19)

cities = ['Beijing', 'New York', 'Pairs']
print('London' in cities)
print('London' not in cities)