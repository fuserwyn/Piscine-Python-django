import random
from beverages import HotBeverage, Coffee, Tea, Cappuccino, Chocolate
class CoffeeMachine:

	def __init__(self):
		self.drinks = 10

	class EmptyCup(HotBeverage):
		def __init__(self):
			self.name = "empty up"
			self.price = 0.90
			
		
		def description(self):
			return  "An empty cup?! Gimme my money back!"
		
	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.")
		
	def repair(self):
			self.drinks = 10

	def serve(self, beverage: HotBeverage):
			self.drinks -= 1 
			if self.drinks < 0:
				raise CoffeeMachine.BrokenMachineException
			if random.randint(0,10) == 0:
				return CoffeeMachine.EmptyCup()
			return beverage

def main():
	coffeemachine = CoffeeMachine()
	for _ in range (20):
		try:
			print(coffeemachine.serve(random.choice([Tea, Coffee, Cappuccino, Chocolate, Coffee])))
		except CoffeeMachine.BrokenMachineException as broken:
			print(broken)
			coffeemachine.repair()


if __name__ == '__main__':
    main()


