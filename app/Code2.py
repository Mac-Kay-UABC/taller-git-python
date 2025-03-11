todo_list = []

while True:
    print("\nTo-Do List:")
    for idx, task in enumerate(todo_list, start=1):
        print(f"{idx}. {task}")
    
    print("\nOptions: [1] Add Task  [2] Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        new_task = input("Enter a new task: ")
        todo_list.append(new_task)
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")