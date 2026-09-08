tasks = []

while True:
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        for task in tasks:
            print("-", task)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
