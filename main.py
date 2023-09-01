import math

print(f"Welcome to the GC Fruit Market!")
name = input("What is your name?\n> ")

print("Welcome " + name +". Which Fruit would you like to buy?")

subtotal = []
apples = []
grapes = []
oranges = []
fruit_options = ["1. Apple $2", "2. Grape $1", "3. Orange $3"]
for x in fruit_options:
    print(x)

choice = int(input("> "))

if choice == 1:
    cost = 2
    subtotal.append(int(cost))
    apples.append(int(1))
    print("You bought 1 apple at $2")
if choice == 2:
    cost = 1
    subtotal.append(int(cost))
    grapes.append(int(1))
    print("You bought 1 grape at $1")
if choice == 3:
    cost = 3
    subtotal.append(int(cost))
    oranges.append(int(1))
    print("You bought an orange at $3")
more_fruit = input("Would you like to buy another piece of fruit? y/n \n> ")

while more_fruit == "y":
    print("\nWelcome " + name + ". Which Fruit would you like to buy?")
    for x in fruit_options:
        print(x)
    choice = int(input("> "))
    if choice == 1:
        cost = 2
        subtotal.append(int(cost))
        apples.append(int(1))
        print("You bought 1 apple at $2")
    elif choice == 2:
        cost = 1
        subtotal.append(int(cost))
        grapes.append(int(1))
        print("You bought 1 grape at $1")
    elif choice == 3:
        cost = 3
        subtotal.append(int(cost))
        oranges.append(int(1))
        print("You bought 1 orange at $3")
    more_fruit = input("Would you like to buy another piece of fruit? y/n \n> ")
else:
    print(f"Receipt for {name}")

sub_total = sum(subtotal)
tax = .05 * sub_total
total = sub_total + tax
sum_apples = sum(apples)
sum_grapes = sum(grapes)
sum_oranges = sum(oranges)

print(f"{sum_apples} apple(s) at $2 apiece")
print(f"{sum_grapes} grape(s) at $1 apiece")
print(f"{sum_oranges} orange(s) at $3 apiece")
print(f"Sub Total: ${sub_total}")
print(f" 5% Tax: ${tax}")
print(f"Total: ${total}")