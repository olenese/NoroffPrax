Activity = int(input("What activity would you like to try? (1-4): "))

if Activity == 1:
    print("Activity 1:")

    total = 0 
    add = int(input("Write a number: "))

    while add != -1:
        total += add
        add = int(input("Write a number: "))

    print("Total: ", total)

elif Activity == 2:
    print("Activity 2:")

    max_value = int(input("Please enter a maximum value: "))
    current = 1

    while current <= max_value:
        total = 0

        for i in range(1, current):
            if current % i == 0:
                total += i

        if total == current:
            print(current, end=" ")

        current += 1

elif Activity == 3:
    print("Activity 3:")

    postalcodes = {
        1444: "Oslo",
        2201: "Hedmark",
        3001: "Buskerud",
        4400: "Vest-Agder",
        5067: "Bergen",
        6856: "Sogndal",
        6893: "Vik i Sogn"

    }
    

    search = int(input("Type a postal code: "))
    if search in postalcodes.keys():
        print(postalcodes[search])

    else: print("This postal code is not in our data")

elif Activity == 4:
    print("Activity 4:")

    sales_list = list()
    while len(sales_list) < 10:
        sales_value = float(input("Enter a sales value: "))
        sales_list.append(sales_value)

        if sales_value < 5000:
            continue

        elif 5000 < sales_value < 10001:
            print("Total: ", sum(sales_list))
            print("Average: ", sum(sales_list)/float(len(sales_list)))

        elif sales_value > 10000:
            print("A possible date entry error has occured.")
            break




else: print("No activity chosen, quitting"), quit