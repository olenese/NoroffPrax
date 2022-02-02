Activity = int(input("What activity would you like to try? (1-3): "))

if Activity == 1:
    print("Activity 1:")

    friends = list()
    for current in range(0, 10):
        friends.append(input("Please enter a name: "))

    print("Unsorted: ", end="")
    print(friends)

    friends.sort()
    print("Sorted: ", end="")
    print(friends)

    search = input("Enter a name to search for: ")
    for i in range(0, 10):
        if friends[i] == search: 
            index = i
            break
    if index > -1:
        print(search, "was found at index", index, ".")
    else:
        print("The name does not exist in the list")

    friends.reverse()
    print("Sorted ", end="")
    print(friends)

    friends_slice = friends[0: int(len(friends) / 2 )]
    print("Slice: ", end="")
    print(friends_slice)

    friends.append(input("Please enter another name: "))
    print("Final ", end="")
    print(friends)


elif Activity == 2:
    print("Activity 2:")

    fastfood = {"pizza", "kebab", "hamburger", "hotdog", "chocolate"}
    fastfood2 = {"kebab", "chips", "chicken", "thai", "pizza"}
    fastfood.add("ramen")

    print("We share the fastfood", fastfood.intersection(fastfood2))



elif Activity == 3:
    print("Activity 3:")

    phonebook = {
        "Company1" : "55443322",
        "Company2" : "11223344",
        "Company3" : "12345678",
        "Company4" : "45612378",
        "Company5" : "69696969"
    }
    new_company = input("Add a company name: ")
    new_phonenumber = input("Add the company's phone number: ")
    phonebook[new_company] = new_phonenumber

    search = input("Type the name of a business")
    if search in phonebook.keys():
         print(phonebook[search])

    else: print("The business is not in the phonebook.")

    print(phonebook)
    print(phonebook.keys())
    



else: print("No activity chosen, quitting"), quit