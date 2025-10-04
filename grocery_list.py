
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