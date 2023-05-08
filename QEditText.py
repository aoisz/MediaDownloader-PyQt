from PyQt5 import QtCore, QtGui, QtWidgets
class MyQTextEdit(QtWidgets.QTextEdit):
    def focusInEvent(self, e):
        if(self.toPlainText() == "Paste link here"):
            self.setPlainText("")
        super(MyQTextEdit, self).focusInEvent(e)

    def focusOutEvent(self, e):
        if(self.toPlainText() == ""):
            self.setPlainText("Paste link here")
        super(MyQTextEdit, self).focusOutEvent(e)