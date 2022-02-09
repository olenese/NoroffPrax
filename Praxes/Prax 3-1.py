
from cgitb import text
from unittest import skip


def splitandjoin():
    text_to_split = input("Please enter a string of text: ")
    splitter = input("Enter a character to split on: ")

    split_result = text_to_split.split(splitter)
    print(split_result)

    combiner = input("Enter a character to combine on: ")
    combined_result = combiner.join(split_result)

    print(combined_result)

def editor():
    some_string = input("Please enter a string: ", )

    choice = 0

    while choice != "e":        
        print("-" * 50)
        print("Current text: ", some_string)
        print("-" * 50)
        print("Select an option to apply for the input text: ")
        print("-" * 50)
        print("1. Uppercase")
        print("2. Lowercase")
        print("3. Titlecase")
        print("4. Remove front and back whitespace")
        print("e. Exit prgram")
        print("")
        choice = int(input("Enter you selection: "))

        if choice == 1:
            some_string = some_string.upper()
        
        if choice == 2:
            some_string = some_string.lower()

        if choice == 3:
            some_string = some_string.title()

        if choice == 4: 
            some_string = some_string.strip()


def slicer():
    to_be_sliced = input("Input a text to be sliced: ")

    try:
        start_index = int(input("Enter a starting index: "))
    except:
        start_index = 0

    try:
        end_index = int(input("Enter a ending index: "))
    except:
        end_index = len(to_be_sliced)

    if start_index < 0:
        start_index = 0

    if end_index >= len(to_be_sliced):
        end_index = len(to_be_sliced)
    
    print(to_be_sliced[start_index:end_index])



if __name__ == "__main__":
#    slicer()
#    splitandjoin()
    editor()
    


