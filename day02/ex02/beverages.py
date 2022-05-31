class HotBeverage:
    def __init__(self):
        self.price = 0.30
        self.name = "hot beverage"
        
    def description(self):
        return "Just some hot water in a cup." 

    def __str__(self):
        TEMEPLATE = ("name : {name}\n"
                     "price: {price:0.2f}\n"
                     "description: {description}")
        return TEMEPLATE.format(name=self.name, price=self.price, description=self.description())
    
class Coffee(HotBeverage):
    def __init__(self):
        self.name = "coffee"
        self.price = 0.40

    def description(self):
        return "A coffee, to stay awake."  

class Chocolate(HotBeverage):
    def __init__(self):
        self.name = "chocolate"
        self.price = 0.50

    def description(self):
        return "Chocolate, sweet chocolate..."
    
class Cappuccino(HotBeverage):
    def __init__(self):
        self.name = "cappuccino"
        self.price = 0.45

    def description(self):
        return "Un po’ di Italia nella sua tazza!"

class Tea(HotBeverage):
    def __init__(self):
        self.name = "tea"
        self.price = 0.30
    
    def description(self):
        return "Just some hot water in a cup."

def main():
    print(HotBeverage())
    print(Chocolate())
    print(Cappuccino())
    print(Coffee())
    print(Tea())


if __name__ == "__main__":
    main()