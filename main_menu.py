# Orchard Manager Main Menu

from tree import Appletree
from orchard_recordkeeping import save_trees, load_trees
from edit_orchard import add_tree, view_trees, search_trees, edit_tree

def print_menu():
    print("\n--- Orchard Manager ---")
    print("1. View all trees")
    print("2. Search trees")
    print("3. Add tree")
    print("4. Edit tree")
    print("5. Save and exit\n")

def main():
    trees = load_trees()
    print(f"Welcome to the Orchard Manager!")
    
    while True:
        print_menu()
        usr_input = input("Choose an option (1-5): ").strip()

        if usr_input ==     "1":
            view_trees(trees)
            print("---\nPress Enter to return to the main menu.")
            input()

        elif usr_input ==   "2":
            search_trees(trees)
            print("---\nPress Enter to return to the main menu.")
            input()

        elif usr_input ==   "3":
            add_tree(trees)

        elif usr_input ==   "4":
            edit_tree(trees)

        elif usr_input ==   "5":
            save_trees(trees)
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid choice, please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
