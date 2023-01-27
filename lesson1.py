[
    {
        "id": 1,
        "name": "Ball",
        "price": 100.0
    }
]

import json

FILE_PATH = 'data.json'

def get_data(ge_price = None, le_price = None):
    with open('data.json') as file:
        data = json.load(file)
    if ge_price:
        new_data = [i for i in data if i['price'] >= ge_price]
        return new_data
    if le_price:
        new_data = [i for i in data if i['price'] <= le_price]
        return new_data
        
    return data
    
def get_one_data(id):
    data = get_data()
    one_data = [i for i in data if i['id'] == id]
    if one_data:
        return one_data
    return


def post_data():
    data = get_data()
    maxid = max([i['id'] for i in data ])
    data.append({
    'id':maxid + 1,
    'name': input('enter the name: '),
    'price': float(input('enter the price: '))
    })
    with open('data.json', 'w') as file:
        json.dump(data, file)
        with open('data.json','w' ) as file:
            json.load(data, file)
    
    return 'No such file '

    
def get_update():
    data = get_data()
    data_update = [i for i in data if i['id'] == id]

    if data_update:
        index_ = data.index(data_update[0])
        data[index_]['name'] = input('enter the new name:    ')
        data[index_]['price'] = float(input('enter new price:    '))
        json.dump(data, open(FILE_PATH, 'w'))
        
        return 'Updated'


def delete():
    data = get_data()
    delete_data = [i for i in data if i['id'] == id]

    if delete_data:
        data.remove(delete_data[0])
        json.dump(data, open(FILE_PATH, 'w'))
        return 'Deleted'
    return 'no such file'
