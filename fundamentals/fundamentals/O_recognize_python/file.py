num1 = 42  # variable declaration, initialize integer
num2 = 2.3  # variable declaration, initialize float
boolean = True  # variable declaration, initialize boolean
string = "Hello World"  # variable declaration, initialize string
pizza_toppings = [
    "Pepperoni",
    "Sausage",
    "Jalepenos",
    "Cheese",
    "Olives",
]  # composite declaration, initialize list
person = {
    "name": "John",
    "location": "Salt Lake",
    "age": 37,
    "is_balding": False,
}  # composite declaration, initialize dictionary
fruit = ("blueberry", "strawberry", "banana")  # composite declaration, initialize tuple
print(type(fruit))  # print type tuple
print(pizza_toppings[1])  # print 'Sausage'
pizza_toppings.append("Mushrooms")  # appends 'Mushrooms' to end of pizza_toppings list
print(person["name"])  # print value 'John' for key 'name' in person dictionary
person["name"] = "George"  # update value for key 'name' to 'George'
person[
    "eye_color"
] = "blue"  # add key 'eye_color' with value 'blue' to person dictionary
print(fruit[2])  # print 'banana'

if num1 > 45:  # conditional if/else declaration, prints 'It's lower'
    print("It's greater")
else:
    print("It's lower")

if (
    len(string) < 5
):  # conditional if, elif, else declaration using length method, prints 'Just right!' (string var is 11 char long)
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):  # for loop declaration, prints 0 to 4
    print(x)  # print x for each iteration
for x in range(2, 5):  # for loop declaration, prints numbers between 2 and 5
    print(x)  # print x for each iteration
for x in range(2, 10, 3):  # for loop declaration, prints numbers 2 to 10 then 10 to 3
    print(x)  # print x for each iteration
x = 0  # variable declaration, initialize int
while x < 5:  # while loop declaration, prints 0 to 4
    print(x)  # print x for each iteration
    x += 1  # increments x by 1 each iteration

pizza_toppings.pop()  # removes 'Mushrooms' from pizza_toppings list
pizza_toppings.pop(1)  # removes 'Sausage' from pizza_toppings list

print(
    person
)  # prints {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, 'eye_color': 'blue'}
person.pop("eye_color")  # removes 'eye_color' key/value pair
print(
    person
)  # prints {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

for (
    topping
) in (
    pizza_toppings
):  # for loop declaration; skips 'Pepperoni', prints 'After 1st if statement' 3 times then breaks loop
    if topping == "Pepperoni":
        continue
    print("After 1st if statement")
    if topping == "Olives":
        break


def print_hello_ten_times():  # function declaration
    for num in range(10):  # for loop declaration
        print("Hello")  # prints 'Hello' 10 times from 0-9


print_hello_ten_times()  # calls the function


def print_hello_x_times(x):  # function declaration with parameter x
    for num in range(x):  # for loop declaration using the parameter x as the argument
        print("Hello")


print_hello_x_times(
    4
)  # calls the function, passing in 4 for the range(), prints 'Hello' 4 time, 0-3


def print_hello_x_or_ten_times(
    x=10,
):  # function declaration with parameter x, x starts at value 10
    for num in range(x):  # for loop declaration taking in x=10
        print("Hello")


print_hello_x_or_ten_times()  # function call, prints 'Hello' 10 times
print_hello_x_or_ten_times(4)  # function call, prints 'Hello' 4 times


"""
Bonus section
"""

# print(num3)  # NameError: name <num3> is not defined
# num3 = 72 # variable declaration, initialize int
# fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) # KeyError: 'favorite_team
# print(pizza_toppings[7]) # IndexError: list index out of range
#   print(boolean) # IndentationError: unexpected indent
# fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'
