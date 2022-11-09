import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QFrame,  QColorDialog, QApplication

from PyQt5.QtGui import QColor


class Dialog(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        # начальный цвет черный
        col = QColor(0, 0, 0)

        # надпись на кнопке
        self.btn = QPushButton('Поменять цвет', self)
        # положение кнопки 
        self.btn.move(20, 20)

        # при нажатии будет диалоговое окошко
        self.btn.clicked.connect(self.Dialog_window)

        
        # параметры цветного прямоугольника
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }"
            % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        
        # параметры рамки основного окна
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Выбор цвета')
        self.show()


    def Dialog_window(self):
        # диалоговое окно с выбором цвета
        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Dialog()
    sys.exit(app.exec_())