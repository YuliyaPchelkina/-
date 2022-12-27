from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import *

import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 760)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.data_base = 0
        
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        
        
        self.tables = QTabWidget(self.centralwidget)
        self.tables.setFixedSize(820, 500)
        self.tables.move(0, 260)

        self.tab_1 = QTableWidget()
        self.tab_2 = QTableWidget()
        self.tab_3 = QTableWidget()
        self.tab_4 = QTableWidget()
        self.tab_5 = QTableWidget()

       
        self.tables.addTab(self.tab_1, "Full table")
        self.tables.addTab(self.tab_2, "Female only")
        self.tables.addTab(self.tab_3, "Rings > 10")
        self.tables.addTab(self.tab_4, "One column")
        self.tables.addTab(self.tab_5, "One line")
        
        
        
        self.bt1 = QtWidgets.QPushButton(self.centralwidget)
        self.bt1.setGeometry(QtCore.QRect(30, 30, 180, 50))
        self.bt1.setCheckable(False)
        self.bt1.setObjectName("bt1")
        self.bt1.clicked.connect(self.female_only)
        
        
        self.bt2 = QtWidgets.QPushButton(self.centralwidget)
        self.bt2.setGeometry(QtCore.QRect(30, 110, 180, 50))
        self.bt2.setObjectName("bt2")
        self.bt2.clicked.connect(self.rings_more_then_10)
        
        
        
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(240, 30, 180, 50))
        self.comboBox.setEditable(True)
        self.comboBox.setModelColumn(0)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.currentTextChanged.connect(self.select_one_column)
        
        
        
        
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(460, 30, 240, 140))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        
        self.line_text = QtWidgets.QLabel(self.groupBox)
        self.line_text.setGeometry(QtCore.QRect(30, 10, 180, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        
        
        self.line_number = QtWidgets.QLineEdit(self.groupBox)
        self.line_number.setGeometry(QtCore.QRect(30, 50, 180, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_number.setFont(font)

        self.bt3 = QtWidgets.QPushButton(self.groupBox)
        self.bt3.setGeometry(QtCore.QRect(30, 80, 180, 50))
        self.bt3.setObjectName("bt3")
        self.bt3.clicked.connect(self.select_one_line)
        
       
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 824, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionSet_connection = QtWidgets.QAction(MainWindow)
        self.actionSet_connection.setObjectName("actionSet_connection")
        self.actionSet_connection.triggered.connect(self.set_connection)
        
        self.actionClose_connection = QtWidgets.QAction(MainWindow)
        self.actionClose_connection.setObjectName("actionClose_connection")
        self.actionClose_connection.setEnabled(False)
        self.actionClose_connection.triggered.connect(self.close_connection)

        
        self.menuMenu.addAction(self.actionSet_connection)
        self.menuMenu.addAction(self.actionClose_connection)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        
        self.bt1.setText(_translate("MainWindow", "Female only"))
        self.bt2.setText(_translate("MainWindow", "Rings > 10"))
        
        self.comboBox.setCurrentText(_translate("MainWindow", "Select Column"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Select Column"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Sex"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Length"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Diameter"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Height"))
        self.comboBox.setItemText(5, _translate("MainWindow", "WholeWeight"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Rings"))
        
        self.line_text.setText(_translate("MainWindow", "Enter number of line (less then 1445)"))
        self.line_number.setText(_translate("MainWindow", "1"))
        self.bt3.setText(_translate("MainWindow", "Select Line"))
        
        
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionSet_connection.setText(_translate("MainWindow", "Set connection"))
        self.actionClose_connection.setText(_translate("MainWindow", "Close connection"))

        
        
    def print_row(self, table, rows):
        col = 0
        row = table.rowCount()
        table.setRowCount(row + 1)
        for i in rows:
            cell = QTableWidgetItem(str(i))
            table.setItem(row, col, cell)
            col += 1

        
    
    def set_connection(self):
        conn = sqlite3.connect('DataBaseAbalone.db')
        
        # Объект cursor позволяет делать SQL-запросы к базе
        cur = conn.cursor()
        
        # заголовок
        columnsName = []
        titul_list = cur.execute('PRAGMA table_info(users)').fetchall()
        self.tab_1.setColumnCount(len(titul_list))
        for name in titul_list:
            columnsName.append(name[1])
        
        self.tab_1.rowCount()
        self.tab_1.setHorizontalHeaderLabels(columnsName)

        # обращение ко всем строкам в таблице users
        records = cur.execute('SELECT * FROM users').fetchall()
        if self.tab_1.rowCount() == 0:
            for rows in records:
                self.print_row(self.tab_1, rows)

        self.tables.setCurrentIndex(0)

        
        self.data_base = conn
        
        self.actionClose_connection.setEnabled(True)
        self.actionSet_connection.setEnabled(False)
        
    
    
    def close_connection(self): 
        self.data_base.close()
        self.data_base = 0
        
        for i in range(self.tables.count()):
            self.tables.widget(i).setRowCount(0)
            self.tables.widget(i).setColumnCount(0)

        
        self.actionClose_connection.setEnabled(False)
        self.actionSet_connection.setEnabled(True)
        

    def female_only(self):
        if self.data_base !=0:
            columnsName = []
            titul_list = self.data_base.cursor().execute('PRAGMA table_info(users)').fetchall()
            self.tab_2.setColumnCount(len(titul_list))
            for name in titul_list:
                columnsName.append(name[1])
        
            self.tab_2.rowCount()
            self.tab_2.setHorizontalHeaderLabels(columnsName)
            
            # только женщины
            records = self.data_base.cursor().execute('SELECT * FROM users').fetchall()
            if self.tab_2.rowCount() == 0:
                for rows in records:
                    if rows[1] == 'F':
                        self.print_row(self.tab_2, rows)

            self.tables.setCurrentIndex(1)
            

            
    def rings_more_then_10(self):
        if self.data_base !=0:
            columnsName = []
            titul_list = self.data_base.cursor().execute('PRAGMA table_info(users)').fetchall()
            self.tab_3.setColumnCount(len(titul_list))
            for name in titul_list:
                columnsName.append(name[1])
        
            self.tab_3.rowCount()
            self.tab_3.setHorizontalHeaderLabels(columnsName)
            
            # количество колец больше 10
            records = self.data_base.cursor().execute('SELECT * FROM users').fetchall()
            if self.tab_3.rowCount() == 0:
                for rows in records:
                    if rows[6] > 10:
                        self.print_row(self.tab_3, rows)

            self.tables.setCurrentIndex(2)

    def select_one_column(self):
        column_name = self.comboBox.currentText()
        if column_name != 'Select Column':
            if self.data_base !=0:
                # только один столбец
                records = self.data_base.cursor().execute('SELECT ' + column_name + ' FROM users').fetchall()
            
                self.tab_4.setColumnCount(1)
                columnsName = [column_name]
            
                self.tab_4.rowCount()
                self.tab_4.setHorizontalHeaderLabels(columnsName)
                self.tab_4.setRowCount(0)
            
                for rows in records:
                    self.print_row(self.tab_4, rows)
            
                self.tables.setCurrentIndex(3)
                
            
    def select_one_line(self):
        number = int(self.line_number.text())
        
        if self.data_base !=0:
            columnsName = []
            titul_list = self.data_base.cursor().execute('PRAGMA table_info(users)').fetchall()
            self.tab_5.setColumnCount(len(titul_list))
            for name in titul_list:
                columnsName.append(name[1])
        
            self.tab_5.rowCount()
            self.tab_5.setHorizontalHeaderLabels(columnsName)
            self.tab_5.setRowCount(0)
            
            # только одна строка
            records = self.data_base.cursor().execute('SELECT * FROM users').fetchall()
            #if self.tab_5.rowCount() == 0:
            self.print_row(self.tab_5, records[number-1])

            self.tables.setCurrentIndex(4)

            
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
