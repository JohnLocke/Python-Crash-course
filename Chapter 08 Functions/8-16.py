# Imports
import person_function
person = person_function.build_person('John', 'Locke')
print(person)


from person_function import build_person
person = build_person('John', 'Locke')
print(person)


from person_function import build_person as bp
person = bp('John', 'Locke')
print(person)


import person_function as pf
person = pf.build_person('John', 'Locke')
print(person)


from person_function import *
person = build_person('John', 'Locke')
print(person)








