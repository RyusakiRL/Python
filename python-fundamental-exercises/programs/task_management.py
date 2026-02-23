class Task:
    def __init__(self, title, description, status="pending"):
        self.title = title
        self.description = description
        self.status = status
    
    def conclude(self):
        self.status = "concluded"
        print(f"The task {self.title}\n Status: {self.status}")

    def see_details(self):
        print(f"============{self.title}============")
        print(f"{self.description}")
        print(f"Status:{self.status}")

tasks = []

while True:
    action = input("Type: 'new task', 'conclude', 'see details' or 'exit': ")
    
    if action == "new task":
        titles = input("Insert the title: ")
        description = input("=============Insert the description=============\n")

        new_task = Task(titles, description)
        tasks.append(new_task)
    
    elif action == "conclude":
        name_title = input("Type the title of the task: ")
        task_concluded = None

        for search in tasks:
            if search.title == name_title:
                task_concluded = search
                break
        if task_concluded!=None:
            task_concluded.conclude()
        else:
            print("Title don't encountered")
    
    elif action == "see details":
        name_title = input("Type the title of the task: ")
        task_details = None

        for search in tasks:
            if search.title == name_title:
                task_details = search
                break
        if task_details!= None:
            task_details.see_details()
        else:
            print("Title don't encountered")
    
    elif action == "exit":
        break

    else:
        print("Invalid command!!!")
