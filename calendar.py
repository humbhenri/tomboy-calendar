#!/usr/bin/python
# Calendar gui with tomboy support

import sys
try:
    import pygtk
    pygtk.require("2.0")
except:
    pass
try:
    import gtk.glade
except:
    sys.exit(1)
import tomboy

class Calendar:
    def __init__(self):
        self.glade_file = "/usr/share/tomboy-calendar/interface.glade"
        self.__get_widgets()
        self.__connect_events()
        self.tomboy = tomboy.Tomboy()
        self.context_id = self.statusBar.get_context_id("Statusbar example")
        self.__update_statusbar(None)

    def __get_widgets(self):
        self.wTree = gtk.glade.XML(self.glade_file)        
        self.window = self.wTree.get_widget("MainWindow")
        self.calendar = self.wTree.get_widget("Calendar")
        self.statusBar = self.wTree.get_widget("Statusbar")
        self.noteview = self.wTree.get_widget("NoteView")
        self.__create_note_view()
        self.notelist = gtk.ListStore(str)
        self.noteview.set_model(self.notelist)
        self.entry = self.wTree.get_widget("searchEntry")

    def __create_note_view(self):
        title = "Note"
        colId = 0
        col = gtk.TreeViewColumn(title, gtk.CellRendererText(),
                                 text=colId)
        col.set_resizable(True)
        col.set_sort_column_id(colId)
        self.noteview.append_column(col)

    def __append_note(self, note_title):
        self.notelist.append([note_title])

    def __row_activated(self, evt, path, column):
        it = self.notelist.get_iter(path)
        note = self.notelist.get_value(it, 0)
        self.tomboy.show_note(note)
        
    def __clear_note_list(self):
        self.notelist.clear()

    def __connect_events(self):
        if (self.window):
            self.window.connect("destroy", gtk.main_quit)
        dic = {"on_quitBtn_clicked": gtk.main_quit,
               "on_Calendar_day_selected": self.__dateSelected,
               "on_Calendar_month_changed": self.__update_statusbar,
               "on_NoteView_row_activated": self.__row_activated,
               "on_aboutBtn_clicked": self.__show_about_dialog,
               "on_searchBtn_clicked": self.__search_notes}
        self.wTree.signal_autoconnect(dic)

    def __search_notes(self, evt):
        input = self.entry.get_text()
        notes = self.tomboy.search_notes(input)
        self.__clear_note_list()


    def __dateSelected(self, evt):
        date = self.calendar.get_date()
        # calendar month is zero-based
        notes = self.tomboy.get_notes_from_date((date[0], date[1]+1, date[2]))
        self.__clear_note_list()
        for note in notes:
            self.__append_note(note)

    def __update_statusbar(self, evt):
        month = self.calendar.get_date()[1] + 1
        text = str(self.tomboy.total_notes_month(month))
        self.statusBar.push(self.context_id, text + " notes")

    def __show_about_dialog(self, evt):
        dialog = self.wTree.get_widget("aboutdialog")
        dialog.run()
        dialog.destroy()

if __name__=="__main__":
    app = Calendar()
    gtk.main()
