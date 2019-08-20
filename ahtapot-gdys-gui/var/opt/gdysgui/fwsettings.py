# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fwsettings.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import config_parser as CP
import gitlab_check as GC
import start_fw
import os
import subprocess
from time import sleep
from dmrlogger import Syslogger
from dmrlogger import Filelogger
import pexpect

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_FwSettingsWindow(QtGui.QWidget):
    def setupUi(self, FwSettingsWindow):
        FwSettingsWindow.setObjectName(_fromUtf8("FwSettingsWindow"))
        FwSettingsWindow.move(250,150)
        FwSettingsWindow.resize(740, 530)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FwSettingsWindow.sizePolicy().hasHeightForWidth())
        FwSettingsWindow.setSizePolicy(sizePolicy)
        FwSettingsWindow.setMinimumSize(QtCore.QSize(740, 530))
        FwSettingsWindow.setMaximumSize(QtCore.QSize(740, 530))
        FwSettingsWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 236, 207);"))
        self.centralwidget = QtGui.QWidget(FwSettingsWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 90, 711, 401))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_path = QtGui.QWidget()
        self.tab_path.setEnabled(False)
        self.tab_path.setObjectName(_fromUtf8("tab_path"))
        self.btn_config_save = QtGui.QPushButton(self.tab_path)
        self.btn_config_save.setGeometry(QtCore.QRect(550, 280, 101, 41))
        self.btn_config_save.setStyleSheet(_fromUtf8("background-color: rgb(159, 173, 176);"))
        self.btn_config_save.setObjectName(_fromUtf8("btn_config_save"))
        self.layoutWidget = QtGui.QWidget(self.tab_path)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 631, 281))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_13 = QtGui.QLabel(self.layoutWidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_2.addWidget(self.label_13)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_12 = QtGui.QLabel(self.layoutWidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_2.addWidget(self.label_12)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cmb_fw_file_name = QtGui.QComboBox(self.layoutWidget)
        self.cmb_fw_file_name.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.cmb_fw_file_name.setObjectName(_fromUtf8("cmb_fw_file_name"))
        self.verticalLayout.addWidget(self.cmb_fw_file_name)
        self.ledit_fw_copy_path = QtGui.QLineEdit(self.layoutWidget)
        self.ledit_fw_copy_path.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.ledit_fw_copy_path.setObjectName(_fromUtf8("ledit_fw_copy_path"))
        self.verticalLayout.addWidget(self.ledit_fw_copy_path)
        self.ledit_std_out_err = QtGui.QLineEdit(self.layoutWidget)
        self.ledit_std_out_err.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.ledit_std_out_err.setObjectName(_fromUtf8("ledit_std_out_err"))
        self.verticalLayout.addWidget(self.ledit_std_out_err)
        self.ledit_poc_ip = QtGui.QLineEdit(self.layoutWidget)
        self.ledit_poc_ip.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.ledit_poc_ip.setObjectName(_fromUtf8("ledit_poc_ip"))
        self.verticalLayout.addWidget(self.ledit_poc_ip)
        self.ledit_poc_user = QtGui.QLineEdit(self.layoutWidget)
        self.ledit_poc_user.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.ledit_poc_user.setObjectName(_fromUtf8("ledit_poc_user"))
        self.verticalLayout.addWidget(self.ledit_poc_user)
        self.ledit_poc_copy_path = QtGui.QLineEdit(self.layoutWidget)
        self.ledit_poc_copy_path.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.ledit_poc_copy_path.setObjectName(_fromUtf8("ledit_poc_copy_path"))
        self.verticalLayout.addWidget(self.ledit_poc_copy_path)
        self.ledit_poc_port_number = QtGui.QLineEdit(self.layoutWidget)
        self.ledit_poc_port_number.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.ledit_poc_port_number.setObjectName(_fromUtf8("ledit_poc_port_number"))
        self.verticalLayout.addWidget(self.ledit_poc_port_number)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.progressBar_path = QtGui.QProgressBar(self.tab_path)
        self.progressBar_path.setGeometry(QtCore.QRect(40, 320, 501, 31))
        self.progressBar_path.setVisible(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.progressBar_path.setFont(font)
        self.progressBar_path.setStyleSheet(_fromUtf8(""))
        self.progressBar_path.setProperty("value", 0)
        self.progressBar_path.setObjectName(_fromUtf8("progressBar_path"))
        self.tabWidget.addTab(self.tab_path, _fromUtf8(""))
        self.tab_gitlab = QtGui.QWidget()
        self.tab_gitlab.setEnabled(False)
        self.tab_gitlab.setObjectName(_fromUtf8("tab_gitlab"))
        self.layoutWidget_2 = QtGui.QWidget(self.tab_gitlab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 30, 641, 271))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_11 = QtGui.QLabel(self.layoutWidget_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_5.addWidget(self.label_11)
        self.label_15 = QtGui.QLabel(self.layoutWidget_2)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_5.addWidget(self.label_15)
        self.label_16 = QtGui.QLabel(self.layoutWidget_2)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_5.addWidget(self.label_16)
        self.label_17 = QtGui.QLabel(self.layoutWidget_2)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.verticalLayout_5.addWidget(self.label_17)
        self.label_18 = QtGui.QLabel(self.layoutWidget_2)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout_5.addWidget(self.label_18)
        self.label_19 = QtGui.QLabel(self.layoutWidget_2)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.verticalLayout_5.addWidget(self.label_19)
        self.label_20 = QtGui.QLabel(self.layoutWidget_2)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.verticalLayout_2.addWidget(self.label_20)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.ledit_gitlab_url = QtGui.QLineEdit(self.layoutWidget_2)
        self.ledit_gitlab_url.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.ledit_gitlab_url.setObjectName(_fromUtf8("ledit_gitlab_url"))
        self.verticalLayout_6.addWidget(self.ledit_gitlab_url)
        self.ledit_gitlab_user = QtGui.QLineEdit(self.layoutWidget_2)
        self.ledit_gitlab_user.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.ledit_gitlab_user.setObjectName(_fromUtf8("ledit_gitlab_user"))
        self.verticalLayout_6.addWidget(self.ledit_gitlab_user)
        self.ledit_gitlab_pass = QtGui.QLineEdit(self.layoutWidget_2)
        self.ledit_gitlab_pass.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.ledit_gitlab_pass.setObjectName(_fromUtf8("ledit_gitlab_pass"))
        self.ledit_gitlab_pass.setEchoMode(QtGui.QLineEdit.Password)
        self.verticalLayout_6.addWidget(self.ledit_gitlab_pass)
        self.ledit_confirm_branch = QtGui.QLineEdit(self.layoutWidget_2)
        self.ledit_confirm_branch.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.ledit_confirm_branch.setObjectName(_fromUtf8("ledit_confirm_branch"))
        self.verticalLayout_6.addWidget(self.ledit_confirm_branch)
        self.ledit_master_branch = QtGui.QLineEdit(self.layoutWidget_2)
        self.ledit_master_branch.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.ledit_master_branch.setObjectName(_fromUtf8("ledit_master_branch"))
        self.verticalLayout_6.addWidget(self.ledit_master_branch)
        self.ledit_project_name = QtGui.QLineEdit(self.layoutWidget_2)
        self.ledit_project_name.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.ledit_project_name.setObjectName(_fromUtf8("ledit_project_name"))
        self.verticalLayout_6.addWidget(self.ledit_project_name)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.btn_config_save_gitlab = QtGui.QPushButton(self.tab_gitlab)
        self.btn_config_save_gitlab.setGeometry(QtCore.QRect(550, 280, 101, 41))
        self.btn_config_save_gitlab.setStyleSheet(_fromUtf8("background-color: rgb(159, 173, 176);"))
        self.btn_config_save_gitlab.setObjectName(_fromUtf8("btn_config_save_gitlab"))
        self.progressBar_gitlab = QtGui.QProgressBar(self.tab_gitlab)
        self.progressBar_gitlab.setGeometry(QtCore.QRect(40, 320, 501, 31))
        self.progressBar_gitlab.setVisible(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.progressBar_gitlab.setFont(font)
        self.progressBar_gitlab.setStyleSheet(_fromUtf8(""))
        self.progressBar_gitlab.setProperty("value", 0)
        self.progressBar_gitlab.setObjectName(_fromUtf8("progressBar_gitlab"))
        self.tabWidget.addTab(self.tab_gitlab, _fromUtf8(""))
        self.btn_unlock = QtGui.QPushButton(self.centralwidget)
        self.btn_unlock.setGeometry(QtCore.QRect(630, 40, 101, 41))
        self.btn_unlock.setStyleSheet(_fromUtf8("background-color: rgb(159, 173, 176);"))
        self.btn_unlock.setObjectName(_fromUtf8("btn_unlock"))
        self.lbl_error_message = QtGui.QLabel(self.centralwidget)
        self.lbl_error_message.setGeometry(QtCore.QRect(10, 40, 611, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.lbl_error_message.setFont(font)
        self.lbl_error_message.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.lbl_error_message.setText(_fromUtf8(""))
        self.lbl_error_message.setObjectName(_fromUtf8("lbl_error_message"))
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 10, 231, 34))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_6 = QtGui.QLabel(self.layoutWidget1)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.cmb_switch_confirm = QtGui.QComboBox(self.layoutWidget)
        self.cmb_switch_confirm.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.cmb_switch_confirm.setObjectName(_fromUtf8("cmb_fw_file_name"))
        self.cmb_switch_confirm.setEnabled(False)
        self.horizontalLayout_2.addWidget(self.cmb_switch_confirm)
        FwSettingsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(FwSettingsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 22))
        self.menubar.setStyleSheet(_fromUtf8(""))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_edit = QtGui.QMenu(self.menubar)
        self.menu_edit.setStyleSheet(_fromUtf8(""))
        self.menu_edit.setObjectName(_fromUtf8("menu_edit"))
        self.menu_help = QtGui.QMenu(self.menubar)
        self.menu_help.setObjectName(_fromUtf8("menu_help"))
        FwSettingsWindow.setMenuBar(self.menubar)
        self.action_exit = QtGui.QAction(FwSettingsWindow)
        self.action_exit.setObjectName(_fromUtf8("action_exit"))
        self.menu_definitions = QtGui.QAction(FwSettingsWindow)
        self.menu_definitions.setObjectName(_fromUtf8("menu_definitions"))
        self.menu_about = QtGui.QAction(FwSettingsWindow)
        self.menu_about.setObjectName(_fromUtf8("menu_about"))
        self.menu_edit.addAction(self.action_exit)
        self.menu_help.addAction(self.menu_definitions)
        self.menu_help.addAction(self.menu_about)
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(FwSettingsWindow)
        self.tabWidget.setCurrentIndex(0)

        self.def_window = None
        self.about_window = None

        #QtCore.QObject.connect(FwSettingsWindow, QtCore.SIGNAL(_fromUtf8("destroyed()")), self.close_event)
        QtCore.QObject.connect(self.action_exit, QtCore.SIGNAL(_fromUtf8("triggered()")), FwSettingsWindow.close)
        #FwSettingsWindow.destroyed.connect(self.close_event)
        QtCore.QMetaObject.connectSlotsByName(FwSettingsWindow)

        abs_path = os.path.abspath(__file__)
        path_list = abs_path.split("/")
        del path_list[-1]
        path_name="/".join(path_list)
        full_path = path_name + "/"

        #stylesheets
        FwSettingsWindow.setStyleSheet(_fromUtf8("QMainWindow#FwSettingsWindow {border-image: url("+full_path+"img/ahtapot_logo.png);}"))

        self.git = False
        self.parent = False
        self.active_user = "None"
        self.current_user = "None"

        confirm_list = [u"Açık",u"Kapalı"]
        self.cmb_switch_confirm.addItems(confirm_list)

        with open(full_path + "current_user.dmr", "r") as current_user:
            self.active_user = current_user.readline()
        self.logger = Syslogger("FWBUILDER-AHTAPOT",'%(name)s %(levelname)s %(message)s',"/dev/log",self.current_user)
        self.filelogger = Filelogger("FWBUILDER-AHTAPOT",'%(asctime)s %(name)s %(levelname)s %(message)s',"/var/log/ahtapot/gdys-gui.log","a",self.current_user)

        QtCore.QObject.connect(self.btn_unlock, QtCore.SIGNAL(_fromUtf8("clicked()")), self.unlock_settings)
        QtCore.QObject.connect(self.cmb_switch_confirm, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(const QString&)")), self.change_confirmation)
        QtCore.QObject.connect(self.btn_config_save, QtCore.SIGNAL(_fromUtf8("clicked()")), self.save_config_path)
        QtCore.QObject.connect(self.btn_config_save_gitlab, QtCore.SIGNAL(_fromUtf8("clicked()")), self.save_config_gitlab)

        QtCore.QObject.connect(self.menu_definitions, QtCore.SIGNAL(_fromUtf8("triggered()")), self.show_def_window)
        QtCore.QObject.connect(self.menu_about, QtCore.SIGNAL(_fromUtf8("triggered()")), self.show_about_window)


        self.set_config_text()
        self.get_confirmation_status()
        self.get_file_list()



    def retranslateUi(self, FwSettingsWindow):
        FwSettingsWindow.setWindowTitle(_translate("FwSettingsWindow", " Ahtapot - GDYS - Yapılandırma", None))
        self.btn_config_save.setText(_translate("FwSettingsWindow", "Kaydet", None))
        self.label_13.setText(_translate("FwSettingsWindow", "Yapılandırma Dosya Adı", None))
        self.label_2.setText(_translate("FwSettingsWindow", "Test Betikleri Dizini", None))
        self.label_12.setText(_translate("FwSettingsWindow", "Hata Bildirim Dizini", None))
        self.label_3.setText(_translate("FwSettingsWindow", "Test Makinesi IP Adresi", None))
        self.label_4.setText(_translate("FwSettingsWindow", "Test Makinesi Kullanıcı Adı", None))
        self.label_5.setText(_translate("FwSettingsWindow", "Test Makinesi Betik Dizini", None))
        self.ledit_fw_copy_path.setToolTip(_translate("FwSettingsWindow", "<html><head/><body><p>Test ortamında çalıştırılacak kural betiklerinin bulunduğu dizin adı</p></body></html>", None))
        self.ledit_gitlab_pass.setToolTip(_translate("FwSettingsWindow", "<html><head/><body><p>Onay mekanizmasında kullanılacak GitLab’a bağlantıyı sağlayan kullanıcının parolası</p></body></html>", None))
        self.ledit_project_name.setToolTip(_translate("FwSettingsWindow", "<html><head/><body><p>Projenin bulunduğu deponun adı</p></body></html>", None))
        self.ledit_master_branch.setToolTip(_translate("FwSettingsWindow", "<html><head/><body><p>Onaylanmış kuralların bulunduğu dalın adı</p></body></html>", None))
        self.ledit_confirm_branch.setToolTip(_translate("FwSettingsWindow", "<html><head/><body><p>Onaya gönderilen kuralların bulunduğu dalın adı</p></body></html>", None))
        self.ledit_gitlab_user.setToolTip(_translate("FwSettingsWindow", "<html><head/><body><p>Onay mekanizmasında kullanılacak GitLab’a bağlantıyı sağlayan kullanıcının adı</p></body></html>", None))
        self.ledit_gitlab_url.setToolTip(_translate("FwSettingsWindow", "<html><head/><body><p>Onay mekanizması için kullanılacak GitLab’ın bağlantı adresi</p></body></html>", None))
        self.ledit_poc_user.setToolTip(_translate("FwSettingsWindow", "<html><head/><body><p>Ip tables kurallarının söz dizimi bakımından test edileceği makinanın kullanıcı adı</p></body></html>", None))
        self.ledit_poc_ip.setToolTip(_translate("FwSettingsWindow", "<html><head/><body><p>Ip tables kurallarının söz dizimi bakımından test edileceği makinanın IP adresi</p></body></html>", None))
        self.ledit_poc_port_number.setToolTip(_translate("FwSettingsWindow", "<html><head/><body><p>Ip tables kurallarının söz dizimi bakımından test edileceği makinanın Port Numarası</p></body></html>", None))
        self.ledit_poc_copy_path.setToolTip(_translate("FwSettingsWindow", "<html><head/><body><p>FirewallBuilder tarafından üretilen ve söz dizimi bakımından test edilecek betikerin kopyalandığı dizin adı</p></body></html>", None))
        self.ledit_std_out_err.setToolTip(_translate("FwSettingsWindow", "<html><head/><body><p>Test sırasında söz dizimi hatası bulunması durumunda hata çıktılarının yazıldığı dizin adı</p></body></html>", None))
        self.cmb_fw_file_name.setToolTip(_translate("FwSettingsWindow", "<html><head/><body><p>FirewallBuilder tarafından açılacak olan yapılandırma dosyasının adı</p></body></html>", None))
        self.cmb_switch_confirm.setToolTip(_translate("FwSettingsWindow", "<html><head/><body><p>FirewallBuilder’dan yazılacak kuralların onay mekanizmasına tabii olup olmayacağını belirten ayar</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_path), _translate("FwSettingsWindow", "Dizin Yapılandırma", None))
        self.label_11.setText(_translate("FwSettingsWindow", "GitLab Bağlantı Adresi", None))
        self.label_15.setText(_translate("FwSettingsWindow", "GitLab Kullanıcı Adı", None))
        self.label_16.setText(_translate("FwSettingsWindow", "GitLab Kullanıcı Parolası", None))
        self.label_17.setText(_translate("FwSettingsWindow", "GitLab Onay Dalı", None))
        self.label_18.setText(_translate("FwSettingsWindow", "GitLab Ana Dal", None))
        self.label_19.setText(_translate("FwSettingsWindow", "GitLab Proje Adı", None))
        self.label_20.setText(_translate("FwSettingsWindow", "Test Makinesi Port Numarası", None))
        self.btn_config_save_gitlab.setText(_translate("FwSettingsWindow", "Kaydet", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_gitlab), _translate("FwSettingsWindow", "Gitlab Yapılandırma", None))
        self.btn_unlock.setText(_translate("FwSettingsWindow", "Kilidi Aç", None))
        self.label_6.setText(_translate("FwSettingsWindow", "Onay Mekanizması :", None))
        self.menu_edit.setTitle(_translate("FwSettingsWindow", "Düzenle", None))
        self.menu_help.setTitle(_translate("FwSettingsWindow", "Yardım", None))
        self.action_exit.setText(_translate("FwSettingsWindow", "Çıkış", None))
        self.action_exit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.menu_definitions.setText(_translate("FwSettingsWindow", "Açıklamalar", None))
        self.menu_definitions.setShortcut(_translate("MainWindow", "Ctrl+D", None))
        self.menu_about.setText(_translate("FwSettingsWindow", "Hakkında", None))
        self.menu_about.setShortcut(_translate("MainWindow", "Ctrl+A", None))


    def set_windows(self,old,new):
        self.old_window = old
        self.new_window = new

    def change_windows(self):
        self.new_window.show()

    def show_def_window(self):
        self.def_window.show()

    def show_about_window(self):
        self.about_window.show()

    def close_event(self):
        self.old_window.show()
        self.new_window.hide()

    def set_error_message(self,message):
        self.lbl_error_message.setText(message)

    def set_config_text(self):

        self.ledit_fw_copy_path.setText(CP.get_configs()["fw_copy_path"])
        self.ledit_poc_user.setText(CP.get_configs()["poc_user"])
        self.ledit_poc_ip.setText(CP.get_configs()["poc_ip"])
        self.ledit_poc_port_number.setText(CP.get_configs()["port_number"])
        self.ledit_poc_copy_path.setText(CP.get_configs()["poc_copy_location"])
        self.ledit_std_out_err.setText(CP.get_configs()["std_out_err"])
        self.ledit_gitlab_url.setText(CP.get_configs()["gitlab_url"])
        self.ledit_gitlab_user.setText(CP.get_configs()["gitlab_user"])
        self.ledit_gitlab_pass.setText(CP.get_configs()["gitlab_pass"])
        self.ledit_confirm_branch.setText(CP.get_configs()["gitlab_confirm_branch"])
        self.ledit_master_branch.setText(CP.get_configs()["gitlab_master_branch"])
        self.ledit_project_name.setText(CP.get_configs()["gitlab_project_name"])

    def save_config_path(self):
        self.logger = Syslogger("FWBUILDER-AHTAPOT",'%(name)s %(levelname)s %(message)s',"/dev/log", self.current_user)
        self.filelogger = Filelogger("FWBUILDER-AHTAPOT",'%(asctime)s %(name)s %(levelname)s %(message)s',"/var/log/ahtapot/gdys-gui.log","a",self.current_user)
        config_paths = {}
        config_paths["fwb_file_name"] = str(self.cmb_fw_file_name.currentText())
        config_paths["fw_copy_path"] = self.ledit_fw_copy_path.text()
        config_paths["poc_user"] = self.ledit_poc_user.text()
        config_paths["poc_ip"] = self.ledit_poc_ip.text()
        config_paths["port_number"] = self.ledit_poc_port_number.text()
        config_paths["poc_copy_location"] = self.ledit_poc_copy_path.text()
        config_paths["std_out_err"] = self.ledit_std_out_err.text()

        self.progressBar_path.setVisible(True)
        self.centralwidget.setEnabled(False)
        self.set_progressbar(self.progressBar_path)
        CP.set_path_config(config_paths)
        self.logger.send_log("warning"," path configs changed")
        self.filelogger.send_log("warning"," path configs changed")
        result = self.check_and_refresh()
        self.centralwidget.setEnabled(True)
        self.progressBar_path.setValue(0)
        self.progressBar_path.setVisible(False)
        if result == True:
            self.lbl_error_message.setText(u"<p>Ayarlarınız başarılı bir şekilde kaydedildi.</p>")

    def save_config_gitlab(self):
        self.logger = Syslogger("FWBUILDER-AHTAPOT",'%(name)s %(levelname)s %(message)s',"/dev/log", self.current_user)
        self.filelogger = Filelogger("FWBUILDER-AHTAPOT",'%(asctime)s %(name)s %(levelname)s %(message)s',"/var/log/ahtapot/gdys-gui.log","a",self.current_user)
        config_gitlab = {}
        config_gitlab["url"] = self.ledit_gitlab_url.text()
        config_gitlab["user"] = self.ledit_gitlab_user.text()
        config_gitlab["pass"] = self.ledit_gitlab_pass.text()
        config_gitlab["confirm_branch"] = self.ledit_confirm_branch.text()
        config_gitlab["master_branch"] = self.ledit_master_branch.text()
        config_gitlab["project_name"] = self.ledit_project_name.text()

        self.progressBar_gitlab.setVisible(True)
        self.centralwidget.setEnabled(False)
        self.set_progressbar(self.progressBar_gitlab)
        CP.set_gitlab_config(config_gitlab)
        self.logger.send_log("warning"," gitlab configs changed")
        self.filelogger.send_log("warning"," gitlab configs changed")
        result = self.check_and_refresh()
        self.centralwidget.setEnabled(True)
        self.progressBar_gitlab.setValue(0)
        self.progressBar_gitlab.setVisible(False)
        if result == True:
            self.lbl_error_message.setText(u"<p>Ayarlarınız başarılı bir şekilde kaydedildi.</p>")

    def set_progressbar(self,progressbar):
        progressbar.setValue(30)
        sleep(1)
        progressbar.setValue(60)
        sleep(1)
        progressbar.setValue(100)

    def check_and_refresh(self):
        check_path = start_fw.check_config_paths(CP.get_path_configs())
        check_gitlab_conn = GC.check_gitlab_connection(CP.get_gitlab_configs())
        self.lbl_error_message.setText("")
        if check_gitlab_conn[0] == True:
            self.git = check_gitlab_conn[1]
            check_gitlab_sett = GC.check_gitlab_settings(self.git,CP.get_gitlab_configs())

        if check_path == True and check_gitlab_conn[0] == True and check_gitlab_sett == True:
            self.lbl_error_message.setText("")
            self.parent.btn_merge_control.setEnabled(True)
            self.parent.btn_deny_control.setEnabled(True)
            self.parent.btn_start_fwbuilder.setEnabled(True)
            self.parent.btn_watch_merge.setEnabled(True)
            self.parent.check_and_refresh()
            return True
        else:
            self.parent.btn_merge_control.setEnabled(False)
            self.parent.btn_deny_control.setEnabled(False)
            self.parent.btn_start_fwbuilder.setEnabled(False)
            self.parent.btn_watch_merge.setEnabled(False)
            self.parent.lbl_merge_control.setText(u"")
            self.lbl_error_message.setText("")
            if check_path != True:
                self.set_error_message(check_path)
            elif check_gitlab_conn[0] != True:
                self.set_error_message(check_gitlab_conn[0])
            else:
                self.set_error_message(check_gitlab_sett)
            return False


    def get_confirmation_status(self):
        status = str(CP.get_gitlab_configs()["gitlab_confirmation"])
        if status == "on":
            self.cmb_switch_confirm.setCurrentIndex(0)
        else:
            self.cmb_switch_confirm.setCurrentIndex(1)

    def change_confirmation(self):
        status = self.cmb_switch_confirm.currentIndex()
        abs_path = os.path.abspath(__file__)
        path_list = abs_path.split("/")
        del path_list[-1]
        path_name="/".join(path_list)
        full_path = path_name + "/"
        with_confirmation = full_path + "installers/" + "with_confirm.py"
        without_confirmation = full_path + "installers/" + "without_confirm.py"
        installer = full_path + "installer.py"

        cmd_cp_with = "cp " + with_confirmation + " " + installer
        cmd_cp_without = "cp " + without_confirmation + " " + installer

        if status == 0:
            config = {}
            config["confirmation"] = "on"
            CP.set_gitlab_config(config)
            subprocess.call([cmd_cp_with],shell=True)
        else:
            config = {}
            config["confirmation"] = "off"
            CP.set_gitlab_config(config)
            subprocess.call([cmd_cp_without],shell=True)

    def unlock_settings(self):
        if self.cmb_switch_confirm.isEnabled() == True:
            self.tab_gitlab.setEnabled(False)
            self.tab_path.setEnabled(False)
            self.cmb_switch_confirm.setEnabled(False)
            self.btn_unlock.setText(u"Kilidi Aç")
        else:
            text, ok = QtGui.QInputDialog.getText(self,u"Giriş Yapınız",u"Root parolasını giriniz : ",QtGui.QLineEdit.Password)
            if ok:
                root_pass = str(text)
                res = self.pam_login('root',root_pass)
                if res == True:
                    self.tab_gitlab.setEnabled(True)
                    self.tab_path.setEnabled(True)
                    self.cmb_switch_confirm.setEnabled(True)
                    self.btn_unlock.setText(u"Kilitle")
                else:
                    QtGui.QMessageBox.warning(self,'Hata',u'Hatalı Giriş Bilgileri',QtGui.QMessageBox.Ok)

    def get_file_list(self):
        self.logger = Syslogger("FWBUILDER-AHTAPOT",'%(name)s %(levelname)s %(message)s',"/dev/log", self.current_user)
        self.filelogger = Filelogger("FWBUILDER-AHTAPOT",'%(asctime)s %(name)s %(levelname)s %(message)s',"/var/log/ahtapot/gdys-gui.log","a",self.current_user)
        fw_path = CP.get_path_configs()["fw_path"]
        files = []
        fwb_list = []
        for (dirpath,dirnames,file_names) in os.walk(fw_path):
            files.extend(file_names)
            break
        for f in files:
            f_name, f_extension = os.path.splitext(f)
            if f_extension == ".fwb":
                fwb_list.append(str(f))

        if len(fwb_list) != 0:
            self.cmb_fw_file_name.addItems(fwb_list)

        fwb_file_name = CP.get_path_configs()["fwb_file_name"]
        index = self.cmb_fw_file_name.findText(str(fwb_file_name))
        if index != -1:
            self.cmb_fw_file_name.setCurrentIndex(index)

    def pam_login(self,username, password):
        try:
            child = pexpect.spawn('/bin/su - %s'%(username))
            child.expect('Password:')
            child.sendline(password)
            result=child.expect(['su: Authentication failure',username])
            child.close()
        except Exception as exc_err:
            child.close()
            print ("Error authenticating. Reason: "%(exc_err))
            self.logger.send_log("error","error found while attempting to login to unlock\n"+str(exc_err))
            self.filelogger.send_log("error","error found while attempting to login to unlock\n"+str(exc_err))
            return False
        if result == 0:
            print ("Authentication failed for user %s."%(username))
            self.logger.send_log("error","failed login to unlock")
            self.filelogger.send_log("error","failed login to unlock")
            return False
        else:
            return True

