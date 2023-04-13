phone_book = []
start_phone_book = []
PATH = 'phone_book.txt'

def get_pb():
    global phone_book
    return phone_book

def load_file():
    global phone_book, start_phone_book
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(':')
        phone_book.append({'name': contact[0],
                          'phone': contact[1],
                          'comment': contact[2]})
    start_phone_book = phone_book.copy()
 
def save_file():
    global phone_book
    data = []
    for contact in phone_book:
        data.append(':'.join([value for value in contact.values()]))
    data = '\n'.join(data)
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(data)

def add_contact(contact: dict):
    global phone_book
    phone_book.append(contact)

def exit_pb() -> bool:
    global phone_book, start_phone_book
    if phone_book == start_phone_book:
        return False
    else:
        return True
    

def search_contact(contact: dict):
    global phone_book
    data_search = []
    for elem in phone_book:
        if contact['name'].lower() == elem.get("name").lower():
            data_search.append(elem)
        elif contact['phone'].lower() == elem.get("phone").lower():
            data_search.append(elem)
        elif contact['comment'].lower() == elem.get("comment").lower():
            data_search.append(elem)
    return data_search

def changed_contact(id: int, changed_contact: dict) -> list:
    global phone_book
    phone_book.pop(id - 1)
    phone_book.insert(id - 1, {'name': changed_contact.get("name"), 
                               'phone': changed_contact.get("phone"), 
                               'comment': changed_contact.get("comment")})
    return phone_book

def delete_contact(id: int) -> list:
    global phone_book
    phone_book.pop(id - 1)
    return phone_book
    

    