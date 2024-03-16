def todo_list():
    tasks = []

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Quit")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter task: ")
            tasks.append(task)
        elif choice == '2':
            if tasks:
                task = input("Enter task to remove: ")
                if task in tasks:
                    tasks.remove(task)
                else:
                    print("Task not found!")
            else:
                print("No tasks to remove!")
        elif choice == '3':
            print("Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
        elif choice == '4':
            break
        else:
            print("Invalid input")

todo_list()
