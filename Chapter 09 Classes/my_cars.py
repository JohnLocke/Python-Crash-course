# Import from each module separately

# Give a module an alias
import car as c
# Using Aliases
from electric_car import ElectricCar as Ec

my_mustang = c.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = Ec('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())


