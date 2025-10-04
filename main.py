import grocery_list

print("Dit is je boodschappenlijst")

while True:
    print("kies een actie: add, delete, show, exit")
    command = str(input())
    if command == "add":
        print("wat wil je toevoegen:")
        grocery_list.add_grocery(input())
    elif command == "show":
        grocery_list.show_grocery_list()
    elif command == "delete":
        print("wat wil je verwijderen:")
        grocery_list.delete_grocery(input())
    elif command == "exit":
        break
    else:
        print("onbekend")