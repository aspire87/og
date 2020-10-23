import sys
from threading import Thread
from PyQt5 import QtWidgets, QtCore


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 100, 100, 50))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Test"))
        self.pushButton.setText(_translate("Dialog", "OK"))


class Ui_MainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        self.pushButton = QtWidgets.QPushButton(mainWindow)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 100, 60))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("mainWindow", "Test"))
        self.pushButton.setText(_translate("mainWindow", "Push Me!"))


class TestDialog(QtWidgets.QDialog):
    signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(TestDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # This message simply needs to go away
        self.ui.pushButton.clicked.connect(self.close)

    def show_message(self):
        # Use this to display the pop-up so the text can be altered
        super(TestDialog, self).exec_()
        self.signal.emit()


class Main(QtWidgets.QMainWindow):
    signal = QtCore.pyqtSignal()

    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dialog = TestDialog()
        self.dialog_done = False

        self.ui.pushButton.clicked.connect(self.start_thread)

    def complete_dialog(self):
        self.dialog_done = True

    def wait_for_dialog(self):
        while not self.dialog_done:
            pass
        self.dialog_done = False

    def start_thread(self):
        t = Thread(target=self.show_dialog)
        t.daemon = True
        t.start()

    def show_dialog(self):
        # Do lots of background stuff here
        self.signal.emit()
        # Wait for the dialog to get closed
        self.wait_for_dialog()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    dialog = TestDialog()
    window.signal.connect(dialog.show_message)
    dialog.signal.connect(window.complete_dialog)
    sys.exit(app.exec_())