todo_list = []

while True:
    print("\nMarket List:")
    for idx, task in enumerate(todo_list, start=1):
        print(f"{idx}. {task}")
    
    print("\nOptions: [1] Add Item  [2] Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        new_task = input("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA: ")
        todo_list.append(new_task)
    elif choice == "2":
        print("Skill Issue")
        break
    else:
        print("Invalid choice, Skill Issue.")