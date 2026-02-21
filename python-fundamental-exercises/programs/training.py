class Character:
    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.power = 10
        self.speed = 10
    
    def train_power(self):
        if self.energy>=20:
            
            self.energy -= 20
            self.power+=5
            return True
        else:
            print("Insufficient energy!!")
            return False
    
    def train_speed(self):
        if self.energy>=15:
            
            self.energy -=15
            self.speed +=5
            return True
        else:
            print("Insufficient energy!!")
            return False
        
    def rest(self):
        self.energy = 100
    

char1 = input("Type the name of your first character: ")

character1 = Character(char1)
while True:
    action = input("Type to train: 'power', 'speed', 'rest', 'see status' or 'exit': ")

    if action == "power":
        character1.train_power()
        if character1.energy>=15:
            print(f"Train of power concluded. Energy: {character1.energy}")
    elif action == "speed":
        character1.train_speed()
        if character1.energy>=15:
            print(f"Train of speed concluded. Energy: {character1.energy}")

    elif action == "rest":
        character1.rest()
        print("Character rest. Energy is fulled")
    elif action == 'see status':
        print(f"\n========Status of {character1.name}========")
        print(f"Energy: {character1.energy}")
        print(f"Power: {character1.power}")
        print(f"Speed: {character1.speed}")
        print("=================================================")

    elif action == "exit":
        break

    else:
        print("invalid command!")       
    
