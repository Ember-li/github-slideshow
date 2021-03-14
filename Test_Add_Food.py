#Test Input Add Foods
#Check if input consists of characters or numbers

def test_input(input):
    try:
        food = int(input)
        print("Input is an integer number. Number = ", food)
    except ValueError:
        try:
            food= float(input)
            print("Input is a float number. Number = ", food)
        except ValueError:
            print("Input is a string. Success!")

name = input("Hi. What's your name? ")
test_input(name)
food1 = input("What is the name of your favourite food? ")
test_input(food1)
food2 = input("And what is your second favourite food called? ")
test_input(food2)

