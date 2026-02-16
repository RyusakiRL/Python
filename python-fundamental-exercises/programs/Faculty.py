faculty = {}

def prices(action, name="", price=0, adjust=1.0):

    global faculty

    if action == "add":

        if name in faculty:
            print(f"This faculty already exists: {name}")
        else:
            faculty[name] = price

    if action == "adjust":
        print("Original values:\n")
        print(faculty)
        print("----------------------")
        faculty = {course: price * adjust for course, price in faculty.items()}
        print("Adjusted values:")
        print(f"{faculty}\n")
while True:
    act = input("Type: 'add', 'adjust' or 'exit'\n")

    if act == "add":
        nam = input("Faculty name: ")
        pric = float(input("\nPrice: "))

        prices(act, nam, pric, 0)

    elif act == "adjust":
        adjusting = float(input("\nInsert the value (Ex:1.10): "))
    
        prices(act, " ", 0, adjusting)

    elif act == "exit":
        break
    
    else:
        print("Invalid command")
