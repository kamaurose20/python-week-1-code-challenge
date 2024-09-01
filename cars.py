class Car:
    def attributes(car, make, model, year):
        car.make = make
        car.model = model
        car.year = year

    def display_info(car):
        print( car.year, car.make, car.model)

my_car = Car()
my_car.attributes("Toyota", "Cross", 2020)
my_car.display_info()
