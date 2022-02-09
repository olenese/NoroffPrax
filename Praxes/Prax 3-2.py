import imp
from random import random

def csvreader():
    file = open("mycsv.csv", "r")

    print(file.read())

    for line in file:
        print(line, end="")

    file.close

def randomnumbers():

    output = ""
    for current in range(0, 100):
        print(current)
        output += str(int(random() * 500)) + ", \n"

    my_file = open("randomnumbers.txt", "w")
    my_file.write(output)
    my_file.close()

    
    


if __name__ == "__main__":
    csvreader()
    randomnumbers()

