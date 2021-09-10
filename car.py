class Car:
    '''
    A constructor to build a car with given attributes
    '''
    def __init__(self, make: str, model: str, color: str, price: float):
        self.make = make
        self.model = model
        self.color = color
        self.price = price

    '''
    A toString method for printing Car objects as strings
    '''
    def __str__(self):
        # return "Make = " + self.make + ", Model = " + self.model + ", Color = " + self.color +", Price = " + str(self.price)
        return "Make = %s, Model = %s, Color = %s, Price = %s" %(self.make, self.model, self.color, self.price)
    
    '''
    A method to update a car's color
    '''
    def selectColor(self) -> None:
        self.color = input("What is the new color? ")
    
    '''
    A method to calculate the total price of the car after taxes
    '''
    def calculateTax(self) -> float:
        priceWithTax = 1.1 * self.price
        return priceWithTax


myCar = Car('Honda', 'Civic', 'White', '1621.50')
print(myCar)

myCar.price = 1800
print(myCar)

myCar.selectColor()
print(myCar)

finalPrice = myCar.calculateTax()
print(finalPrice)