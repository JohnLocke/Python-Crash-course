# Importing a Single Class
from car import Car

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

# Modifying an Attribute’s Value Directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modifying an Attribute’s Value Through a Method
my_new_car.update_odometer(50)
my_new_car.read_odometer()

# Incrementing an Attribute’s Value Through a Method
my_new_car.increment_odometer(50)
my_new_car.read_odometer()
