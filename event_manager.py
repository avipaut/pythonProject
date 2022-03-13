import sqlite3 as sq
import random


# 1 - той
# 2 - бизнес встреча


def event_id_generator():
    event_id = random.randint(111, 999)
    return event_id


def check_number(number):
    up = 0
    down = 0
    if number % 6 == 0:
        return True
    else:
        n1 = number
        n2 = number
        while n1 % 6 != 0:
            n1 += 1
        while n2 % 6 != 0:
            n2 -= 1
        return n1, n2


def check_customer_in_users(customer):
    customer = customer
    with sq.connect("desert_eagle.db") as con:
        cur = con.cursor()
        cur.execute("SELECT customer FROM events WHERE customer = :Customer", {"Customer": customer})
        info = cur.fetchone()
        if info == None:
            return False
        else:
            return True


def get_names_of_food(category):
    with sq.connect("desert_eagle.db") as con:
        cur = con.cursor()
        cur.execute("SELECT food_id, name, price FROM menu WHERE category = :Category", {"Category": category})
        foods = cur.fetchall()
        return foods


def get_variant(category):
    global variant, aa
    if category == 1:
        aa = "first dish"
    elif category == 2:
        aa = "dish for the second"
    elif category == 3:
        aa = "drink"
    elif category == 4:
        aa = "salad"
    elif category == 5:
        aa = "fruit"
    elif category == 6:
        aa = "grill"
    elif category == 7:
        aa = "fish"
    elif category == 8:
        aa = "candy and biscuits"
    elif category == 9:
        aa = "nuts"
    variants = get_names_of_food(category)
    ids = []
    for variant in variants:
        ids.append(variant[0])
    while True:
        try:
            print(f"Please select {aa}: ")
            for variant in variants:
                print(f"{variant[0]}. {variant[1]} - {variant[2]} сом")
            variant = int(input())
            if variant not in ids:
                raise ValueError
        except:
            print("There is no such position in the menu!")
            continue
        break
    return variant


def get_name_menu():
    first = get_variant(1)
    second = get_variant(2)
    drink = get_variant(3)
    salad = get_variant(4)
    fruits = get_variant(5)
    grill = get_variant(6)
    fish = get_variant(7)
    candys = get_variant(8)
    nuts = get_variant(9)

    return (first, second, drink, salad, fruits, grill, fish, candys, nuts)


def get_food_name_price_by_food_id(food_id):
    with sq.connect("desert_eagle.db") as con:
        cur = con.cursor()
        cur.execute("SELECT name, price FROM menu WHERE food_id = :Food_id", {"Food_id": food_id})
        food_name_price = cur.fetchall()[0]
    return food_name_price


def get_number_menu(number):
    # на каждого первое и второе, на двоих один литр напитка, на троих два салата,
    # на шестерых один гриль, на троих одна нарезка фруктов, на троих по 200 грамм
    # конфет и печенья, на троих одна рыба, на троих по 100 грамм орехов

    first = number
    second = number
    drink = number / 2
    salad = number / 3
    fruits = number / 3
    grill = number / 6
    fish = number / 3
    candys = number / 3
    nuts = number / 3

    return (first, second, drink, salad, fruits, grill, fish, candys, nuts)


def get_number_of_guests():
    global number, choice
    while True:
        try:
            number = input("Number of guests: ")
            if number.isnumeric():
                number = int(number)

            else:
                print("Need a figure!")
                continue
            info = check_number(number)
            if info != True:
                up = number + info[0]
                down = number - info[1]
                while True:
                    try:
                        choice = int(input((f"""The number of guests you entered is not a multiple of 6.
This will make it difficult to arrange the guests at the tables.
You can:
1. Increase their number to {info[0]}
2. Reduce their number to {info[1]}\n""")))
                        if choice not in (1, 2):
                            raise ValueError
                    except:
                        print("Choose one of the options!")
                        continue
                    break
                if choice == 1:
                    number = info[0]
                elif choice == 2:
                    number = info[1]
        except ValueError:
            print("Insert the number!")
            continue
        break
    return number


def food_ids_into_food_names_prices(food_ids):
    food_names_prices = []
    for i in food_ids:
        food_names_price = get_food_name_price_by_food_id(i)
        food_names_prices.append(food_names_price)
    return food_names_prices


def get_menu():
    number_of_guests = get_number_of_guests()
    food_numbers = get_number_menu(number_of_guests)
    food_ids = get_name_menu()
    food_names_prices = food_ids_into_food_names_prices(food_ids)
    food_names = []
    food_prices = []
    for i in food_names_prices:
        food_names.append(i[0])
        food_prices.append(i[1])
    food_costs = []
    for i, e in zip(food_numbers, food_prices):
        food_costs.append(i * e)
    menu = []
    for k, l, m in zip(food_names, food_numbers, food_costs):
        menu.append((k, l, m))
    summ = 0
    for i in menu:
        summ += i[-1]
    return (number_of_guests, menu, summ)


def get_arrangement_of_tables(number_of_guests, type_):
    global arrangement_of_tables
    number_of_tables = number_of_guests / 6
    if type_ == "Toy":
        arrangement_of_tables = "P - figurative"
    elif type_ == "Business meeting":
        arrangement_of_tables = "T - figurative"
    elif type_ == "Corporate":
        arrangement_of_tables = "islets"
    return (number_of_tables, arrangement_of_tables)


while True:
    def date_month():
        date = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
                "December"]
        chose_date = input("Month:")
        if chose_date not in date:
            print("Incorrect date!")
            date_month()
            return chose_date
        if chose_date in date:
            return chose_date


    def date_number(month):
        global chose_number
        date_month1 = month
        if date_month1 == "January" or date_month1 == "March" or date_month1 == "May" or date_month1 == "July" or \
                date_month1 == "October" or date_month1 == "December":
            chose_number = int(input("Choose a date:"))
            if chose_number in range(1, 32):
                with sq.connect("desert_eagle.db") as con:
                    cur = con.cursor()
                    cur.execute("SELECT date,date_number FROM events WHERE date = :Date and date_number = :Date_number",
                                {"Date": month, "Date_number": chose_number})
                    info = cur.fetchone()
                    if info == None:
                        return chose_number

                    else:
                        print("Date is busy, please choose another date!")
                        date_number(month)
                        return chose_number
            else:
                print("Incorrect date!")
                date_number(month)
                return chose_number

        if date_month1 == "April" or date_month1 == "June" or date_month1 == "September" or date_month1 == "November":
            chose_number = int(input("Choose a date:"))
            if chose_number in range(1, 31):
                with sq.connect("desert_eagle.db") as con:
                    cur = con.cursor()
                    cur.execute("SELECT date,date_number FROM events WHERE date = :Date and date_number = :Date_number",
                                {"Date": month, "Date_number": chose_number})
                    info = cur.fetchone()
                    if info == None:
                        return chose_number

                    else:
                        print("Date is busy, please choose another date!")
                        date_number(month)
                        return chose_number
            else:
                print("Incorrect date!")
                date_number(month)
                return chose_number
        if date_month1 == "February":
            chose_number = int(input("Choose a date:"))
            if chose_number in range(1, 29):
                with sq.connect("desert_eagle.db") as con:
                    cur = con.cursor()
                    cur.execute("SELECT date,date_number FROM events WHERE date = :Date and date_number = :Date_number",
                                {"Date": month, "Date_number": chose_number})
                    info = cur.fetchone()
                    if info == None:
                        return chose_number

                    else:
                        print("Date is busy, please choose another date!")
                        date_number(month)
                        return chose_number

            else:
                print("Incorrect date!")
                date_number(month)
                return chose_number


    break


def add_event():
    global type_
    event_id = event_id_generator()
    customer = input("Customer name: ")
    chose_date = date_month()
    date_number1 = date_number(chose_date)
    order = get_menu()
    while True:
        try:
            type_ = int(input("""Select the type of event
1. Toy
2. Business meeting
3. Corporate\n"""))
            if type_ not in (1, 2, 3):
                raise ValueError
        except:
            print("There is no such type of event!")
            continue
        break

    if type_ == 1:
        type_ = "Toy"
    elif type_ == 2:
        type_ = "Business meeting"
    elif type_ == 3:
        type_ = "Corporate"
    arrangement_of_tables = get_arrangement_of_tables(order[0], type_)

    number_of_guests = order[0]
    summ = order[2] + order[2] * 0.15
    event = (event_id, customer, type_, number_of_guests, summ, chose_date, date_number1,)

    with sq.connect("desert_eagle.db") as con:
        cur = con.cursor()
        cur.execute("INSERT  INTO events VALUES (?,?,?,?,?,?,?)", event)
    return event_id, customer, type_, order, arrangement_of_tables


def get_case():

    order = add_event()
    customer = order[1]
    type_ = order[2]
    if type_ == "Toy":
        type_ = "toy"
    elif type_ == "Business meeting":
        type_ = "business meeting"
    elif type_ == "Corporate":
        type_ = "corporate"
    menu = order[3][1]
    number_of_guests = order[3][0]
    summ = order[3][2]
    service = summ * 0.15
    summ += service
    number_of_tables = order[4][0]
    arrangement_of_tables = order[4][1]
    strMenu = ""
    for strs in menu:
        strMenu += f"{strs[0]} {strs[1]} {strs[2]}\n"
    case = f"""=== Order ===
{customer} holds a {type_} for guests in quantity {number_of_guests}.
Menu: 
{strMenu}
Tables will be placed in quantity {number_of_tables} with arrangement {arrangement_of_tables}.
The total cost together with the service in {service} сом will be {summ} сом.
"""
    print(case)
    case1 = case
    with sq.connect("desert_eagle.db") as con:
        cur = con.cursor()
        cur.execute("INSERT  INTO 'check' VALUES (?)", [case1])

    print("1.Back")
    exit_menu = int(input("Action:"))
    if exit_menu == 1:
        return True


def delete_event():
    print("=== Delete Event ===")
    customer = input("Customer name: ")
    is_event_in_existens = check_customer_in_users(customer)
    if is_event_in_existens == True:
        with sq.connect("desert_eagle.db") as con:
            cur = con.cursor()
            cur.execute("DELETE FROM events WHERE customer = :Customer", {"Customer": customer})
        print(f"Сustomer {customer} deleted")
        return True

    else:
        print("Event not found!")


def get_event(customer):
    with sq.connect("desert_eagle.db") as con:
        cur = con.cursor()
        cur.execute("SELECT customer, type_, number_of_guests FROM events WHERE customer = :Customer",
                    {"Customer": customer})
        event1 = cur.fetchall()
        return event1


# def show_events():
#     global _type
#     while True:
#         try:
#             _type = int(input("""=== Меню ===
# 1. Официанты
# 2. Менежеры
# 3. Админы\n
# """))
#             if _type not in (1, 2, 3):
#                 raise ValueError
#         except:
#             print("Такой роли нет")
#
#         if _type == 1:
#             event1 = get_event(1)
#
#             for customer in event1:
#                 print(f"{customer[1]} {customer[0]} сом")
#
# # show_events()
# get_event()
# delete_event()
# get_case()
# print(get_menu())
# print(get_name_menu())

# print(get_number_menu(150))

# print(get_case())

# print(food_ids_into_food_names_prices((3795, 4785, 2486, 829, 8124, 5642, 2978, 2456, 6901)))
# добавить в таблицу event_id, customer, data, number, men
