import sqlite3

sqlconnection = sqlite3.connect("data_task.db")
cursorcon = sqlconnection.cursor()

class Task:
    def __init__(self, uid, title, stats):
        self.id = uid
        self.title = title
        self.stats = stats

    def complete_task(self):
        self.stats = "completed"

class Bugfix(Task):
    def __init__(self, uid, title, stats, priority):
        super().__init__(uid, title, stats)
        self.priority = priority

    def details(self):
        print(f"The task {self.title} have a {self.priority} priority.")

class Feature(Task):
    def __init__(self, uid, title, stats, estimated_time):
        super().__init__(uid, title, stats)
        self.estimated_time = estimated_time
    
    def details(self):
        print(f"The task {self.title} have a estimated time of {self.estimated_time} hours.")


cursorcon.execute("""CREATE TABLE IF NOT EXISTS data_task(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        stats TEXT NOT NULL,
                        type TEXT NOT NULL,
                        priority TEXT,
                        time INTEGER)""")

def save():
    cursorcon.execute("SELECT * FROM data_task")
    table = cursorcon.fetchall()

    list_temporary = []

    for tasking in table:
        uid, title, stats, types, priority, timing = tasking

        match types:
            case "estimated time":
                new_task_class = Feature(uid=uid, title=title, stats=stats, estimated_time=timing )
            case "task with priorities":
                new_task_class = Bugfix(uid=uid, title=title, stats=stats, priority=priority)
        
        list_temporary.append(new_task_class)

    return list_temporary

tasks_list = save()

while True:
    action = str(input("Choose between:\n [add task] [list pending tasks] [complete a task] [see details] [delete] [exit]\n"))

    match action.lower():

        case "add task":
            new_title = str(input("Insert a title: "))
            
            cursorcon.execute("SELECT title FROM data_task WHERE title = ?", (new_title,))
            title_existence = cursorcon.fetchone()

            while title_existence is not None:
                new_title = str(input("The task already exists, insert a new a task: "))

                cursorcon.execute("SELECT title FROM data_task WHERE title = ?", (new_title,))
                title_existence = cursorcon.fetchone()

            type_task = str(input("Insert [estimated time] or [task with priorities]\n"))

            while type_task.lower()!="estimated time" and type_task.lower()!="task with priorities":
                type_task = str(input("Insert a valid command:\n [estimated time] or [task with priorities]\n"))


            if type_task== "estimated time":
                try:
                    stats = "pending"
                    time = int(input("Insert the estimated time for do the task: "))
                    cursorcon.execute("""INSERT INTO data_task(title, stats, type, time)
                                        VALUES(?, ?, ?, ?)""",
                                        (new_title, stats, type_task, time))
                    sqlconnection.commit()

                    addinguid = cursorcon.lastrowid

                    new_task = Feature(uid=addinguid, title=new_title, stats=stats, estimated_time=time)
                    tasks_list.append(new_task)
                    print("Task added with sucess")

                except ValueError:
                    print("Insert a integer number")

            elif type_task == "task with priorities":
                prioring = str(input("Insert the priority:\n [low] [medium] [high]\n"))

                while prioring.lower()!="low" and prioring.lower()!="medium" and prioring.lower()!="high":
                    prioring = str(input("Insert a valid priority:\n [low] [medium] [high]\n"))

                stats = "pending"

                cursorcon.execute("""INSERT INTO data_task(title, stats, type, priority)
                                     VALUES(?, ?, ?, ?)""", 
                                     (new_title, stats, type_task, prioring))
                sqlconnection.commit()
                
                addinguid = cursorcon.lastrowid
                new_task = Bugfix(uid=addinguid, title=new_title, stats=stats, priority=prioring)
                tasks_list.append(new_task)
                print("Task added with sucess")

        case "list pending tasks":
            cursorcon.execute("SELECT title FROM data_task WHERE stats=?", ("pending",))
            pending_tasks = cursorcon.fetchall()

            for pend_tasks in tasks_list:
                if pend_tasks.stats == "pending":
                    print(f"The task: {pend_tasks.title} is pending")
            
            if not pending_tasks:
                print("Not have any pending task")
            
        case "complete a task":
            title_name = str(input("Insert the title of completed task: "))
            title_existence = False
            for titles in tasks_list:
                if titles.title == title_name:
                    title_existence = True
                    titles.complete_task()

                    cursorcon.execute("""
                        UPDATE data_task
                        SET stats = ?
                        WHERE title = ?
                        """, ("completed", title_name))
                    sqlconnection.commit()

                    print("Congratulations for the completed task")
                    break
            if not title_existence:
                print("The title task don't exists")

        case "see details":
            title_name = str(input("Insert the title of completed task: "))
            title_existence = None

            for titles in tasks_list:
                if titles.title == title_name:
                    title_existence = titles
                    break
            
            if title_existence!=None:
                title_existence.details()
            else:
                print("Name not encountered")

        case "delete":
            title_name = str(input("Insert the title "))
            cursorcon.execute("DELETE FROM data_task WHERE title = ?", (title_name,))

            title_existence = False
            for titles in tasks_list:
                if titles.title == title_name:
                    title_existence = True
                    cursorcon.execute("DELETE FROM data_task WHERE title = ?", (title_name,))
                    tasks_list.remove(titles)
                    print("Deleted with sucess")
                    break
            
            if not title_existence:
                print("Title not encountered")

        case "exit":
            break

        case _:
            print("Invalid command")