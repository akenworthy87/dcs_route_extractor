



def select_routename(routedata: dict) -> str:
    enumerate_keys = list(enumerate(routedata.keys(), start=1))
    
    print("Select a route name:")
    for i, key in enumerate_keys:
        print(f"{i}: {key}")
    while True:
        choice = input("Enter the number of the route name: ")
        try:
            choice_int = int(choice)
            if 1 <= choice_int <= len(enumerate_keys):
                routename = enumerate_keys[choice_int - 1][1]
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return routename