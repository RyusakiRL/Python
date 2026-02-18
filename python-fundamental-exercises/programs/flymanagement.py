flies = {
    "AA123": "Confirmed",
    "AB123": "Confirmed",
    "AC123": "Confirmed"     
    }

def fly_management(act, name= "", situation = ""):
    global flies

    if act == "add":
        if name in flies:
            print(f"The fly {name} already exists, situation {flies[name]}")
        else:
            flies[name] = situation

    elif act == "check":
        print(flies.get(f"{name}", "Not encountered"))
    
    elif act == "update":
        if name in flies:
            del flies[name]
            flies[name] = situation
        else:
            flies[name] = situation

    elif act == "cancel":
        flies.pop(name)
        print(f"Removed: {name}")
    
    return
while True:
    print("-----------MAIN-----------\n")
    action = input("Type: add, check, update, cancel or exit\n")

    if action == "add":
        fly_name = input("Insert the fly name: ")
        fly_situation = input("Situation (Confirmed or Delayed): ")
        fly_management(action, fly_name, fly_situation)

    elif action == "check":
        fly_name = input("Insert the fly name: ")
        fly_management(action, fly_name)

    elif action == "update":
        fly_name = input("Insert the fly name: ")
        fly_situation = input("Current situation (Confirmed or Delayed): ")
        fly_management(action, fly_name, fly_situation)

    elif action == "cancel":
        fly_name = input("Insert the fly name: ")
        fly_management(action, fly_name)
    
    elif action == "exit":
        break

    else:
        print("Invalid Command")