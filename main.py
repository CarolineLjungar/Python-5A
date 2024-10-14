def add(prompt, strings):
    new_string = input(prompt)
    strings.append(new_string)
    return strings

def view(description, strings):
    n = 0
    print(f"{description}")
    print()
    for x in strings:
        n = n + 1
        print(f"{n}) {x}")

def menu(title, prompt, options):
    while True:
        print(title)
        print()
        for x in options:
            print(f"{x}) {options[x]}")
        print()
        s = input(f"{prompt} ")
        print()
        if s in options:
            return s
        else:
            print(f"invalid option: {s}. Please try again.")

def login(users):
    options = {"r":"Try again", "q":"Quit"}
    while True:
        print()
        a = input("    User: ")
        p = input("Password: ")
        if a in users and p in users[a]["password"]:
            print()
            return a
        else:
            print()
            choice = menu("Invalid username or password", "Option:", options)
            if choice == "q":
                return None

def main():
    users = {"nisse": {"password": "apa", "items": ["luva", "vante"]},"bosse": {"password": "ko", "items": ["gräs", "mjölk"]}}

    while True:
        choice = menu("Welcome to Lagra (TM)", "Option:", {"l": "Log in", "q": "Quit"})
        if choice == "q":
            print("Goodbye!")
            break
        logged_in_user = login(users)
        if not logged_in_user:
            continue
        while True:
            view("These are your items", users[logged_in_user]["items"])
            print()
            action = menu("Select an action", "Option:", {"a": "Add item", "l": "List items", "q": "Log out"})      
            if action == "a":
                add("Add item: ", users[logged_in_user]["items"])
                print()
            elif action == "l":
                print()
                view("These are your items", users[logged_in_user]["items"])
            elif action == "q":
                break

        
    