def show_menu():
    print("\n~~~~~ TO-DO LIST ~~~~~")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")


def add_task(to_do_tasks):
    number_of_tasks = int(input('How many tasks do you want to add?: '))
    for _ in range(number_of_tasks):
        task = input('Enter the task: ')
        to_do_tasks.append({"task": task, "done": False})
        print(f'Task "{task}" added successfully!')


def show_tasks(to_do_tasks):
    green_color = "\033[92m"  # ANSI escape code for green text
    red_color = "\033[91m"  # ANSI escape code for red text
    reset_color = "\033[0m"  # ANSI escape code to reset color to default
    print('\n~~~~~ TASKS ~~~~~')
    for index, task in enumerate(to_do_tasks):
        green_check_mark = green_color + "\u2611" + reset_color
        red_empty_box = red_color + '\u2610' + reset_color
        status = green_check_mark if task['done'] else red_empty_box
        print(f"{index + 1}| {status} {task['task']}")


def mark_task_as_done(to_do_tasks):
    show_tasks(to_do_tasks)

    number_of_marks = int(input('How many tasks do you want to mark as "DONE!"?: '))
    for _ in range(number_of_marks):
        task_number = int(input('Enter the task number to mark as done: '))
        if 0 <= task_number - 1 < len(to_do_tasks):
            to_do_tasks[task_number - 1]["done"] = True
            print("Task marked as DONE!")
        else:
            print("Invalid task number. Please enter a valid number")


def to_do_list():
    to_do_tasks = []

    while True:
        show_menu()
        choice = int(input('Enter your choice (1-4): '))

        if choice == 1:
            add_task(to_do_tasks)
        elif choice == 2:
            show_tasks(to_do_tasks)
        elif choice == 3:
            mark_task_as_done(to_do_tasks)
        elif choice == 4:
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again with a number between 1 and 4.")


if __name__ == "__main__":
    to_do_list()
