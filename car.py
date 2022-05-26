#car-management-system

'''
Car Module, where all the car methods and it's variables are managed.
'''

class Car:
	def __int__(self, name, speed, gas):
		self.name = name
		self.speed = speed
		self.gas = gas

	def getName(self):
		return self.name
	
	def getSpeed(self):
		return self.speed
		
	def getGas(self):
		return self.gas

	def setSpeed(self, speed):
		self.speed = speed
		
	def setName(self, carName):
		self.name = carName
		
	def setGasIntake(self, gasIntake):
		self.gas = gasIntake

	def __str__(self):
		printCarString = "The car " + self.name + " has " + str(self.speed) + " and also have intake of " + str(self.gas) + " litres."
		return printCarString

arrCars = []

def addCar(name, speed, gas):
	newCar = Car()
	newCar.setGasIntake(gas)
	newCar.setName(name)
	newCar.setSpeed(speed)
	arrCars.append(newCar)

def removeCar(name):
    for i in range(len(arrCars)):
        if(arrCars[i].getName() == name):
            break
    arrCars.pop(i)
    
def getCar(name):
	for i in range(len(arrCars)):
		if(arrCars[i].getName() == name):
			break
	return arrCars[i]

addCar("Benz", 100, 10)
addCar("Lamborghini", 200, 20)
addCar("Ferrari", 150, 15)
addCar("Audi", 175, 18)
addCar("Hyndai", 125, 13)
addCar("Maruti", 140, 11)
addCar("Tesla", 190, 17)

print(getCar("Benz"))
print(getCar("Lamborghini"))
print(getCar("Ferrari"))

removeCar("Benz")

print(arrCars)
