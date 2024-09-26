shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            add_item ()
        elif choice == '2':
            # Prompt for and remove an item
            remove_item ()
        elif choice == '3':
            # Display the shopping list
            display_items ()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
def add_item():
    item_name = input("Enter the item name to add to the list: ")
    shopping_list.append(item_name)

def remove_item():
    item_name = input("enter tha name of the item to remove: ")
    if item_name in shopping_list:
        shopping_list.remove(item_name)
    else:
        print("Item dose not exist.")

def display_items():
    for item in shopping_list:
        print(item)  

if __name__ == "__main__":
    main()