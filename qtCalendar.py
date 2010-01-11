import sys 
try:
    from PyQt4 import QtGui, QtCore
except:
    print('Python Qt4 bindings not installed!')
    sys.exit(0)
from qtGui import Ui_Frame
from tomboy import Tomboy 


class MyForm(QtGui.QFrame):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.tomboy = Tomboy()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        frect = self.frameGeometry()
        frect.moveCenter(QtGui.QDesktopWidget().availableGeometry().center())
        self.move(frect.topLeft())
        self.setupActions()
        self.notes = []

    def popupSearch(self, item):
        self.tomboy.search_notes(str(item.text()))

    def showNotes(self):
        if self.notes == []:
            return
        popup = QtGui.QFrame(self)
        popup.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.Popup)
        popup.resize(150, 100)
        popup.setGeometry(QtGui.QCursor.pos().x(), QtGui.QCursor.pos().y(), 200, 200)
        layout = QtGui.QVBoxLayout()
        listWidget = QtGui.QListWidget()
        for note in self.notes:
            listWidget.addItem(QtCore.QString(note))
        layout.addWidget(listWidget)
        self.connect(listWidget, QtCore.SIGNAL('itemDoubleClicked(QListWidgetItem*)'), self.popupSearch)
        self.connect(listWidget, QtCore.SIGNAL('itemDoubleClicked(QListWidgetItem*)'), popup.close)
        popup.setLayout(layout)
        popup.show()

    def search(self):
        self.tomboy.search_notes(str(self.ui.searchEdit.text()))

    def dateChanged(self, date):
        year = date.year()
        month = date.month()
        day = date.day()
        self.notes = self.tomboy.get_notes_from_date((year, month, day))        
        self.showNotes()

    def setupActions(self):
        self.connect(self.ui.quitButton, QtCore.SIGNAL('clicked()'), self.close)
        self.connect(self.ui.searchEdit, QtCore.SIGNAL('returnPressed()'), self.search)
        self.connect(self.ui.calendarWidget, QtCore.SIGNAL('clicked(QDate)'), self.dateChanged)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
