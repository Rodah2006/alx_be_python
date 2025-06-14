shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"'{item}' has been added to your shopping list.\n")
    elif choice == "2":
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed from your shopping list.\n")
        else:
            print(f"'{item}' is not in your shopping list.\n")
    elif choice == "3":
        if shopping_list:
            print("Your shopping list:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
        else:
            print("Your shopping list is empty.")
        print()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
