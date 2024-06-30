todo_list = []

def add_item(item):
    todo_list.append(item)
    print(f"'{item}' has been added to the to-do list.")

def view_items():
    if not todo_list:
        print("The to-do list is empty.")
    else:
        print("To-Do List:")
        for index, item in enumerate(todo_list, start=1):
            print(f"{index}. {item}")

def delete_item(index):
    if 0 <= index < len(todo_list):
        removed_item = todo_list.pop(index)
        print(f"'{removed_item}' has been removed from the to-do list.")
    else:
        print("Invalid index. Please try again.")

def menu():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add item")
        print("2. View items")
        print("3. Delete item")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(item)
        elif choice == '2':
            view_items()
        elif choice == '3':
            try:
                index = int(input("Enter the index of the item to delete: ")) - 1
                delete_item(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting the to-do list program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
