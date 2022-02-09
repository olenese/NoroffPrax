import time
import pytz
from datetime import datetime
from random import seed
from random import randint

def create_time():
    timestamp = time.time()
    print("The time right now is: ", datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'))


def output_local_time():
    tz_london = datetime.now(pytz.timezone("GMT"))
    print("Time right now in London is: ", tz_london.strftime('%Y-%m-%d %H:%M:%S'))

def calculate_differnce():
    value1 = float(input("Please enter a value: "))
    value2 = float(input("Please enter another value: "))

    output = value1 - value2

    print("The differnce between the numbers are: ", output)

def generate_random():
    seed(1)
    value = randint(0, int(input("Please enter a maximum number: ")))
    print(value)


if __name__ == "__main__":
    create_time()
    output_local_time()
    calculate_differnce()
    generate_random()


