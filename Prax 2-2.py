from ast import arg


Activity = int(input("What activity would you like to try? (1-3): "))

if Activity == 1:
    print("Activity 1:")

    def metric_converter(target_value):
        print("Input inches: ", target_value)
        print("Output CM: ", target_value * 2.54)
    
    if __name__ == "__main__":
        metric_converter(12)


elif Activity == 2:
    print("Activity 2:")

    def summing_machine():
        total = 0
        user_input = input("Please enter a number: ")

        while user_input != "s":
            total += int(user_input)
            user_input = input("Input a number")

    if __name__ == "__main__":
        print(summing_machine())


elif Activity == 3:
    print("Activity 3:")

    def calculate_area_of_shape():
        shape = input("Enter a shape, the allowed shapes are square, cube and circle: ")
        if shape == "square":
            length = float(input("What is the length? "))
            width = float(input("What is the widht? "))

            print(width * length)
        
        elif shape == "cube":
            length = float(input("What is the length? "))
            height = float(input("What is the height? "))

            print(length * height ** 6)

        elif shape == "circle":
            radius = float(input("What is the radius? "))

            print(radius ** 2 * 3.1415)

    if __name__ == "__main__":
        calculate_area_of_shape()



else: print("No activity chosen, quitting"), quit

