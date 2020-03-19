# classwork
def shopping():
    action = input("What would you like to do?")
    l = []

    while(action != "exit"):
        if action == "add":
            item = input("What would you like to add?")
            l += [item]
            l.sort()
            print(item + " added to shopping list")
        elif action == "delete":
            item = input("What would you like to delete?")
            index = l.index(item)
            del l[index]
            print(item + " deleted from shopping list")
        elif action == "view":
            print("Your shopping list is now: ")
            for i in l:
                print(i)
        elif action == "clear":
            l = []
            print("Shopping list cleared")
        else:
            print("Enter 'add', 'delete', 'view', 'clear', ' or exit'")

        action = input("What would you like to do?")

shopping()
