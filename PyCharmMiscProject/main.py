from task_manager import TaskManager
from menu import show_menu


manager = TaskManager()
manager.load_from_file("tasks.json")

while True:
    show_menu()

    choice = input("Выберите действие: ")

    if choice == "1":
        manager.show_tasks()

    elif choice == "2":
        title = input("Название задачи: ")
        try:
            priority = int(input("Приоритет: "))
        except ValueError:
            print("Нужно ввести число")
            continue
        manager.add_task(title, priority)
        manager.save_to_file("tasks.json")

    elif choice == "3":
        try:
            task_id = int(input("ID: "))
        except ValueError:
            print("Нужно ввести число")
            continue
        manager.mark_done(task_id)
        manager.save_to_file("tasks.json")

    elif choice == "4":
        try:
            task_id = int(input("ID: "))
        except ValueError:
            print("Нужно ввести число")
            continue
        manager.delete_task(task_id)
        manager.save_to_file("tasks.json")

    elif choice == "5":
        query = input("Введите текст: ")
        results = manager.search_tasks(query)

        for task in results:
            print(task)

    elif choice == "6":
        tasks = manager.get_done_tasks()

        for task in tasks:
            print(task)

    elif choice == "7":
        tasks = manager.get_undone_tasks()

        for task in tasks:
            print(task)

    elif choice == "8":
        tasks = manager.sort_by_priority()

        for task in tasks:
            print(task)

    elif choice == "0":
        manager.save_to_file("tasks.json")
        break