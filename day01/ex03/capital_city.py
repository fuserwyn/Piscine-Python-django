import sys

def capitals(key: str):
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
        key = states.get(key)
        if not key:
            print("Unknown state")
            return
        value = capital_cities.get(key)
        print (value)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        capitals(sys.argv[1])