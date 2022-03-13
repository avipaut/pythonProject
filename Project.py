import event_manager
# import get_case
import menu_manager
import users_manager
import sqlite3 as sq


def waiter():
    print("Waiter")
    print("=== Menu ===")
    print(
        "1..Menu control\n"
        "2.Event management\n"
        "3.Checks\n"
        "4.Log out\n"
    )
    action = int(input("Action:"))
    if action == 1:
        print(
            "1.Show menu\n"
            "2.Log out"
        )
        menu_action = int(input("Action:"))
        if menu_action == 1:
            menu_manager.show_menu()
            waiter()
        if menu_action == 2:
            waiter()
    if action == 2:
        print(
            "1.Add event\n"
            "2.List of events\n"
            "3.Log out"
        )
        event_action = int(input("Action:"))
        if event_action == 1:
            event_manager.get_case()
            waiter()
        if event_action == 2:
            with sq.connect("desert_eagle.db") as con:
                cur = con.cursor()
                for i in cur.execute("SELECT event_id, customer, type_,number_of_guests,summ, date, date_number FROM "
                                     "events").fetchall():
                    print(f"{i[0]} - {i[1]} - {i[2]} - {i[3]} - {i[4]} - {i[5]}-{i[6]}")
            print("Log out.1")
            user_action_exit = int(input("Action:"))
            if user_action_exit == 1:
                waiter()

        if event_action == 3:
            waiter()
    if action == 3:
        with sq.connect("desert_eagle.db") as con:
            cur = con.cursor()
            for i in cur.execute('SELECT "check" FROM "check"').fetchall():
                print(f"{i[0]}")
        print("Log out.1")
        user_action_exit = int(input("Action:"))
        if user_action_exit == 1:
            waiter()
    if action == 4:
        waiter()
def manager():
    print("manager")
    print("===  Menu  ===")
    print(
        "1.Menu control\n"
        "2.Event management\n"
        "3.User management\n"
        "4.Checks\n"
        "5.Log out\n"
    )
    action = int(input("Action:"))
    if action == 1:
        print(
            "1.Show menu\n"
            "2.Add dish\n"
            "3.Delete dish\n"
            "4.Log out"
        )
        menu_action = int(input("Action:"))
        if menu_action == 1:
            menu_manager.show_menu()
        if menu_action == 2:
            menu_manager.add_food()
            manager()
        if menu_action == 3:
            menu_manager.delete_food()
            manager()
        if menu_action == 4:
            manager()
    if action == 2:
        print(
            "1.Add event\n"
            "2.Delete event\n"
            "3.List of events\n"
            "4.Log out"
        )
        event_action = int(input("Action:"))
        if event_action == 1:
            event_manager.get_case()
            manager()
        if event_action == 2:
            event_manager.delete_event()
        if event_action == 3:
            with sq.connect("desert_eagle.db") as con:
                cur = con.cursor()
                for i in cur.execute("SELECT event_id, customer, type_,number_of_guests,summ, date, date_number FROM "
                                     "events").fetchall():
                    print(f"{i[0]} - {i[1]} - {i[2]} - {i[3]} - {i[4]} - {i[5]}-{i[6]}")
            print("Log out.1")
            user_action_exit = int(input("Action:"))
            if user_action_exit == 1:
                manager()
        if event_action == 4:
            manager()
    if action == 3:
        print("1.Add user\n"
              "2.List of users\n"
              "3.Log out")
        user_action = int(input("Action:"))
        if user_action == 1:
            users_manager.add_user()
            print("1.Add more\n"
                  "2.Log out")
            user_action_add = int(input("Action:"))
            if user_action_add == 1:
                users_manager.add_user()
                manager()
            if user_action_add == 2:
                manager()

        if user_action == 2:
            with sq.connect("desert_eagle.db") as con:
                cur = con.cursor()
                for i in cur.execute('SELECT user_id, name, role FROM users').fetchall():
                    print(f"ID:{i[0]}, Name:{i[1]}, Role:{i[2]}\n")
            print("Log out.1")
            user_action_exit = int(input("Action:"))
            if user_action_exit == 1:
                manager()

        if action == 4:
            with sq.connect("desert_eagle.db") as con:
                cur = con.cursor()
                for i in cur.execute('SELECT "check" FROM "check"').fetchall():
                    print(f"{i[0]}")
            print("Log out.1")
            user_action_exit = int(input("Action:"))
            if user_action_exit == 1:
                manager()

        if user_action == 5:
            manager()


def admin():
    print("admin")
    print("===  Menu  ===")
    print(
        "1.Menu control\n"
        "2.Event management\n"
        "3.User management\n"
        "4.Check\n"
        "5.Log out\n"
    )
    action = int(input("Action:"))
    if action == 1:
        print(
            "1.Show menu\n"
            "2.Add dish\n"
            "3.Delete dish\n"
            "4.Log out"
        )
        menu_action = int(input("Action:"))
        if menu_action == 1:
            menu_manager.show_menu()
            admin()
        if menu_action == 2:
            menu_manager.add_food()
            admin()
        if menu_action == 3:
            menu_manager.delete_food()
            admin()
        if menu_action == 4:
            admin()
    if action == 2:
        print(
            "1.Add event\n"
            "2.Delete event\n"
            "3.List of events\n"
            "4.Log out"
        )
        event_action = int(input("Action:"))
        if event_action == 1:
            event_manager.get_case()
            admin()
        if event_action == 2:
            event_manager.delete_event()
        if event_action == 3:
            with sq.connect("desert_eagle.db") as con:
                cur = con.cursor()
                for i in cur.execute("SELECT event_id, customer, type_,number_of_guests,summ, date, date_number FROM "
                                     "events").fetchall():
                    print(f"{i[0]} - {i[1]} - {i[2]} - {i[3]} - {i[4]} - {i[5]}-{i[6]}")
            print("Log out.1")
            user_action_exit = int(input("Action:"))
            if user_action_exit == 1:
                admin()

        if event_action == 4:
            admin()

    if action == 3:
        print("1.Add user\n"
              "2.Delete user\n"
              "3.List of users\n"
              "4.Log out")
        user_action = int(input("Action:"))
        if user_action == 1:
            users_manager.add_user()
            print("1.Add more\n"
                  "2.Log out")
            user_action_add = int(input("Action:"))
            if user_action_add == 1:
                users_manager.add_user()
                admin()
            if user_action_add == 2:
                admin()
        if user_action == 2:
            users_manager.delete_user()
            print("1.Delete more\n"
                  "2.Log out")
            user_action_delete = int(input("Action:"))
            if user_action_delete == 1:
                users_manager.delete_user()
                admin()
            if user_action_delete == 2:
                admin()
        if user_action == 3:
            with sq.connect("desert_eagle.db") as con:
                cur = con.cursor()
                for i in cur.execute('SELECT user_id, name, role FROM users').fetchall():
                    print(f'{i[0]}-{i[1]}-{i[2]}')
            print("Log out.1")
            user_action_exit = int(input("Action:"))
            if user_action_exit == 1:
                admin()
        if user_action == 4:
            admin()
    if action == 4:
        with sq.connect("desert_eagle.db") as con:
            cur = con.cursor()
            for i in cur.execute('SELECT "check" FROM "check"').fetchall():
                print(f"{i[0]}")
        print("Log out.1")
        user_action_exit = int(input("Action:"))
        if user_action_exit == 1:
            admin()
    if action == 5:
        start()


def start():
    global role
    while True:
        print("To come in:1     Registration:2")
        chose = input("Action:")
        role = -1
        if chose.isnumeric():
            chose = int(chose)

        else:
            print("Need a figure!")
            continue

        if chose == 2:
            role = users_manager.add_user()

        elif chose == 1:
            role = users_manager.enter_user()
        else:
            start()

        if role == 2:
            waiter()
        if role == 1:
            manager()
        if role == 3:
            admin()


start()
