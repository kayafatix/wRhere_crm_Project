# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crm_basvuru.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import gspread

from crm_ara_ekran import *  

credentials = 'wrherecrmproject-609f4fae20b3.json'

gc = gspread.service_account(filename=credentials)

spreadsheet = gc.open('Basvurular')

worksheet = spreadsheet.get_worksheet(0)  # İstenilen çalışma sayfasının indeksini değiştirin


class crm_basvurular(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 553)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_4.setGeometry(QtCore.QRect(30, 140, 811, 311))
        self.tableWidget_4.setStyleSheet("")
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(11)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(10, item)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 20, 131, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 80, 271, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 80, 241, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 241, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(590, 80, 241, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(590, 20, 241, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 880, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #Tüm Başvurular  düğmesi işlevi
        self.pushButton.clicked.connect(self.show_all_applicants)
        
        # ARA düğmesi işlevi
        self.pushButton_3.clicked.connect(self.search)
        
        # Mentor ataması Olanlar düğmesi işlevi
        self.pushButton_2.clicked.connect(self.show_assigned_mentor)

        # Mentor ataması Olmayanlarlar düğmesi işlevi
        self.pushButton_4.clicked.connect(self.show_unassigned_mentor)

        # Tercihler Ekranina Geri Don düğmesi işlevi
        self.pushButton_5.clicked.connect(self.go_to_preferences_screen)
    
    def show_all_applicants(self):
        # Proje Gonderilmis Olanlar düğmesi işlevi
        # Drive'dan proje gönderilmiş adayları alıp tableWidget_3'e ekleyebilirsiniz.
                        
        # Google Sheets'ten sadece proje gönderilmiş adayları, proje gönderilme tarihi ve geri dönüş tarihini alın
        all_applicants_data = worksheet.get_all_values()  # Tüm verileri al, her satır bir liste içerir

        # Eski verileri temizle
        self.tableWidget_4.setRowCount(0)

        # Verileri tableWidget_4'e ekleyin
        row_index = 0
        for data_row in all_applicants_data:
            time_stamp = data_row[0]
            name_surname = data_row[1]  
            mail = data_row[2]  
            mobile_phone_number = data_row[3]  
            post_code = data_row[4]
            province = data_row[5]
            current_situation = data_row[6]
            attend_ITPH = data_row[7]
            economic_situation = data_row[8]
            attending_language_course = data_row[9]
            foreign_language_level = data_row[10]            
            
            self.tableWidget_4.insertRow(row_index)
            self.tableWidget_4.setItem(row_index, 0, QtWidgets.QTableWidgetItem(time_stamp))
            self.tableWidget_4.setItem(row_index, 1, QtWidgets.QTableWidgetItem(name_surname))
            self.tableWidget_4.setItem(row_index, 2, QtWidgets.QTableWidgetItem(mail))
            self.tableWidget_4.setItem(row_index, 3, QtWidgets.QTableWidgetItem(mobile_phone_number))
            self.tableWidget_4.setItem(row_index, 4, QtWidgets.QTableWidgetItem(post_code))
            self.tableWidget_4.setItem(row_index, 5, QtWidgets.QTableWidgetItem(province))
            self.tableWidget_4.setItem(row_index, 6, QtWidgets.QTableWidgetItem(current_situation))
            self.tableWidget_4.setItem(row_index, 7, QtWidgets.QTableWidgetItem(attend_ITPH))
            self.tableWidget_4.setItem(row_index, 8, QtWidgets.QTableWidgetItem(economic_situation))
            self.tableWidget_4.setItem(row_index, 9, QtWidgets.QTableWidgetItem(attending_language_course))
            self.tableWidget_4.setItem(row_index, 10, QtWidgets.QTableWidgetItem(foreign_language_level))
            
            row_index += 1

    def search(self):        
        name_list = worksheet.get_all_values()  # Tüm verileri al, her satır bir liste içerir

    # ARA düğmesi işlevi - İsim soyisim arama
        keyword = self.lineEdit.text().strip().lower()  # Kullanıcının girdiği metni al
    # Eşleşen sonuçları temizle
        self.tableWidget_4.setRowCount(0)
    # Eşleşen sonuçları tableWidget_4'e ekleyin
        row_index = 0
        for data_row in name_list:
            time_stamp = data_row[0]
            name_surname = data_row[1]  
            mail = data_row[2]  
            mobile_phone_number = data_row[3]  
            post_code = data_row[4]
            province = data_row[5]
            current_situation = data_row[6]
            attend_ITPH = data_row[7]
            economic_situation = data_row[8]
            attending_language_course = data_row[9]
            foreign_language_level = data_row[10]
                    
            if keyword in name_surname.lower():
                self.tableWidget_4.insertRow(row_index)
                self.tableWidget_4.setItem(row_index, 0, QtWidgets.QTableWidgetItem(time_stamp))
                self.tableWidget_4.setItem(row_index, 1, QtWidgets.QTableWidgetItem(name_surname))
                self.tableWidget_4.setItem(row_index, 2, QtWidgets.QTableWidgetItem(mail))
                self.tableWidget_4.setItem(row_index, 3, QtWidgets.QTableWidgetItem(mobile_phone_number)) 
                self.tableWidget_4.setItem(row_index, 4, QtWidgets.QTableWidgetItem(post_code)) 
                self.tableWidget_4.setItem(row_index, 5, QtWidgets.QTableWidgetItem(province)) 
                self.tableWidget_4.setItem(row_index, 6, QtWidgets.QTableWidgetItem(current_situation)) 
                self.tableWidget_4.setItem(row_index, 7, QtWidgets.QTableWidgetItem(attend_ITPH)) 
                self.tableWidget_4.setItem(row_index, 8, QtWidgets.QTableWidgetItem(economic_situation)) 
                self.tableWidget_4.setItem(row_index, 9, QtWidgets.QTableWidgetItem(attending_language_course))
                self.tableWidget_4.setItem(row_index, 10, QtWidgets.QTableWidgetItem(foreign_language_level))                                  
                row_index += 1
    
    def show_assigned_mentor(self):                             
        # Google Sheets'ten sadece proje gönderilmiş adayları, proje gönderilme tarihi ve geri dönüş tarihini alın
        all_applicants_data = worksheet.get_all_values()  # Tüm verileri al, her satır bir liste içerir

        # Eski verileri temizle
        self.tableWidget_4.setRowCount(0)

        # Verileri tableWidget_4'e ekleyin
        row_index = 0
        for data_row in all_applicants_data:
            time_stamp = data_row[0]
            name_surname = data_row[1]  
            mail = data_row[2]  
            mobile_phone_number = data_row[3]  
            post_code = data_row[4]
            province = data_row[5]
            current_situation = data_row[6]
            attend_ITPH = data_row[7]
            economic_situation = data_row[8]
            attending_language_course = data_row[9]
            foreign_language_level = data_row[10]
            mentor_status = data_row[20]
            

            # Sadece mentor ataması yapılanları göster
            if mentor_status == "OK": 
                
                self.tableWidget_4.insertRow(row_index)
                self.tableWidget_4.setItem(row_index, 0, QtWidgets.QTableWidgetItem(time_stamp))
                self.tableWidget_4.setItem(row_index, 1, QtWidgets.QTableWidgetItem(name_surname))
                self.tableWidget_4.setItem(row_index, 2, QtWidgets.QTableWidgetItem(mail))
                self.tableWidget_4.setItem(row_index, 3, QtWidgets.QTableWidgetItem(mobile_phone_number)) 
                self.tableWidget_4.setItem(row_index, 4, QtWidgets.QTableWidgetItem(post_code)) 
                self.tableWidget_4.setItem(row_index, 5, QtWidgets.QTableWidgetItem(province)) 
                self.tableWidget_4.setItem(row_index, 6, QtWidgets.QTableWidgetItem(current_situation)) 
                self.tableWidget_4.setItem(row_index, 7, QtWidgets.QTableWidgetItem(attend_ITPH)) 
                self.tableWidget_4.setItem(row_index, 8, QtWidgets.QTableWidgetItem(economic_situation)) 
                self.tableWidget_4.setItem(row_index, 9, QtWidgets.QTableWidgetItem(attending_language_course))
                self.tableWidget_4.setItem(row_index, 10, QtWidgets.QTableWidgetItem(foreign_language_level))
                # self.tableWidget_4.setItem(row_index, 20, QtWidgets.QTableWidgetItem(mentor_status))
                row_index += 1
    
    def show_unassigned_mentor(self):                             
        # Google Sheets'ten sadece proje gönderilmiş adayları, proje gönderilme tarihi ve geri dönüş tarihini alın
        all_applicants_data = worksheet.get_all_values()  # Tüm verileri al, her satır bir liste içerir

        # Eski verileri temizle
        self.tableWidget_4.setRowCount(0)

        # Verileri tableWidget_4'e ekleyin
        row_index = 0
        for data_row in all_applicants_data:
            time_stamp = data_row[0]
            name_surname = data_row[1]  
            mail = data_row[2]  
            mobile_phone_number = data_row[3]  
            post_code = data_row[4]
            province = data_row[5]
            current_situation = data_row[6]
            attend_ITPH = data_row[7]
            economic_situation = data_row[8]
            attending_language_course = data_row[9]
            foreign_language_level = data_row[10]
            mentor_status = data_row[20]
            

            # Sadece mentor ataması yapılanları göster
            if mentor_status == "ATANMADI" or mentor_status == "": 
                
                self.tableWidget_4.insertRow(row_index)
                self.tableWidget_4.setItem(row_index, 0, QtWidgets.QTableWidgetItem(time_stamp))
                self.tableWidget_4.setItem(row_index, 1, QtWidgets.QTableWidgetItem(name_surname))
                self.tableWidget_4.setItem(row_index, 2, QtWidgets.QTableWidgetItem(mail))
                self.tableWidget_4.setItem(row_index, 3, QtWidgets.QTableWidgetItem(mobile_phone_number)) 
                self.tableWidget_4.setItem(row_index, 4, QtWidgets.QTableWidgetItem(post_code)) 
                self.tableWidget_4.setItem(row_index, 5, QtWidgets.QTableWidgetItem(province)) 
                self.tableWidget_4.setItem(row_index, 6, QtWidgets.QTableWidgetItem(current_situation)) 
                self.tableWidget_4.setItem(row_index, 7, QtWidgets.QTableWidgetItem(attend_ITPH)) 
                self.tableWidget_4.setItem(row_index, 8, QtWidgets.QTableWidgetItem(economic_situation)) 
                self.tableWidget_4.setItem(row_index, 9, QtWidgets.QTableWidgetItem(attending_language_course))
                self.tableWidget_4.setItem(row_index, 10, QtWidgets.QTableWidgetItem(foreign_language_level))
                # self.tableWidget_4.setItem(row_index, 20, QtWidgets.QTableWidgetItem(mentor_status))
                row_index += 1              
                
                
    
    def go_to_preferences_screen(self):
        self.crm_ara_ekran = crm_ara_ekran() 
        self.crm_ara_ekran.setupUi(MainWindow)
        MainWindow.show()
            

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Basvurular "))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "tarih"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "isim soyisim "))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "mail"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "telefon"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "posta kodu"))
        item = self.tableWidget_4.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "eyalet"))
        item = self.tableWidget_4.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "su anki durum"))
        item = self.tableWidget_4.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "ekonomik durum"))
        item = self.tableWidget_4.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "dil kursu takibi "))
        item = self.tableWidget_4.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "ing seviye "))
        item = self.tableWidget_4.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "felm seviye "))
        self.pushButton_3.setText(_translate("MainWindow", "ARA"))
        self.pushButton_2.setText(_translate("MainWindow", "Mentor Gorusmesi Tanimlananlar"))
        self.pushButton.setText(_translate("MainWindow", "Tum Basvurular"))
        self.pushButton_4.setText(_translate("MainWindow", "Mentor Gorusmesi Tanimlanmayanlar"))
        self.pushButton_5.setText(_translate("MainWindow", "Tercihler Ekranina Geri Don"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = crm_basvurular()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())