import datetime
from colorama import Fore, Style

from src.Controller import Controller
from src.NoteModel import NoteModel
from src.Note import Note
from src.View import View


def run():
    c = Controller(NoteModel("data/Notes.json"), View())

    while True:
        command = input(Fore.BLUE +
                        '1 - создать заметку\n'
                        '2 - прочитать заметки\n'
                        '3 - обновить заметку\n'
                        '4 - удалить заметку\n'
                        '5 - очистить заметки\n'
                        '7 - выход\n' +
                        'Сделайте Ваш выбор: '
                        + Style.RESET_ALL)
        
        if command == '7':
            break

        elif command == '1':
            print(Fore.GREEN + '\nСоздать заметку:' + Style.RESET_ALL)
            c.create_note(get_note_data())

        elif command == '2':
            if c.notes_exist():
                print(Fore.BLUE + '\nСписок всех заметок:' + Style.RESET_ALL)
                c.show_notes()
            else:
                View.show_empty_list_message()
                
        elif command == '3':
            if c.notes_exist():
                print(Fore.YELLOW + '\nОбновить заметку:' + Style.RESET_ALL)
                updated_id = int(get_number())
                if c.note_id_exist(updated_id):
                    print(Fore.YELLOW + 'Редактируемая заметка:' + Style.RESET_ALL)
                    c.show_note(updated_id)
                    if input(Fore.RED + 'Вы точно хотите обновить заметкy? (y/N): '
                         + Style.RESET_ALL).capitalize() == 'Y':
                        c.update_note(updated_id, get_note_data())
                        print(Fore.GREEN + 'Обновлённая заметка:' + Style.RESET_ALL)
                        c.show_note(updated_id)
                    else:
                        print(Fore.RED + 'Редактирование заметки отменено.' + Style.RESET_ALL)
                else:
                    View.display_note_id_not_exist(updated_id)
            else:
                View.show_empty_list_message()

        elif command == '4':
            if c.notes_exist():
                print(Fore.RED + '\nУдалить заметку:' + Style.RESET_ALL)
                delete_id = int(get_number())
                if c.note_id_exist(delete_id):
                    print(Fore.RED + 'Удаляемая заметка:' + Style.RESET_ALL)
                    c.show_note(delete_id)
                    if input(Fore.RED + 'Вы точно хотите удалить заметкy? (y/N): '
                         + Style.RESET_ALL).capitalize() == 'Y':
                        c.delete_note(delete_id)
                    else:
                        print(Fore.RED + 'Удаление заметки отменено.' + Style.RESET_ALL)
                else:
                    View.display_note_id_not_exist(delete_id)
            else:
                View.show_empty_list_message()

        elif command == '5':
            if c.notes_exist():
                print(Fore.RED + '\nУдалить все заметки:' + Style.RESET_ALL)
                if input(Fore.RED + 'Вы точно хотите удалить все заметки? (y/N): '
                         + Style.RESET_ALL).capitalize() == 'Y':
                    if c.notes_exist():
                        c.delete_all_notes()
                else:
                    print(Fore.RED + 'Удаление заметок отменено.' + Style.RESET_ALL)
            else:
                View.show_empty_list_message()
            

        else:
            print(Fore.RED + 'Команда не найдена' + Style.RESET_ALL)



def get_note_data():
    note_id = 0
    note_dt = datetime.datetime.now()
    note_title = input('Введите заголовок заметки: ')
    note_text = input('Введите заметку: ')
    return Note(note_id, note_dt, note_title, note_text)


def get_number():
    while True:
        get_choice = input('Введите id заметки: ')
        if get_choice.isdigit() and int(get_choice) > 0:
            return get_choice
        else:
            print(Fore.RED + 'Введите целое положительное число!' + Style.RESET_ALL)