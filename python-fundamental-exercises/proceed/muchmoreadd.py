def generator (bord, repeats, text):
    match bord:
        case 1:
            print("+-------=======------+")
        case 2:
            print("~~~~~~~~:::::::~~~~~~~")
        case 3:
            print("<<<<<<<<------->>>>>>>")

    for i in range(repeats):
        print(text)
    
    match bord:
        case 1:
            print("+-------=======------+")
        case 2:
            print("~~~~~~~~:::::::~~~~~~~")
        case 3:
            print("<<<<<<<<------->>>>>>>")


generator(1, 3, "Hello World");