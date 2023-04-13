import text_fields as txt

def main_menu() -> int:
    print(''' Главное меню: 
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти котнакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход''')
    while True:
        choice = input('Выберите пункт меню: ')
        if choice.isdigit and 0 < int(choice) < 9:
            return int(choice)
        else:
            print('Введите число от 1 до 8')

def print_info(message: str):
    print('\n' + '-' * len(message))
    print(message)
    print('-' * len(message) + '\n')

def show_contacts(book: list[dict], message: str):
    if book:
        print('\n' + '-' * 70)
        for n, contact in enumerate(book, 1):
            print(f'{n:>3}. {contact.get("name"):<20}'
                  f'{contact.get("phone"):<20}'
                  f'{contact.get("comment"):<20}')
        print('-' * 70 + '\n')
    else:
        print(message)

def new_contac() -> dict:
    print()
    name = input(txt.new_name)
    phone = input(txt.new_phone)
    comment = input(txt.new_comment)
    print()
    return{'name': name, 'phone': phone, 'comment': comment}

def confirm(message:str) -> bool:
    print()
    answer = input(message + ' y/n -> ')
    if answer.lower() == 'y':
        return True
    else:
        return False

def search_contac() -> dict:
    print()
    while True:
        select = int(input('Выберите критерии поиска (1 - имя, 2 - номер телефона, 3 - комментарий): '))
        if select == 1:
            search_name = input(txt.search_name)
            search_phone = ''
            search_comment = ''
            return{'name': search_name, 'phone': search_phone, 'comment': search_comment}
        elif select == 2:
            search_name = ''
            search_phone = input(txt.search_phone)
            search_comment = ''
            return{'name': search_name, 'phone': search_phone, 'comment': search_comment}
        elif select == 3:
            search_name = ''
            search_phone = ''
            search_comment = input(txt.search_comment)
            return{'name': search_name, 'phone': search_phone, 'comment': search_comment}
        else:
            print(txt.incorrect_result)


def change_contact() -> dict:
    print()
    name = input(txt.change_name)
    phone = input(txt.change_phone)
    comment = input(txt.change_comment)
    print()
    return{'name': name, 'phone': phone, 'comment': comment}

def contact_id(book: list[dict]) -> int:
    while True:
        id = int(input(txt.contact_id))
        print()
        if 0 < id < len(book) + 1:
            return int(id)
        else:
            print(txt.incorect_id)
            print()
            


