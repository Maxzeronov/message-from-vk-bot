#импорт нужных классов библиотеки PyQt5
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

#импорт sys
import sys

#класс окна программы
class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Тест")
        self.setGeometry(500, 450, 550, 450)
        self.text = QtWidgets.QLabel(self)
        self.text.setText("Отправка сообщения от имени бота!")
        self.text.move(100,100)
        self.text.adjustSize()
        self.text.setFont(QtGui.QFont("SansSerif", 20))

def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()