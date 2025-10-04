grocery_items = []

def add_grocery(item):
    grocery_items.append(item)

def show_grocery_list():
    print("Je boodschappen:")
    for items in grocery_items:
        print(items)

def delete_grocery(item):
    if item in grocery_items:
        grocery_items.remove(item)
    else:
        print("Artikel staat niet op het lijstje")