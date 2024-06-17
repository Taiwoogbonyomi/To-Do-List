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


