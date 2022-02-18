from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3 

cnx = sqlite3.connect('todolist.db')
c = cnx.cursor()
c.execute("""CREATE TABLE if not exists todo(listitem text) """)
cnx.commit()
cnx.close()



class Ui_root(object):
    def setupUi(self, root):
        root.setObjectName("root")
        root.resize(507, 583)
        root.setFixedSize(507,583)
        icon = QtGui.QIcon.fromTheme("mousepad")
        root.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(root)
        self.centralwidget.setObjectName("centralwidget")
        self.entry = QtWidgets.QLineEdit(self.centralwidget)
        self.entry.setGeometry(QtCore.QRect(10, 0, 491, 51))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Serif")
        font.setPointSize(16)
        self.entry.setFont(font)
        self.entry.setObjectName("entry")
        self.add_item = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.addit())
        self.add_item.setGeometry(QtCore.QRect(10, 70, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.add_item.setFont(font)
        self.add_item.setObjectName("add_item")
        self.clear_all = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.clearit())
        self.clear_all.setGeometry(QtCore.QRect(270, 70, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.clear_all.setFont(font)
        self.clear_all.setObjectName("clear_all")
        self.remove_item = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.removeit())
        self.remove_item.setGeometry(QtCore.QRect(140, 70, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.remove_item.setFont(font)
        self.remove_item.setObjectName("remove_item")
        self.lista = QtWidgets.QListWidget(self.centralwidget)
        self.lista.setGeometry(QtCore.QRect(10, 120, 491, 411))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Serif")
        font.setPointSize(14)
        self.lista.setFont(font)
        self.lista.setObjectName("lista")
        self.save = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.saveit())
        self.save.setGeometry(QtCore.QRect(400, 70, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.save.setFont(font)
        self.save.setObjectName("save")
        root.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(root)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 507, 24))
        self.menubar.setObjectName("menubar")
        root.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(root)
        self.statusbar.setObjectName("statusbar")
        root.setStatusBar(self.statusbar)

        self.retranslateUi(root)
        QtCore.QMetaObject.connectSlotsByName(root)
        self.grab_all()

    def grab_all(self):
        cnx = sqlite3.connect('todolist.db')
        c = cnx.cursor()
        c.execute("SELECT * FROM todo ")
        records = c.fetchall()
        cnx.commit()
        cnx.close()
        for record in records:
            self.lista.addItem(str(record[0]))


    def addit(self):
        item = self.entry.text()
        self.lista.addItem(item)
        self.entry.setText("")


    def removeit(self):
        selected = self.lista.currentRow()
        self.lista.takeItem(selected)


    def clearit(self):
        self.lista.clear()

    def saveit(self):
        cnx = sqlite3.connect('todolist.db')
        c = cnx.cursor()
        c.execute("DELETE FROM todo;",)
        
        items = []
        for i in range(self.lista.count()):
            items.append(self.lista.item(i))

        for item in items:
            c.execute("INSERT INTO todo VALUES (:item)",
            {
                'item': item.text(),
            })
        cnx.commit()
        cnx.close()
        msg = QMessageBox()
        msg.setWindowTitle("Saving Progress")
        msg.setText("Your Tasks Have Been Saved To The DataBase Successfully !")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()



    def retranslateUi(self, root):
        _translate = QtCore.QCoreApplication.translate
        root.setWindowTitle(_translate("root", "To Do List"))
        self.add_item.setText(_translate("root", "Add Item"))
        self.clear_all.setText(_translate("root", "Clear"))
        self.remove_item.setText(_translate("root", "Delete Item"))
        self.save.setText(_translate("root", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    root = QtWidgets.QMainWindow()
    ui = Ui_root()
    ui.setupUi(root)
    root.show()
    sys.exit(app.exec_())
