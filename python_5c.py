options1 = {"l":"Log in", "q":"Quit"}
options2 = {"r":"Try again", "q":"Quit"}
options3 = {"a":"Add item", "l":"List items", "q":"Log out"}

users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
data = {"nisse":["luva", "vante"], "bosse":["spik", "skruv", "hammare"], "stina":["tidsmaskin"]}

def add(prompt, strings):
    element = input(prompt)
    print()
    strings.append(element)
    return strings

def login(users):
    username = input("User: ")
    password = input("Password: ")
    while username not in users or password != users[username]:
        choice = menu("Invalid username or password", "Option: ", options2)
        if choice == "r":
            username = input("User: ")
            password = input("Password: ")
        else:
            return None    
    return username

def menu(title, prompt, options):
    print(f"\n{title}\n")
    for x in options:
        print(f"  {x}) {options[x]}")
    print()
    selection = input(prompt)
    while selection not in options:
        selection = input(prompt)
    return selection

def view(description, xs):
    print(f"{description}\n")
    n = 1
    for x in xs:
        print(f"  {n}) {x}")
        n += 1

def main():
    while True:
        choice1 = menu("Welcome to Lagra (TM)", "Option: ", options1)
        print()
        if choice1 == "l":
            name = login(users)
            print(f"\nWelcome {name}\n")
            view("These are your items: ", data[name])
            while True:
                choice2 = menu("Select an action: ", "Option: ", options3)
                if choice2 == "a":
                    print()
                    add("Add item: ", data[name])
                    view("These are your items: ", data[name])
                elif choice2 == "l":
                    print()
                    view("These are your items: ", data[name])
                else:
                    break
        else:
            break
main()

