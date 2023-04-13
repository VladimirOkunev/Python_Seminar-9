import view
import model
import text_fields as txt


def start_pb():
    while True:
        choice = view.main_menu()
        if choice == 1:
            model.load_file()
            view.print_info(txt.load_successful)
        if choice == 2:
            model.save_file()
            view.print_info(txt.save_successful)
        if choice == 3:
            pb = model.get_pb()
            view.show_contacts(pb, txt.no_contact_or_file)
        if choice == 4:
            contact = view.new_contact()
            model.add_contact(contact)
            view.print_info(txt.new_contact_successfu)
        if choice == 5:
            search = view.search_contac()
            result = model.search_contact(search)
            view.show_contacts(result, txt.search_no_result)
        if choice == 6:
            pb = model.get_pb()
            view.show_contacts(pb, txt.no_contact_or_file)
            id = view.contact_id(pb)
            changed_contact = view.change_contact()
            model.changed_contact(id, changed_contact)
        if choice == 7:
            pb = model.get_pb()
            view.show_contacts(pb, txt.no_contact_or_file)
            id = view.contact_id(pb)
            model.delete_contact(id)
        if choice == 8:
            if model.exit_pb():
                if view.confirm(txt.is_changed):
                    model.save_file()
            view.print_info(txt.bye_bye)
            exit()
