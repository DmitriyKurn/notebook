from colorama import Fore, Style


class View(object):

    @staticmethod
    def show_number_point_list(notes):
        for note in notes:
            print(Fore.GREEN + '+++++++++++++++++++++++++++++++++++++++++++' + Style.RESET_ALL)
            print(note)

    @staticmethod
    def show_note(note):
        print(Fore.YELLOW)
        print(note)
        print(Style.RESET_ALL)

    @staticmethod
    def show_empty_list_message():
        print(Fore.YELLOW)
        print('Cписок заметок пустой!')
        print(Style.RESET_ALL)

    @staticmethod
    def display_note_id_not_exist(note_id):
        print(Fore.RED)
        print('Заметка с id: {} не найдена!'.format(note_id))
        print(Style.RESET_ALL)

    @staticmethod
    def display_note_id_exist(note_id):
        print(Fore.RED)
        print('Заметка с id: {} уже есть!'.format(note_id))
        print(Style.RESET_ALL)

    @staticmethod
    def display_note_stored(note_id):
        print(Fore.GREEN)
        print('Заметка с id: {} успешно добавлена!'.format(note_id))
        print(Style.RESET_ALL)

    @staticmethod
    def display_note_updated(note_id):
        print(Fore.GREEN)
        print('Заметка с id: {} обновлена успешно!'.format(note_id))
        print(Style.RESET_ALL)

    @staticmethod
    def display_note_deletion(note_id):
        print(Fore.RED)
        print('Заметка с id: {} удалена успешно!'.format(note_id))
        print(Style.RESET_ALL)

    @staticmethod
    def display_all_notes_deletion():
        print(Fore.RED)
        print('Все заметки удалены!')
        print(Style.RESET_ALL)