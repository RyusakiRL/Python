import sqlite3

class Characters:
    def __init__(self, name, health, energy):
        self.name = name
        self.health = health
        self._energy = energy 

class Warrior(Characters):
    def __init__(self, name, health, energy, fury=0):
        super().__init__(name, health, energy)
        self._fury = fury

class Runner(Characters):
    def __init__(self, name, health, energy, extra_energy=50):
        super().__init__(name, health, energy)
        self._extra_energy = extra_energy
    
connection = sqlite3.connect("chars.db")
cursor = connection.cursor()

def save():
    cursor.execute("SELECT name, health, char_class, energy FROM chars")
    saving_auto = cursor.fetchall()

    for charact in saving_auto:
        name, health, char_class, energy = charact

        match char_class.lower():
            case "warrior":
                Warrior(name=name, health=health, energy=energy)
            case "runner":
                Runner(name=name, health=health, energy=energy)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS chars(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        health TEXT NOT NULL,
        char_class TEXT NOT NULL,
        energy INTEGER NOT NULL
        )""")

while True:
    
    print("====================MAIN MENU====================")
    print("Select a option:")
    action = str(input("[new char] [rest] [exit] [delete]\n"))

    match action.lower():
        case "new char":
            name_char = str(input("Insert the name of your character: "))

            cursor.execute("SELECT name FROM chars WHERE name = ?", (name_char,))
            results = cursor.fetchone()
            

            while results is not None:
                print(f"The name {name_char} already exists, enter a new name")
                name_char = str(input("Insert the a new name for you character: "))

                cursor.execute("SELECT name FROM chars WHERE name = ?", (name_char,))
                results = cursor.fetchone()

                
            class_user = str(input("Choose a class:\n[Warrior] [Runner]\n"))

            while class_user.lower()!= "warrior" and class_user.lower()!="runner":
                class_user=str(input("These class don't exist, please insert a valid name:\n [Warrior] [Runner]\n"))

            energy_user = 100
            health = 100

            cursor.execute("""
                INSERT INTO chars(name, health, char_class, energy)
                VALUES(?, ?, ?, ?)
                """, (name_char, health, class_user, energy_user))                   
            connection.commit()
            
            print("Character added with sucess")

        case "rest":
            name_char = str(input("Insert the name of the character to rest: "))
            
            cursor.execute("""
            UPDATE chars
            SET energy = 100
            WHERE name = ?
            """, (name_char,))
            connection.commit()

            print(f"The {name_char} recovered your energy")

        case "delete":
            uid = int(input("Insert the char uid: "))
            cursor.execute("DELETE FROM chars WHERE id = ?", (uid, ))
            connection.commit()
            print("Character deleted forever!")

        case "exit":
            break

        case _:
            print("Invalid command")