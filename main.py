grocery_items = []

print("Dit is je boodschappenlijst")

def add_grocery(item):
    grocery_items.append(item)

def show_grocery_list():
    print("Je boodschappen:")
    for items in grocery_items:
        print(items)

def delete_grocery(item):
    for items in grocery_items:
        if items == item:
            grocery_items.remove(item)
            return
    print("Artikel staat niet op het lijstje")

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