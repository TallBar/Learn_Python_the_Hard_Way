# Set # of cars
cars = 100
# 
space_in_a_car = 4
# Total # of drivers
drivers = 30
#Total # of passengers
passengers = 90
# Cars not being used
cars_not_driven = cars - drivers
cars_driven = drivers
# How many people can be taken at a time
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We need to put about", average_passengers_per_car,"in each car")

# ERROR USE 
# average_passengers_per_car = car_pool_capacity / passengers
# There were two errors in this code: 1) The #variable carpool_capacity was separated #into car_pool_capacity and thus wasn't #recognized; 2) The variable passengers was turned into passenger

