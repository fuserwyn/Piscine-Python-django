import sys
def value_getter(dict: dict, str: str):
	for key, value in dict.items():
		if key == str:
			return value
	return None

def key_getter(dict: dict, str: str):
	for key, value in dict.items():
		if value == str:
			return key
	return None


def capitals(str: str):
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
	new_str = str.split(",")
	for token in new_str:
		token = token.strip()
		if (len(token) != 0):
			key = key_getter(capital_cities, token)			
			value = value_getter(states, token)
			if value:
				print(capital_cities.get(value),"is the state of", key_getter(states, value))
			elif key:
				print(capital_cities.get(key),"is the capital of", key_getter(states, key))
			else:
				print(token, "is neither a capital city nor a state") 

if __name__ == '__main__':
    if (len(sys.argv) == 2):
    	capitals(sys.argv[1])	