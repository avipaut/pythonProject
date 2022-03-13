import sqlite3 as sq
import random
import string


def password_generator():
    temp = random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, 8)
    password = "".join(temp)
    return password


def user_id_generator():
    temp = random.sample(string.digits, 4)
    user_id = "".join(temp)
    return user_id


def check_user_in_users(name):
    name = name
    with sq.connect("desert_eagle.db") as con:
        cur = con.cursor()
        cur.execute("SELECT name FROM users WHERE name = :Name", {"Name": name})
        info = cur.fetchone()
        if info == None:
            return False
        else:
            return True


def enter_user():
    global role
    print("=== Вход ===")
    while True:
        name = input("Enter your name:")
        password = input("Enter password:")
        role = str()
        with sq.connect("desert_eagle.db") as con:
            cur = con.cursor()
            cur.execute("SELECT name FROM users WHERE name = :Name and password = :Password",
                        {"Name": name, "Password": password})

            info = cur.fetchone()
            if info == None:
                print("Wrong login or password")
            else:
                print("Welcome!")

                cur.execute(f"SELECT role FROM users WHERE name='{name}' and password ='{password}'")
                role = cur.fetchone()[0]
                if info == None:
                    print("Wrong login or password")
                    return False
                else:

                    return role





def add_user():
    global role
    print("=== Add user ===")
    while True:
        name = input("Username: ")
        is_username_taken = check_user_in_users(name)
        if is_username_taken == True:
            print("Username is taken!")
            continue
        else:
            break
    password = password_generator()
    user_id = user_id_generator()
    while True:
        try:
            role = int(input("""User role
1. Manager
2. Waiter\n"""))
            if role not in (1, 2, 3):
                raise ValueError
        except:
            print("There is no such role!")
            continue
        break
    user = (user_id, name, password, role)

    with sq.connect("desert_eagle.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO users VALUES (?, ?, ?, ?)", user)

    print(f"User {name} added ")
    return role


# add_user()



def delete_user():
    print("=== Удалить пользователя ===")
    name = input("Имя пользователя: ")
    is_user_in_existens = check_user_in_users(name)

    if is_user_in_existens == True:
        with sq.connect("desert_eagle.db") as con:
            cur = con.cursor()
            cur.execute("DELETE FROM users WHERE name = :Name", {"Name": name})
        print(f"Пользователь {name} удален")
    else:
        print("Пользователь не найден!")

# enter_user()
# add_user()
# delete_user()
