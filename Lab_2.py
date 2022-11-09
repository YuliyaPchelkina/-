# Лабораторная работа №2. Пчелкина Ю.Ж. группа 6231-010402D.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, pyqtSignal, QObject

class usdHolder(QObject):
    update_signal = pyqtSignal(float, float)
    
    def __init__(self):
        super().__init__()
        self.value = ''
    # курс доллара будем считать по формуле: 3300 / цена за нефть в рублях = 3300 / (цена за нефть в долларах * k)
    def update_value(self, k: float, oil_price: float):
        self.value = 3300/(oil_price * k)

        
class rubHolder(QObject):
    update_signal = pyqtSignal(float, float)
    
    def __init__(self):
        super().__init__()
        self.value = ''
    # курс рубля будем считать по формуле: цена за нефть в долларах / 3300
    def update_value(self, k: float, oil_price: float):
        self.value = oil_price/3300

        
        

class My_MainWindow(object):
    
    def My_setup(self, MainWindow):
        
        self.rubHolder = rubHolder()
        self.usdHolder = usdHolder()

        
        # задаем внешний вид - размеры кнопок и полей, положение, шрифт, рамки и т.д.
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        MainWindow.setStyleSheet("background-color: rgb(227, 227, 227);")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.rezult_button = QtWidgets.QPushButton(self.centralwidget)
        self.rezult_button.setGeometry(QtCore.QRect(25, 350, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rezult_button.setFont(font)
        self.rezult_button.setStyleSheet("background-color:  rgb(181, 181, 181);")
        self.rezult_button.setCheckable(True)
        self.rezult_button.setObjectName("rezult_button")
        
        self.rub_name = QtWidgets.QLabel(self.centralwidget)
        self.rub_name.setGeometry(QtCore.QRect(25, 20, 140, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.rub_name.setFont(font)
        self.rub_name.setAutoFillBackground(False)
        self.rub_name.setStyleSheet("")
        self.rub_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.rub_name.setFrameShadow(QtWidgets.QFrame.Plain)
        self.rub_name.setMidLineWidth(1)
        self.rub_name.setObjectName("rub_name")
        
        self.baks_name = QtWidgets.QLabel(self.centralwidget)
        self.baks_name.setGeometry(QtCore.QRect(25, 90, 140, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.baks_name.setFont(font)
        self.baks_name.setAutoFillBackground(False)
        self.baks_name.setStyleSheet("")
        self.baks_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.baks_name.setFrameShadow(QtWidgets.QFrame.Raised)
        self.baks_name.setMidLineWidth(1)
        self.baks_name.setObjectName("baks_name")
        
        self.baks_result = QtWidgets.QLabel(self.centralwidget)
        self.baks_result.setGeometry(QtCore.QRect(175, 90, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.baks_result.setFont(font)
        self.baks_result.setAutoFillBackground(False)
        self.baks_result.setStyleSheet("")
        self.baks_result.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.baks_result.setFrameShadow(QtWidgets.QFrame.Raised)
        self.baks_result.setMidLineWidth(1)
        self.baks_result.setObjectName("baks__result")
        
        self.rub_result = QtWidgets.QLabel(self.centralwidget)
        self.rub_result.setGeometry(QtCore.QRect(175, 20, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.rub_result.setFont(font)
        self.rub_result.setAutoFillBackground(False)
        self.rub_result.setStyleSheet("")
        self.rub_result.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.rub_result.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.rub_result.setMidLineWidth(1)
        self.rub_result.setObjectName("rub_result")
        
        self.oil_name = QtWidgets.QLabel(self.centralwidget)
        self.oil_name.setGeometry(QtCore.QRect(25, 230, 140, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.oil_name.setFont(font)
        self.oil_name.setAutoFillBackground(False)
        self.oil_name.setStyleSheet("")
        self.oil_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.oil_name.setFrameShadow(QtWidgets.QFrame.Raised)
        self.oil_name.setMidLineWidth(1)
        self.oil_name.setObjectName("oil_name")
        
        self.koef_name = QtWidgets.QLabel(self.centralwidget)
        self.koef_name.setGeometry(QtCore.QRect(25, 160, 140, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.koef_name.setFont(font)
        self.koef_name.setAutoFillBackground(False)
        self.koef_name.setStyleSheet("")
        self.koef_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.koef_name.setFrameShadow(QtWidgets.QFrame.Raised)
        self.koef_name.setMidLineWidth(1)
        self.koef_name.setObjectName("koef_name")
        
        self.koef_mean = QtWidgets.QComboBox(self.centralwidget)
        self.koef_mean.setGeometry(QtCore.QRect(175, 170, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.koef_mean.setFont(font)
        self.koef_mean.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.koef_mean.setObjectName("koef_mean")
        self.koef_mean.addItem("")
        self.koef_mean.addItem("")
        self.koef_mean.addItem("")
        self.koef_mean.addItem("")
        self.koef_mean.addItem("")
        self.koef_mean.addItem("")
        self.koef_mean.addItem("")
        self.koef_mean.addItem("")
        self.koef_mean.addItem("")
        self.koef_mean.addItem("")
        self.koef_mean.addItem("")
        self.koef_mean.addItem("")
        self.koef_mean.addItem("")
        
        self.oil_price = QtWidgets.QLineEdit(self.centralwidget)
        self.oil_price.setGeometry(QtCore.QRect(175, 240, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.oil_price.setFont(font)
        self.oil_price.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.oil_price.setFrame(True)
        self.oil_price.setPlaceholderText("")
        self.oil_price.setObjectName("oil_price")
        
        self.rezult_text = QtWidgets.QLabel(self.centralwidget)
        self.rezult_text.setGeometry(QtCore.QRect(25, 300, 250, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(50)
        font.setKerning(False)
        self.rezult_text.setFont(font)
        self.rezult_text.setToolTipDuration(0)
        self.rezult_text.setAutoFillBackground(False)
        self.rezult_text.setStyleSheet("")
        self.rezult_text.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.rezult_text.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rezult_text.setMidLineWidth(1)
        self.rezult_text.setObjectName("rezult_text")
        
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # пусть для начала цена нефти = 96 USD/bbl
        self.oil = 96
        self.rub = 0.016
        self.baks = 61.36
 
      
       
        self.rubHolder.update_signal.connect(self.rubHolder.update_value)
        self.usdHolder.update_signal.connect(self.usdHolder.update_value)
        
        
        # вызываем функцию расчета
        self.rezult_button.clicked.connect(self.rezult_function)
        
        #self.show()

        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Course Generator"))
        self.rezult_button.setText(_translate("MainWindow", "rate calculation"))
        self.rub_name.setText(_translate("MainWindow", "Ruble rate (USD):"))
        self.baks_name.setText(_translate("MainWindow", "Dollar rate (RUR):"))
        self.baks_result.setText(_translate("MainWindow", "61.36"))
        self.rub_result.setText(_translate("MainWindow", "0.016"))
        self.oil_name.setText(_translate("MainWindow", "Oil  (USD/bbl):"))
        self.koef_name.setText(_translate("MainWindow", "Coefficient:"))
        self.koef_mean.setItemText(0, _translate("MainWindow", "60"))
        self.koef_mean.setItemText(1, _translate("MainWindow", "1"))
        self.koef_mean.setItemText(2, _translate("MainWindow", "2"))
        self.koef_mean.setItemText(3, _translate("MainWindow", "3"))
        self.koef_mean.setItemText(3, _translate("MainWindow", "5"))
        self.koef_mean.setItemText(4, _translate("MainWindow", "10"))
        self.koef_mean.setItemText(5, _translate("MainWindow", "15"))
        self.koef_mean.setItemText(6, _translate("MainWindow", "20"))
        self.koef_mean.setItemText(7, _translate("MainWindow", "25"))
        self.koef_mean.setItemText(8, _translate("MainWindow", "30"))
        self.koef_mean.setItemText(9, _translate("MainWindow", "35"))
        self.koef_mean.setItemText(10, _translate("MainWindow", "45"))
        self.koef_mean.setItemText(11, _translate("MainWindow", "50"))
        self.koef_mean.setItemText(12, _translate("MainWindow", "55"))
        self.oil_price.setText(_translate("MainWindow", "96"))
        self.rezult_text.setText(_translate("MainWindow", "rezult"))


    def rezult_function(self):
        # пусть для начала koeff = 60 (типа как курс доллара)
        
        #изначальная цена нефти
        start_oil_price = self.oil
        
        # считываем новую цену на нефть
        new_oil_price = float(self.oil_price.text())
        
        # считиваем коэффициент
        koeff = float(self.koef_mean.currentText())
        
        # начальные значения рубля и доллара
        rub = self.rub
        baks = self.baks
        
        
        # Если нефть выросла - рубль вырос. 
        if start_oil_price < new_oil_price:
            self.rubHolder.update_signal.emit(koeff, new_oil_price)
            rub = self.rubHolder.value
            baks = (1 / rub)

            # рост - зеленым, остальное черным
            self.rub_result.setStyleSheet("color: rgb(0, 150, 0);")
            self.baks_result.setStyleSheet("color: rgb(0, 0, 0);")
            self.rezult_text.setText("the value of the RUBLE has risen")
        
        # Если нефть упала - доллар вырос. Цену нефти в рублях считаем через коэффициент
        elif start_oil_price > new_oil_price:
            self.usdHolder.update_signal.emit(koeff, new_oil_price)
            baks = self.usdHolder.value
            rub = 1 / baks
            
            # рост - зеленым, остальное черным
            self.baks_result.setStyleSheet("color: rgb(0, 150, 0);")
            self.rub_result.setStyleSheet("color: rgb(0, 0, 0);")
            self.rezult_text.setText("the value of the DOLLAR has risen")
            
        
        # если изменений по нефти не не было - посчитали курс все равно (коэффициент мог поменяться)
        # и предлагаем поменять цену нефти
        else:
            self.rubHolder.update_signal.emit(koeff, new_oil_price)
            self.usdHolder.update_signal.emit(koeff, new_oil_price)
            
            self.rub_result.setStyleSheet("color: rgb(0, 0, 0);")
            self.baks_result.setStyleSheet("color: rgb(0, 0, 0);")

            self.rezult_text.setText("try to change the price of oil")        
            new_oil_price = start_oil_price

            
        # обновили значение нефти
        self.oil = new_oil_price
        self.oil_price.setText(str(new_oil_price))
        

        # записали значение рубля и доллара
        self.rub = rub
        self.baks = baks
        
        rub_str = str(rub)
        baks_str = str(baks)
        
        self.rub_result.setText(rub_str)
        self.baks_result.setText(baks_str)

     
        
        
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    prog = My_MainWindow()
    prog.My_setup(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
