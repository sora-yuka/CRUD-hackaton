import json

FILE_PATH = "data.json"

def product_listing():
    try:
        with open("data.json") as file:
            data = json.load(file)
                
        if data == []:
            return "Product list is empty."
        return data

    except json.decoder.JSONDecodeError:
        with open(FILE_PATH, "w") as file:
            json.dump([], file)
        return "Product list is empty."
    
def product_retrieve_listing(id):
    data = product_listing()
    
    try:
        one_data = [i for i in data if i["id"] == id]
        
    except TypeError:
        return "Product list is empty."
    
    if one_data == []:
        return "The product you entered doesn't exist."
    return one_data

def product_creating():
    try:
        with open(FILE_PATH) as file:
            data = json.load(file)
    except json.decoder.JSONDecodeError:
        with open(FILE_PATH, "w") as file:
            json.dump([], file)
        with open(FILE_PATH, "r") as file:
            data = json.load(file)
    
    try:
        max_id = max([i["id"] for i in data])
    except ValueError:
        max_id = 0
    
    data.append(
        {
            "id": max_id + 1,
            "name": input("enter the name: ").capitalize(),
            "price": int(input("enter the price: "))
        }
    )
    with open("data.json", "w") as file:
        json.dump(data, file)
    
    return "You have successfully created product."

def product_updateting(id):
    data = product_listing()
    
    if data != "Product list is empty.":
        product = [i for i in data if i["id"] == id]

        if product:
            index_ = data.index(product[0])
            data[index_]["name"] = input("enter a new name:  ").capitalize()
            data[index_]["price"] = float(input("enter a new price:  "))
            json.dump(data, open(FILE_PATH, "w"))
            return "Product updated successfully."
        
    return "The product you entered doesn't exist."

def product_destroying(id):
    data = product_listing()
    
    if data != "Product list is empty.":
        product = [i for i in data if i["id"] == id]

        if product:
            data.remove(product[0])
            json.dump(data, open(FILE_PATH, "w"))
            return "Product deleted successfully."
    
    return "The product you entered doesn't exist."