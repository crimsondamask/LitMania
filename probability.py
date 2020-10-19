import random

COUNT1 = 0
COUNT2 = 0

for i in range(100) :
    LIST = ['door1', 'door2', 'door3']
    door_car = random.choice(LIST)
    first_choice = random.choice(LIST)
    if first_choice == door_car :
        COUNT1 += 1
print("Number of times you get the car if you don't change your choice:=> ",
COUNT1, "/100")

for i in range(100) :
    LIST = ['door1', 'door2', 'door3']
    door_car = random.choice(LIST)
    first_choice = random.choice(LIST)
    LIST.remove(first_choice)
    if LIST[0] == door_car :
        COUNT2 += 1
    elif LIST[1] == door_car :
            COUNT2 += 1

print("Number of times you get the car if you change your choice:=> ",
COUNT2, "/100")
