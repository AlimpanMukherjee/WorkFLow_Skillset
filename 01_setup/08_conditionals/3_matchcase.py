a=int(input("enter the number"))

match a:
    case 1:
        print("you won a charger")
    case 2:
        print("you won a chocos")
    case 3:
        print("you won a tissue")
    case _:
        print("better luck next time")