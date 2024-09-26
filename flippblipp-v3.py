def flippblipp(n):
    if n % 3 == 0 and n % 5 == 0:
        return("flipp blipp")
    elif n % 3 == 0:
        return("flipp")
    elif n % 5 == 0:
        return("blipp")
    else:
        return(str(n))

start = True
n = 1

print(1)

while start: # Villkor i while-loop
    svar = input("Nästa: ")
    n = n + 1
    if svar != flippblipp(n):
        start = False
        print(f"Fel - {flippblipp(n)}")
        print()
        print("Game Over")
        
    
    


    