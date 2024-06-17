import datetime

#This is an empty list to store tasks
tasks = []

def display_instructions():
    """
    Function to display the to_do list instructions
    """
    print("""
    ===== To-Do List Instructions =====
    Welcome to the To-Do list application!
    You can manage your tasks with the following options:
    1. Display to-do list : View all tasks currently in the list.
    2. Add a task : Enter a new task to add to your to-do list.
    3. Remove a task : Choose a task by its index to remove the task from your list.
    4. View all tasks : View all tasks you have on your to-do list.
    5. Quit : Exit the application.
    ===================================== 
    
    """)

#Function to display the to-do list
def display_tasks():
        if not tasks:
            print("\U0001F4ED Your to-do list is empty.")
        else:
            print("\U0001F4CB Your to-do list.")
            for index,task in enumerate(tasks, start=1):
                print(f"{index}. {task['description']} - Due: {task['due-date']} {task['due-time']}")


#Function to add task to the to-do list
def add_task():
        description = input("Enter task description: ") 
        due_date = input("Enter due date (YYYY-MM-DD): ")
        due_time = input("Enter due-time (HH:MM): ")
        try:
             datetime.datetime.strptime(due_date, "%Y-%m-%d")
             datetime.datetime.strptime(due_time, "%H:%M")       
        except ValueError:
             print("\U0000274C Invalid date or time format. Task not added.")
             return

        task = {
            "description": description,
            "due_date": due_date,
            "due_time": due_time
         }
        
        tasks.append(task)
        print(f"\U00002705 Task '{description}' added to your to-do list")   
    

#Function to remove a task from the to-do list
def remove_task():
    display_tasks()
    if tasks:
        try:
            index = int(input("Enter the number of the task to remove")) - 1
            if 0 <= index < len(tasks):
                removed_task = tasks.pop(index)
                print(f"\U0001F4ED Task '{description}' removed from your to-do list.")
            else:
                print("\U0000274C Invalid index")
        except ValueError:
            print("\U0000274C Invalid input. Please enter a number.")
    else:
        print("\U0001F4ED Your to-do list is already empty")            

#function to view all tasks on the to-do list
def view_tasks():
    display_tasks() 


def main():
        
        """
        Main function to run the to-do list application
        """
        print("\U0001F4CB Welcome to the to-do list app \U0001F4CB")
        while True:
            print("\n === To-Do List Menu===")
            print("Please select one of the following options")
            print("------------------------------------------")
            print("1. Display to-do list")
            print("2. Add a task")
            print("3. Remove a task")
            print("4. View all tasks")
            print("5. Quit")

            choice = input("Enter your choice (1-5): ")
            
            if (choice == "1"):
                display_tasks()
            elif (choice == "2"):
                add_task()
            elif (choice == "3"):
                remove_task()
            elif (choice == "4"):
                view_tasks()
            elif (choice == "5"):
                print("Quit application...")
                break
            else:
                print("\U0000274C Invalid choice, Please enter a number from 1 to 5")
                
            print(" Goodbye \U0001F44B \U0001F44B ")

# Run the main function to start the application
if __name__ == "__main__":
    main()


