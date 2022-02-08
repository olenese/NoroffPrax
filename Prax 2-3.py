def generate_letter():
    current = 97
    while True:
        yield chr(current)
        current += 1 
        if current == 102:
            current = 97


def handle_exceptions():

    sales_number = list()

    while input("Do you want to enter a sales value? Enter y for yes and any other key for no") == "y":
        try:
            sales_number.append(float(input("Please enger a sales value")))
        except ValueError:
            print("Please ensure that you enter a valid value")
        
    print("You have entered ", len(sales_number), "sales values. \n How many of these would you like to include in the total?")

    while True: 
        numbers_of_sales = -1
        try: 
            numbers_of_sales = int(input("Number of sales: "))

            total = 0

            try:
                for i in range(0, numbers_of_sales):
                    total += sales_number[i]
                print("Sales total: ", total)
                break
            except IndexError:
                print("Please ensure the number of sales entered is in the range 0 to ", len(sales_number))
        except ValueError:
            print("Please ensure that you enter a valid number of sales.")
            continue


if __name__ == "__main__":
    task_number = float(input("Which task would you like to run?"))
    if task_number == 1:
        letter_generator = generate_letter()
        for i in range(0, 10):
            print(next(letter_generator))
    elif task_number == 2:
        handle_exceptions()
    else: exit