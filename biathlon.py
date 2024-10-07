from random import randint

# Globala variabler
open = 0
closed = 1
start = True

def splash():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("              Biathlon                ")
    print("         a hit or miss game           ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return None

def is_open(value):
    if value == open:
        return True
    else:
        return False

def is_closed(value):
    if value == closed:
        return True
    else:
        return False
    
def new_targets():
    new_list = []
    for x in range (5):
        new_list.append(open)
    return new_list

def close_target(targets, position):
    targets[position] = closed
    return targets

def points(targets):
    goals = 0
    for x in targets:
        if is_closed(x):
            goals = goals + 1
    return goals

def targets_to_string(targets):
    string_targets = ""
    for x in targets:
        if is_open(x):
            string_targets = string_targets + "0 "
        if is_closed(x):
            string_targets = string_targets + "* "
    return(string_targets)

def view_targets(targets):
    print()
    print("0 1 2 3 4")
    print()
    print(targets_to_string(targets))
    print()
    return None

def random_hit():
    if randint(0, 1) == 0:
        return True
    else:
        return False
    
def shoot(targets, position):
    if random_hit() and is_open(targets[position]):
        close_target(targets, position)
        return("Hit on open target")
    elif random_hit() and is_closed(targets[position]):
        return("Hit on closed target")
    else:
        return("Miss")
    
def count_result(targets):
    result = 0
    for x in targets:
        if x == 1:
            result = result + 1
    return result


while start:
    splash()
    shots = 5
    turn = 1
    list_targets = new_targets()
    
    print(f"You got {shots} shots")
    view_targets(list_targets)

    while shots > 0:
        choice = input(f"Shot nr {turn} at: ")
        if -1 < int(choice) < 5:
            print()
            print(shoot(list_targets, int(choice)))
            view_targets(list_targets)
            shots = shots - 1
            turn = turn + 1
        else:
            print("Invalid input. Try again")

    print(f"You hit {count_result(list_targets)} of 5 targets")
    print()
    
    game = input("Do you want to play again? (y/n): ")
    
    if game == "n":
        start = False
    while game != "y" and game != "n":
        game = input("Invalid answer. Do you want to play again? (y/n): ")
        if game == "n":
            start = False
        
print()
print("Game over")
    





