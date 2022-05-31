import sys
import antigravity

def main():
	if (len(sys.argv) == 4):
		try:
			latitude = float(sys.argv[1])
		except:
			return print ("use float")
		try:
			longitude = float(sys.argv[2])
		except:
			return print ("use float")
		try:
			datedow = sys.argv[3].encode('utf-8')
		except:
			return print("use string")
		antigravity.geohash(latitude, longitude, datedow)
	else:
		print("use 3 args")	

if __name__ == '__main__':
    main()