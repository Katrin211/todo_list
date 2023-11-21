# Function to display the menu
def show_menu():
    print("\n===== To-Do List Menu =====")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Quit")


# Initial empty to-do list
to_do_list = []

# Main program loop
while True:
    # Display the menu
    show_menu()

    # Get user input
    choice = input("Enter your choice (1-4): ")

    # Process user input
    if choice == "1":
        # View To-Do List
        print("\n===== To-Do List =====")
        if not to_do_list:
            print("No tasks.")
        else:
            # Using enumerate to display tasks with their corresponding index
            for index, task in enumerate(to_do_list, 1):
                print(f"{index}. {task}")

    elif choice == "2":
        # Add Task
        task = input("Enter the task: ")
        to_do_list.append(task)
        print("Task added!")

    elif choice == "3":
        # Mark Task as Completed
        if not to_do_list:
            print("No tasks to mark as completed.")
        else:
            print("\n===== To-Do List =====")
            for index, task in enumerate(to_do_list, 1):
                print(f"{index}. {task}")

            # Get user input for the task to mark as completed
            task_index = int(input("Enter the task number to mark as completed: ")) - 1

            # Check if the entered index is valid
            if 0 <= task_index < len(to_do_list):
                # Remove the task at the specified index and store it in completed_task
                completed_task = to_do_list.pop(task_index)
                print(f"Task '{completed_task}' marked as completed!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        # Quit the program
        print("Exiting the To-Do List. Goodbye!")
        break

    else:
        # Handle invalid choices
        print("Invalid choice. Please enter a number between 1 and 4.")
