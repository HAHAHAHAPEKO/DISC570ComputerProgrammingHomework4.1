while True:
    try:
        c = int(input("Enter how many chocolates you want to give: "))
        f = int(input("Enter how many friends you have: "))
        if f == 0:
            print("Imagine that you have zero chocolates and you split them evenly among zero friends. How many chocolate does each person get? See? It doesn't make sense. Chocolate Monster is sad that there are no chocolates, and you are sad because you have no friends.")
            break
        elif c < 0 or f < 0:
            print("Please enter a whole positive number.")
        else:
            print(f"You can equally give each friend {c // f} chocolates.")
            print(f"You will have {c % f} chocolates remaining for yourself.")
            break
    except ValueError:
        print("Please enter a whole positive number.")

