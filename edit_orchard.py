
from tree import Appletree

def add_tree(trees):

    correct_input = False
    while correct_input == False:
        tree_id = input("Tree ID (e.g. A1): ").strip()
        if not tree_id:
            return  # "blank' "" input, User chose to cancel adding a tree
        
        elif any(t.tree_id == tree_id for t in trees): # Check for a duplicate ID in list
            print("A tree with that ID already exists. Please choose a different ID.")
            print("Or press 'Enter' to cancel.")

        else:
            correct_input = True #tree_id is unique, exit loop
          
    variety = input("Variety (e.g. Ingrid Marie): ").strip()

    while True:
        year_input = input("Planted year (e.g. 2015): ").strip()
        try:
            planted_year = int(year_input)
            break
        except ValueError: #must be integer
            print("Please enter a valid year as a number.")

    harvest_time = input("Expected harvest time (e.g. September): ").strip()

    new_tree = Appletree(tree_id, variety, planted_year, harvest_time)
    trees.append(new_tree)
    print(f"Tree '{tree_id}' added.")


def view_trees(trees):
    if not trees:
        print("No trees registered yet.")
        return

    print(f"\n--- Orchard: {len(trees)} tree(s) ---")
    for tree in trees:
        print(tree)


def find_tree_by_id(trees, tree_id):
    # return the Tree object with this ID from list, or None if not found.
    # used by search_trees and edit_tree
    for tree in trees:
        if tree.tree_id == tree_id:
            return tree
    return None


def search_trees(trees):
    if not trees:
        print("No trees registered yet.")
        return

    tree_id = input("Tree ID to edit: ").strip()
    tree = find_tree_by_id(trees, tree_id)

    if not tree:
        print("No matching trees found.")
    else:
        print(f"\n--- Tree found ---")
        print(tree)


def edit_tree(trees):
    if not trees:
        print("No trees registered yet.")
        return

    print(view_trees(trees))
    tree_id = input("Tree ID to edit: ").strip()
    tree = find_tree_by_id(trees, tree_id)

    if tree is None:
        print("No tree found with that ID.")
        return

    while True:
        print("\n--- Edit Tree ---")
        print("1. Change variety")
        print("2. Change planted year")
        print("3. Change expected harvest time")
        print("4. Add/Modify problems/diseases")
        print("5. Mark/Unmark as pruned this year")
        print("6. Remove tree")
        print("7. Back to main menu\n")

        usr_choice = input("Choose an option (1-7): ").strip()

        # Change 'variety'
        if  usr_choice ==   "1": 
            new_variety = input("New variety: ").strip()
            tree.variety = new_variety
            print(f"Variety updated for tree '{tree_id}'.")

        # Change 'planted year'    
        elif usr_choice ==  "2":
            while True:
                year_input = input("New planted year: ").strip()
                try:
                    new_year = int(year_input)
                    tree.planted_year = new_year
                    print(f"Planted year updated for tree '{tree_id}'.")
                    break
                except ValueError:
                    print("Please enter a valid year as a number.")

        #Change 'harvest time(eg. [month])'
        elif usr_choice ==  "3":
            new_harvest_time = input("New expected harvest time: ").strip()
            tree.harvest_time = new_harvest_time
            print(f"Expected harvest time updated for tree '{tree_id}'.")

        #Add/Mofify 'problems/diseases(eg. [bark damege, brown rot])'
        elif usr_choice ==  "4":
            print(f"Current problems/diseases: {', '.join(tree.problems) if tree.problems else 'None'}")
            input_problem = input("Add a new problem/disease, name problem to remove or leave blank to skip: ").strip()
            if input_problem == "":
                print("No changes made to problems/diseases.")
            elif input_problem in tree.problems:
                tree.problems.remove(input_problem)
                print(f"Problem '{input_problem}' removed for tree '{tree_id}'.")
            elif input_problem:
                tree.problems.append(input_problem)
                print(f"Problem '{input_problem}' added for tree '{tree_id}'.")

        #Mark/Unmark 'pruned this year'
        elif usr_choice ==  "5":
            print(f"Current pruned status: {'Yes' if tree.pruned_this_year else 'No'}")
            tree.pruned_this_year = not tree.pruned_this_year
            status = "marked as pruned" if tree.pruned_this_year else "unmarked as pruned"
            print(f"Tree '{tree_id}' {status} this year.")

        #Remove tree
        elif usr_choice ==  "6":
            confirm_rm = input(f"Are you sure you want to remove tree '{tree_id}'? (y/n): ").strip().lower()
            if confirm_rm == "y":
                trees.remove(tree)
                print(f"Tree '{tree_id}' removed from the orchard.")
                break 
            else:
                print("Tree removal canceled.")

        # No choice, back to main menu
        elif usr_choice == "" or usr_choice == "7":
            break  
