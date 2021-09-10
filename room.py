class Room:
    def __init__(self, size: int, view: str, _type: str, basicRates: float) -> None:
        self.size = size
        self.view = view
        self._type = _type
        self.basicRates = basicRates
    

    def __str__(self) -> None:
        return "Size = %s, View = %s, Type = %s, Basic Rates = %s" % (self.size, self.view, self._type, self.basicRates)
    
    def calculateRates(self, day: str) -> float:
        if day == 'Weekends':
            self.basicRates *= 1.5
        elif day == 'Public Holidays':
            self.basicRates *= 2
        elif day == 'Christmas':
            self.basicRates *= 2.5
        
        return self.basicRates
    



room = Room(132, 'City', 'Double', 120.0)
print(room)

print('*******************')

newRates = room.calculateRates('Public Holidays')
print(room)
print(newRates)