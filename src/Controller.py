class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_notes(self):
        notes = self.model.read_notes()
        self.view.show_number_point_list(notes)

    def show_note(self, note_id):
        try:
            note = self.model.read_note(note_id)
            self.view.show_note(note)
        except ValueError:
            self.view.display_note_id_not_exist(note_id)

    def create_note(self, note):
        note_id = self.model.create_note(note)
        self.view.display_note_stored(note_id)

    def update_note(self, note_id, note):
        if self.note_id_exist(note_id):
            self.model.update_note(note_id, note)
            self.view.display_note_updated(note_id)
        else:
            self.view.display_note_id_not_exist(note_id)

    def delete_note(self, note_id):
        if self.note_id_exist(note_id):
            try:
                self.model.delete_note(note_id)
                self.view.display_note_deletion(note_id)
            except ValueError:
                self.view.display_note_id_not_exist(note_id)
        else:
            self.view.display_note_id_not_exist(note_id)

    def delete_all_notes(self):
        self.model.delete_all_notes()
        self.view.display_all_notes_deletion()

    def notes_exist(self):
        notes = self.model.read_notes()
        if len(notes) == 0:
            return False
        else:
            return True

    def note_id_exist(self, search_id):
        notes = self.model.read_notes()
        for note in notes:
            if note.note_id == search_id:
                return True
        else:
            return False