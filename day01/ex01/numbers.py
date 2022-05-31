def numbers():
    file = open ("numbers.txt", 'r')
    for line in file.readlines():
        numbers = line.split(",")
    for i in numbers:
        print(i)
    file.close()

if __name__ == '__main__':
    numbers()