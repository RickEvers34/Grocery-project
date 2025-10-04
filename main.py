grocery_items = []

print("Dit is je boodschappenlijst")

while True:
    print("kies een actie: add, delete, show, exit")
    command = str(input())
    if command == "add":
        print("wat wil je toevoegen:")
        add_grocery(input())
    elif command == "show":
        show_grocery_list()
    elif command == "delete":
        print("wat wil je verwijderen:")
        delete_grocery(input())
    elif command == "exit":
        break
    else:
        print("onbekend")