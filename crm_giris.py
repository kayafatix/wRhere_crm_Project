# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crm_giris.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from crm_ara_ekran import *

import gspread

# Kimlik doğrulama bilgilerini yükleyin
credentials = 'wrherecrmproject-609f4fae20b3.json'

# Gspread ile oturumu başlatın
gc = gspread.service_account(filename=credentials)

# Google Sheets elektronik tabloyu açın
spreadsheet = gc.open('Kullanicilar')

# Çalışma sayfasını seçin
worksheet = spreadsheet.get_worksheet(0)  # İstenilen çalışma sayfasının indeksini değiştirin

# Şimdi, çalışma sayfası ile çalışabilirsiniz


cell_value = worksheet.acell('A1').value
print(f'A1 Hücresi Değeri: {cell_value}')

# Belirli bir satırı okuma (örneğin, 2. satır)
row_values = worksheet.row_values(2)
print(f'2. Satır Değerleri: {row_values}')

# Belirli bir sütunu okuma (örneğin, A sütunu)
column_values = worksheet.col_values(1)
print(f'A Sütunu Değerleri: {column_values}')

all_values = worksheet.get_all_values()

print(all_values[0][1])




class crm_giris(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(606, 336)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 190, 171, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 70, 291, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 70, 151, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 141, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 120, 291, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 606, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        
        #GİRİŞ TIKLAMA YAPILDIĞI ZAMAN GİRİŞ KONTROLÜ İÇİN girisKontrol FONKSİYONUNA GİDİYOR. 
        self.pushButton.clicked.connect(self.girisKontrol)
        



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Giris"))
        self.pushButton.setText(_translate("MainWindow", "Giris"))
        self.label.setText(_translate("MainWindow", "Kullanici Adiniz"))
        self.label_2.setText(_translate("MainWindow", "Sifre"))

    def girisKontrol(self):
        kullaniciAdi = self.lineEdit_3.text()
        sifre=self.lineEdit_4.text()
        kontrol=okGirisKontrol(kullaniciAdi,sifre, all_values)
        #if kontrol:
        if kontrol:
            print("giriş Tamam")
            self.crm_ara_ekran = crm_ara_ekran()
            self.crm_ara_ekran.onceki_pencere = self
            #self.teacher = teacher()    
            self.crm_ara_ekran.setupUi(MainWindow)
            MainWindow.show()
            #sys.exit(app.exec_())
            #self.hide()
        

def okGirisKontrol(kullaniciAdi,sifre,tumVeriler):
    kontrol=False
    for row in tumVeriler:
        if (kullaniciAdi==row[0]):
            if sifre==row[1]:
                kontrol=True
    return kontrol

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = crm_giris()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
    
    