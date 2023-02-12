def say_hello():
    print("")
    print("")
    print("Hello")

def some_numbers():
    prices = [1.5, 2.5, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0,
          11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]

    sum = 0
    for numbers in prices:
        sum += numbers
    print("this is the sum ", sum)
    lessthan = []
    for numbers in prices:
        if numbers < 12:
            lessthan.append(numbers)
    print("this is how many are less than ",len(lessthan))

def colors():
    colors = ["red", "Green", "blue", "yellow", "green", "Orange", "Red", "BLUE", 
        "YELLOW", "blue", "purple", "Pink", "brown", "Black", "white", "GREY", "silver", 
        "Gold", "Cyan", "magenta", "BluE"]
    numbers = []
    for color in colors:
        numbers.append(color)
    print("this is how many colors there are: ", len(numbers))
    blue = "blue"
    filtered = list(filter(lambda x: x.lower() == blue.lower(), colors))
    print("blue this many times: ", len(filtered))
    unique = []
    for color in colors:
        if color.lower() not in unique:
            unique.append(color.lower())
    print(unique)
        
def ages():
    ages = [24, 35, 18, 46, 29, 51, 22, 33, 40, 27, 55, 19, 31, 37, 43, 25, 49, 20, 23, 26]
    over30 = []
    between2535 =[]
    for numbers in ages:
        if numbers > 30:
            over30.append(numbers)
        if numbers > 25 and numbers < 35:
            between2535.append(numbers)
    print(len(over30))
    print(len(between2535))

ages()
colors()
some_numbers()
say_hello()