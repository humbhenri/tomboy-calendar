# Module for tomboy interaction

import dbus
import time

class Tomboy:
    def __init__(self):
        try:
            bus = dbus.SessionBus()
            obj = bus.get_object("org.gnome.Tomboy",
                                 "/org/gnome/Tomboy/RemoteControl")
            self.__interface = dbus.Interface(obj,
                                "org.gnome.Tomboy.RemoteControl")
            self.__update()
        except:
            print "Error: can't find tomboy"
            exit(1)

    def show_note(self, title):
        self.__interface.DisplayNote(self.__interface.FindNote(title))

    def get_notes_from_date(self, date):
        """ Expects a tuple (year, month, day) and returns a list
        of note titles created in that date. """
        notes = []
        for note in self.__all_notes:
            note_date = time.localtime(self.__interface.GetNoteCreateDate(note))
            if note_date[0:3] == date:
                notes.append(self.__interface.GetNoteTitle(note))
        return notes

    def total_notes_month(self, month):
        """ Expects a number between 1-12 representing a month."""
        total = 0
        for note in self.__all_notes:
            note_date = time.localtime(self.__interface.GetNoteCreateDate(note))
            if note_date[1] == month:
                total += 1
        return total
        
    def __update(self):
        self.__all_notes = self.__interface.ListAllNotes()

    def search_notes(self, text):
        self.__interface.DisplaySearchWithText(text)

