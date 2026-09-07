class Car:
    def __init__(self, make, model, year, miles, price):
        self.make = make
        self.model = model
        self.year = year
        self.miles = miles
        self.price = price

    def __str__(self):
        return (f'{self.year} is the year COVID did not exist!'
                f'\n I drove in a {self.model} car for {self.miles} miles.' 
                f'\nAnd the cost of my favorite soda is ${self.price}!'
                f'\nAnd this is sponsored by {self.make}!!! NAHHH!!!!'
                f'\n------')

cars = []
cars.append(Car('Ford', 'Mustang', 2013, 25000, 37999))
cars.append(Car('Nissan', 'Xterra', 2004, 89500, 7500))
cars.append(Car('Nissan', 'Maxima', 2012, 25000, 15750))

for car in cars:
    print(car)

your_script = Car('', '', '', '', '')
your_script.make = str(input("Enter your most hated car brand:"))
your_script.model = str(input("Enter a popular celebrity model name (e.g. Kim Kardashian):"))
your_script.year = str(input("Enter a random year from the Gregorian Calendar:"))
your_script.miles = str(input("Enter the total distance you've driven today:"))
your_script.price = str(input("Enter the price of your car purchase:"))

print(f'\n{your_script}')