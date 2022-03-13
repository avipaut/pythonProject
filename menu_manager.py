import sqlite3 as sq
import random, string
# import Project
# import all
# import Project


def check_food_in_menu(name):
    with sq.connect("desert_eagle.db") as con:
        cur = con.cursor()
        cur.execute("SELECT name FROM menu WHERE name LIKE :Name", {"Name": name})
        info = cur.fetchone()
        if info == None:
            return False
        else:
            return True


def food_id_generator():
    temp = random.sample(string.digits, 3)
    food_id = "".join(temp)
    return int(food_id)


def delete_food():
    print("=== Delete dish ===")
    name = input("Name of the dish: ")
    is_food_in_existens = check_food_in_menu(name)
    if is_food_in_existens == True:
        with sq.connect("desert_eagle.db") as con:
            cur = con.cursor()
            cur.execute("DELETE FROM menu WHERE name = :Name", {"Name": name})
            print(f"{name} deleted")


    else:
        print("Dish not found!")


def add_food():
    global price, category
    print("=== Add dish ===")
    while True:
        name = input("Name of the dish: ")
        info = check_food_in_menu(name)
        if info == True:
            print("We already have such a dish!")
            continue
        else:
            break
    while True:
        try:
            # first, second, drink, salad, fruits, grill, fish, candys, biscuits, nuts
            category = int(input("""Dish category
1. First course
2. Second course
3. Beverages
4. Salads
5. Fruit
6. Grill
7. Fish
8. Sweets and biscuits
9. Nuts
10. Back\n"""))
            if category not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
                print("There is no such category!")
                raise ValueError
            if category == 10:

                return

        except:
            continue
        break
    food_id = food_id_generator()
    while True:
        try:
            price = int(input(f"Price {name}: "))
        except:
            print("The price must be a number!")
            continue
        break
    food = (food_id, name, price, category)
    with sq.connect("desert_eagle.db") as con:
        cur = con.cursor()
        cur.execute("INSERT  INTO menu VALUES (?, ?, ?, ?)", food)
    print(f"{food} added")


def get_category(category):
    with sq.connect("desert_eagle.db") as con:
        cur = con.cursor()
        cur.execute("SELECT name, price FROM menu WHERE category = :Category", {"Category": category})
        foods = cur.fetchall()
        return foods


def show_menu():
    global category
    while True:
        try:
            category = int(input("""=== Menu ===
1. First course
2. Second course
3. Beverages
4. Salads
5. Fruit
6. Grill
7. Fish
8. Sweets and biscuits
9. Nuts
10.Back\n"""))
            if category not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
                raise ValueError
        except:
            print("There is no such category")

        if category == 1:
            foods = get_category(1)
            print("First course")
            for food in foods:
                print(f"{food[0]} {food[1]} сом")

        elif category == 2:
            foods = get_category(2)
            print("Second course")
            for food in foods:
                print(f"{food[0]} {food[1]} сом")
        elif category == 3:
            foods = get_category(3)
            print("Beverages")
            for food in foods:
                print(f"{food[0]} {food[1]} сом")
        elif category == 4:
            foods = get_category(4)
            print("Salads")
            for food in foods:
                print(f"{food[0]} {food[1]} сом")
        elif category == 5:
            foods = get_category(5)
            print("Fruit")
            for food in foods:
                print(f"{food[0]} {food[1]} сом")
        elif category == 6:
            foods = get_category(6)
            print("Grill")
            for food in foods:
                print(f"{food[0]} {food[1]} сом")
        elif category == 7:
            foods = get_category(7)
            print("Fish")
            for food in foods:
                print(f"{food[0]} {food[1]} сом")
        elif category == 8:
            foods = get_category(8)
            print("Sweets and biscuits")
            for food in foods:
                print(f"{food[0]} {food[1]} сом")
        elif category == 9:
            foods = get_category(9)
            print("Nuts")
            for food in foods:
                print(f"{food[0]} {food[1]} сом")
        elif category == 10:
            return True

# show_menu()
# add_food()
# delete_food()
# get_category()