import sys
def value_getter(dict: dict, value):
        for key, item in dict.items():
            if item == value:
                return key
        return None

def capitals(value: str):
        states = {
                    "Oregon" : "OR",
                    "Alabama" : "AL",
                    "New Jersey": "NJ",
                    "Colorado" : "CO"
                }
        capital_cities = {
                    "OR": "Salem",
                    "AL": "Montgomery",
                    "NJ": "Trenton",
                    "CO": "Denver"
                }
        value = value_getter(capital_cities, value)
        if not value:
            print("Unknown state")
            return
        print (value)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        capitals(sys.argv[1])