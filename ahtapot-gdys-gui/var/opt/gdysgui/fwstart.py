# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fwstart.ui'
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
import fwsettingsdef

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

class Ui_FwStartWindow(QtGui.QWidget):
    def setupUi(self, FwStartWindow):
        FwStartWindow.setObjectName(_fromUtf8("FwStartWindow"))
        FwStartWindow.move(200,100)
        FwStartWindow.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FwStartWindow.sizePolicy().hasHeightForWidth())
        FwStartWindow.setSizePolicy(sizePolicy)
        FwStartWindow.setMinimumSize(QtCore.QSize(800, 600))
        FwStartWindow.setMaximumSize(QtCore.QSize(800, 600))
        FwStartWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 236, 207);"))
        self.centralwidget = QtGui.QWidget(FwStartWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_deny_control = QtGui.QPushButton(self.centralwidget)
        self.btn_deny_control.setGeometry(QtCore.QRect(340, 430, 181, 50))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(490, 120, 301, 181))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_deny_control.sizePolicy().hasHeightForWidth())
        self.btn_deny_control.setSizePolicy(sizePolicy)
        self.btn_deny_control.setMinimumSize(QtCore.QSize(160, 50))
        self.btn_deny_control.setAcceptDrops(False)
        self.btn_deny_control.setStyleSheet(_fromUtf8("background-color: rgb(159, 173, 176);"))
        self.btn_deny_control.setObjectName(_fromUtf8("btn_deny_control"))
        self.btn_start_fwbuilder = QtGui.QPushButton(self.centralwidget)
        self.btn_start_fwbuilder.setGeometry(QtCore.QRect(150, 430, 181, 50))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start_fwbuilder.sizePolicy().hasHeightForWidth())
        self.btn_start_fwbuilder.setSizePolicy(sizePolicy)
        self.btn_start_fwbuilder.setMinimumSize(QtCore.QSize(160, 50))
        self.btn_start_fwbuilder.setStyleSheet(_fromUtf8("background-color: rgb(159, 173, 176);"))
        self.btn_start_fwbuilder.setObjectName(_fromUtf8("btn_start_fwbuilder"))
        self.lbl_last_merge = QtGui.QLabel(self.centralwidget)
        self.lbl_last_merge.setGeometry(QtCore.QRect(240, 530, 505, 41))
        self.lbl_last_merge.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lbl_last_merge.setFont(font)
        self.lbl_last_merge.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.lbl_last_merge.setText(_fromUtf8(""))
        self.lbl_last_merge.setObjectName(_fromUtf8("lbl_last_merge"))
        self.lbl_error_start = QtGui.QLabel(self.centralwidget)
        self.lbl_error_start.setGeometry(QtCore.QRect(20, 260, 375, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lbl_error_start.setFont(font)
        self.lbl_error_start.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.lbl_error_start.setText(_fromUtf8(""))
        self.lbl_error_start.setObjectName(_fromUtf8("lbl_error_start"))

        self.btn_kill_fw = QtGui.QPushButton(self.centralwidget)
        self.btn_kill_fw.setGeometry(QtCore.QRect(10, 300, 51, 50))
        self.btn_kill_fw.setMinimumSize(QtCore.QSize(120, 50))
        self.btn_kill_fw.setAcceptDrops(False)
        self.btn_kill_fw.setStyleSheet(_fromUtf8("background-color: rgb(159, 173, 176);"))
        self.btn_kill_fw.setObjectName(_fromUtf8("btn_kill_fw"))
        self.btn_kill_fw.setEnabled(False)

        self.btn_watch_merge = QtGui.QPushButton(self.centralwidget)
        self.btn_watch_merge.setGeometry(QtCore.QRect(530, 430, 181, 50))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_watch_merge.sizePolicy().hasHeightForWidth())
        self.btn_watch_merge.setSizePolicy(sizePolicy)
        self.btn_watch_merge.setMinimumSize(QtCore.QSize(160, 50))
        self.btn_watch_merge.setAcceptDrops(False)
        self.btn_watch_merge.setStyleSheet(_fromUtf8("background-color: rgb(159, 173, 176);"))
        self.btn_watch_merge.setObjectName(_fromUtf8("btn_watch_merge"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(120, 10, 571, 31))
        self.progressBar.setVisible(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet(_fromUtf8(""))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.btn_merge_control = QtGui.QPushButton(self.centralwidget)
        self.btn_merge_control.setGeometry(QtCore.QRect(580, 60, 181, 50))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_merge_control.sizePolicy().hasHeightForWidth())
        self.btn_merge_control.setSizePolicy(sizePolicy)
        self.btn_merge_control.setMinimumSize(QtCore.QSize(160, 50))
        self.btn_merge_control.setStyleSheet(_fromUtf8("background-color: rgb(159, 173, 176);"))
        self.btn_merge_control.setObjectName(_fromUtf8("btn_merge_control"))
        self.lbl_merge_control = QtGui.QLabel(self.frame)
        self.lbl_merge_control.setGeometry(QtCore.QRect(1, 1, 300, 180))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_merge_control.sizePolicy().hasHeightForWidth())
        self.lbl_merge_control.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_merge_control.setFont(font)
        self.lbl_merge_control.setAutoFillBackground(False)
        self.lbl_merge_control.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.lbl_merge_control.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        self.lbl_merge_control.setObjectName(_fromUtf8("lbl_merge_control"))
        FwStartWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(FwStartWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setStyleSheet(_fromUtf8(""))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_edit = QtGui.QMenu(self.menubar)
        self.menu_edit.setObjectName(_fromUtf8("menu_edit"))
        self.menu_help = QtGui.QMenu(self.menubar)
        self.menu_help.setObjectName(_fromUtf8("menu_help"))
        FwStartWindow.setMenuBar(self.menubar)
        self.action_refresh = QtGui.QAction(FwStartWindow)
        self.action_refresh.setObjectName(_fromUtf8("action_refresh"))
        self.action_settings = QtGui.QAction(FwStartWindow)
        self.action_settings.setObjectName(_fromUtf8("action_settings"))
        self.action_definitions = QtGui.QAction(FwStartWindow)
        self.action_definitions.setObjectName(_fromUtf8("action_definitions"))
        self.action_about = QtGui.QAction(FwStartWindow)
        self.action_about.setObjectName(_fromUtf8("action_about"))
        self.action_exit = QtGui.QAction(FwStartWindow)
        self.action_exit.setObjectName(_fromUtf8("action_exit"))
        self.menu_edit.addAction(self.action_refresh)
        self.menu_edit.addAction(self.action_settings)
        self.menu_edit.addAction(self.action_exit)
        self.menu_help.addAction(self.action_definitions)
        self.menu_help.addAction(self.action_about)
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.auto_refresh)

        self.def_window = None
        self.about_window = None


        self.retranslateUi(FwStartWindow)
        self.git = False
        self.git_status = False
        self.child = False
        self.old_config = {}
        self.active_user = "None"
        self.current_user = "None"

        abs_path = os.path.abspath(__file__)
        path_list = abs_path.split("/")
        del path_list[-1]
        path_name="/".join(path_list)
        full_path = path_name + "/"
        with open(full_path+"current_user.dmr","r") as current_user:
            self.active_user = current_user.readline()
        self.full_path = full_path
        self.logger = Syslogger("FWBUILDER-AHTAPOT",'%(name)s %(levelname)s %(message)s',"/dev/log", self.current_user)
        self.filelogger = Filelogger("FWBUILDER-AHTAPOT",'%(asctime)s %(name)s %(levelname)s %(message)s',"/var/log/ahtapot/gdys-gui.log","a",self.current_user)

        #stylesheets
        FwStartWindow.setStyleSheet(_fromUtf8("QMainWindow#FwStartWindow {border-image: url("+full_path+"img/ahtapot_logo.png);}"))

        self.set_confirmation_status()


        QtCore.QObject.connect(self.action_settings, QtCore.SIGNAL(_fromUtf8("triggered()")), self.change_windows)
        QtCore.QObject.connect(self.action_exit, QtCore.SIGNAL(_fromUtf8("triggered()")), exit)
        QtCore.QObject.connect(self.action_refresh, QtCore.SIGNAL(_fromUtf8("triggered()")), self.refresh_method)
        QtCore.QObject.connect(self.action_definitions, QtCore.SIGNAL(_fromUtf8("triggered()")), self.show_def_window)
        QtCore.QObject.connect(self.action_about, QtCore.SIGNAL(_fromUtf8("triggered()")), self.show_about_window)


        QtCore.QObject.connect(self.btn_start_fwbuilder, QtCore.SIGNAL(_fromUtf8("clicked()")), self.start_fwbuilder)
        QtCore.QObject.connect(self.btn_merge_control, QtCore.SIGNAL(_fromUtf8("clicked()")), self.check_git_merge)
        QtCore.QObject.connect(self.btn_deny_control, QtCore.SIGNAL(_fromUtf8("clicked()")), self.load_new_rules)
        QtCore.QObject.connect(self.btn_watch_merge, QtCore.SIGNAL(_fromUtf8("clicked()")), self.watch_new_rules)
        QtCore.QObject.connect(self.btn_kill_fw, QtCore.SIGNAL(_fromUtf8("clicked()")), self.kill_all)

        QtCore.QMetaObject.connectSlotsByName(FwStartWindow)



    def retranslateUi(self, FwStartWindow):
        FwStartWindow.setWindowTitle(_translate("FwStartWindow", " Ahtapot - GDYS", None))
        self.btn_deny_control.setText(_translate("FwStartWindow", "Onaylanmış Ayarlar\n"
"    ile Çalıştır", None))
        self.btn_start_fwbuilder.setText(_translate("FwStartWindow", "Yerel Ayarlar \n"
"  ile Çalıştır", None))
        self.btn_watch_merge.setText(_translate("FwStartWindow", "Onaylanmış Ayarları\n"
"   Göster", None))
        self.btn_merge_control.setText(_translate("FwStartWindow", "Onay Kontrol", None))
        self.btn_kill_fw.setText(_translate("FwStartWindow", "Sonlandır", None))
        self.lbl_merge_control.setText(_translate("FwStartWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.menu_edit.setTitle(_translate("FwStartWindow", "Düzenle", None))
        self.menu_help.setTitle(_translate("FwStartWindow", "Yardım", None))
        self.action_refresh.setText(_translate("FwStartWindow", "Yenile", None))
        self.action_refresh.setShortcut(_translate("MainWindow", "Ctrl+R", None))
        self.action_settings.setText(_translate("FwStartWindow", "Yapılandırma Ayarları", None))
        self.action_settings.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.action_definitions.setText(_translate("FwStartWindow", "Açıklamalar", None))
        self.action_definitions.setShortcut(_translate("MainWindow", "Ctrl+D", None))
        self.action_about.setText(_translate("FwStartWindow", "Hakkında", None))
        self.action_about.setShortcut(_translate("MainWindow", "Ctrl+A", None))
        self.action_exit.setText(_translate("FwStartWindow", "Çıkış", None))
        self.action_exit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.timer.start(15000)

    def set_windows(self,old,new):
        self.old_window = old
        self.new_window = new

    def change_windows(self):
        self.child.setupUi(self.new_window)
        self.child.parent = self
        self.child.about_window = self.about_window
        FwSettingsDefWindow = QtGui.QMainWindow()
        ui_settings_def = fwsettingsdef.Ui_Form()
        ui_settings_def.setupUi(FwSettingsDefWindow)
        self.child.def_window = FwSettingsDefWindow
        self.child.current_user = self.current_user
        self.new_window.show()

    def show_def_window(self):
        self.def_window.show()

    def show_about_window(self):
        self.about_window.show()

    def set_error_message(self,message):
        self.lbl_error_start.setText(message)

    def check_and_refresh(self):
        check_path = start_fw.check_config_paths(CP.get_path_configs())
        check_gitlab_conn = GC.check_gitlab_connection(CP.get_gitlab_configs())
        self.old_config = CP.get_configs()
        if check_gitlab_conn[0] == True:
            self.git = check_gitlab_conn[1]
            GC.set_project_id(self.git,CP.get_gitlab_connection()["gitlab_project_name"])
            check_gitlab_sett = GC.check_gitlab_settings(self.git,CP.get_gitlab_configs())

        if check_path == True and check_gitlab_conn[0] == True and check_gitlab_sett == True:
            self.lbl_error_start.setText("")
            self.btn_merge_control.setEnabled(True)
            self.btn_deny_control.setEnabled(True)
            self.btn_start_fwbuilder.setEnabled(True)
            self.btn_watch_merge.setEnabled(True)
            self.check_git_merge(self.git)
            self.warn_if_fw_runs()
            return True
        else:
            self.btn_merge_control.setEnabled(False)
            self.btn_deny_control.setEnabled(False)
            self.btn_start_fwbuilder.setEnabled(False)
            self.btn_watch_merge.setEnabled(False)
            self.lbl_merge_control.setText("")
            self.lbl_merge_control.setText("")
            if check_path != True:
                self.set_error_message(check_path)
            elif check_gitlab_conn[0] != True:
                self.set_error_message(check_gitlab_conn[0])
            else:
                self.set_error_message(check_gitlab_sett)
            return False

    def check_git_merge(self,git):
        self.lbl_error_start.setText("<p></p>")
        self.progressBar.setVisible(True)
        self.centralwidget.setEnabled(False)
        self.set_progressbar()

        #git = GC.gitlab_connect(CP.get_configs()["gitlab_url"],CP.get_configs()["gitlab_user"],CP.get_configs()["gitlab_pass"]) #<<<<
        git_status = GC.check_mergerequest(git,CP.get_configs()["gitlab_project_id"]) #<<<<<
        self.git_status = git_status
        self.set_last_commit(GC.get_master_commit_id(git,CP.get_configs()["gitlab_project_id"],CP.get_configs()["gitlab_master_branch"]))
        if git_status == False:
            self.lbl_merge_control.setText(u"<p>Sistemde onay bekleyen kurallar bulunuyor.<br/>Son durumunu kontrol etmek için lütfen <br/>\"Onay Kontrol\" butonuna basınız.<br/><b>Not:</b> Onayda bekleyen istek olduğu sürece <br/>FWBuilder sadece okunabilir modda çalışacaktır</p>")
            self.btn_deny_control.setEnabled(False)
            self.btn_watch_merge.setEnabled(True)
        else:
            if GC.get_mergerequest_status(git,CP.get_configs()["gitlab_project_id"]) == "closed" and GC.check_merge_confirm() == True:
                self.lbl_merge_control.setText(u"<p><b>Son kural değişiklikleri reddedilmiş :</b> <br/>"+git.getmergerequestcomments(CP.get_configs()["gitlab_project_id"],git.getmergerequests(CP.get_configs()["gitlab_project_id"])[0]["id"])[-1]["note"]+"</p>")
            elif GC.get_mergerequest_status(git,CP.get_configs()["gitlab_project_id"]) == "merged":
                self.check_merge_file()
            self.btn_merge_control.setEnabled(False)
            self.btn_start_fwbuilder.setEnabled(True)
            self.btn_deny_control.setEnabled(True)
            self.btn_watch_merge.setEnabled(True)
        self.centralwidget.setEnabled(True)
        self.progressBar.setValue(0)
        self.progressBar.setVisible(False)

    def start_fwbuilder(self):
        self.logger = Syslogger("FWBUILDER-AHTAPOT",'%(name)s %(levelname)s %(message)s',"/dev/log", self.current_user)
        self.filelogger = Filelogger("FWBUILDER-AHTAPOT",'%(asctime)s %(name)s %(levelname)s %(message)s',"/var/log/ahtapot/gdys-gui.log","a",self.current_user)
        self.lbl_error_start.setText("<p></p>")
        if start_fw.check_if_runs() == False:
            with open(self.full_path + "current_user.dmr", "w") as current_user:
                current_user.write(self.current_user)
            fw_path = CP.get_configs()["fw_path"]
            start_fw.start_fwbuilder(self.git)
            self.logger.send_log("info"," Firewall Builder Started with Local settings")
            self.filelogger.send_log("info"," Firewall Builder Started with Local settings")
        else:
            self.warn_if_fw_runs()
            subprocess.call(["xdotool search --name \"Firewall Builder\" windowactivate windowsize 90\% 90\%"],shell=True)

    def refresh_method(self):
        self.progressBar.setVisible(True)
        self.centralwidget.setEnabled(False)
        self.set_progressbar()
        self.lbl_error_start.setText(u"<p></p>")
        if self.git != False:
            GC.set_project_id(self.git,CP.get_gitlab_connection()["gitlab_project_name"])
        self.check_and_refresh()
        self.warn_if_fw_runs()
        self.centralwidget.setEnabled(True)
        self.progressBar.setValue(0)
        self.progressBar.setVisible(False)

    def check_merge_file(self):
        if GC.check_merge_confirm() == True:
            self.lbl_merge_control.setText(u"<p>Onaylanmış yapılandırma mevcut, <br/>yüklemeniz tavsiye edilir.<br/> Aksi halde varolan ayarlarla başlatılıcaktır.</p>")
        else:
            self.lbl_merge_control.setText(u"<p></p>")

    def pull_repo(self):
        fw_path = CP.get_configs()["fw_path"]
        master_branch = CP.get_configs()["gitlab_master_branch"]
        confirm_branch = CP.get_configs()["gitlab_confirm_branch"]
        fwb_file_name = CP.get_configs()["fwb_file_name"]
        cmd_git_undo = "cd "+fw_path + "&& git checkout -- ."
        cmd_git_branch = "cd "+fw_path + "&& git checkout "+master_branch
        cmd_git_pull = "cd "+fw_path + "&& git pull --rebase origin "+master_branch
        subprocess.call([cmd_git_undo],shell=True)
        subprocess.call([cmd_git_branch],shell=True)
        subprocess.call([cmd_git_pull],shell=True)
        start_fw.kill_fw()
        fw_path = CP.get_configs()["fw_path"]
        cmd_git_branch = "cd "+fw_path + "&& git checkout "+confirm_branch
        cmd_git_check_file = "cd "+fw_path + " && git checkout "+master_branch+" -- " + fwb_file_name
        subprocess.call([cmd_git_branch],shell=True)
        subprocess.call([cmd_git_check_file],shell=True)
        start_fw.start_fwbuilder(self.git)

    def load_new_rules(self):
        self.logger = Syslogger("FWBUILDER-AHTAPOT",'%(name)s %(levelname)s %(message)s',"/dev/log", self.current_user)
        self.filelogger = Filelogger("FWBUILDER-AHTAPOT",'%(asctime)s %(name)s %(levelname)s %(message)s',"/var/log/ahtapot/gdys-gui.log","a",self.current_user)
        self.lbl_error_start.setText("<p></p>")
        if GC.check_mergerequest(self.git,CP.get_configs()["gitlab_project_id"]) == False:
            self.refresh_method()
        elif start_fw.check_if_runs() is True:
            self.warn_if_fw_runs()
        else:
            self.progressBar.setVisible(True)
            self.centralwidget.setEnabled(False)
            self.set_progressbar()
            abs_path = os.path.abspath(__file__)
            path_list = abs_path.split("/")
            del path_list[-1]
            path_name = "/".join(path_list)
            full_path = path_name + "/"
            if os.path.exists(full_path + "onay.dmr"):
                os.remove(full_path + "onay.dmr")
            self.pull_repo()
            self.logger.send_log("warning", " Rule Settings pulled from Master and Firewall Builder Started")
            self.filelogger.send_log("warning", " Rule Settings pulled from Master and Firewall Builder Started")
            self.lbl_merge_control.setText(u"<p></p>")
            self.centralwidget.setEnabled(True)
            self.progressBar.setValue(0)
            self.progressBar.setVisible(False)

    def set_last_commit(self,commit_date):
        if commit_date!=False:
            self.lbl_last_merge.setText(u"<b>Son Onaylanmış Commit ID :</b> " + commit_date)

    def set_progressbar(self):
        self.progressBar.setValue(30)
        sleep(1)
        self.progressBar.setValue(60)
        sleep(1)
        self.progressBar.setValue(100)

    def watch_new_rules(self):
        start_fw.start_fwbuilder_temp()

    def warn_if_fw_runs(self):
        if start_fw.check_if_runs() == True:
            with open(self.full_path + "current_user.dmr", "r") as active_user:
                self.active_user = active_user.readline()
            self.lbl_error_start.setText(u"<b>UYARI:</b> Şuan kullanılan başka bir Firewall Builder mevcut.<br/><b>Kullanıcı : </b>" + self.active_user)
            self.btn_kill_fw.setEnabled(True)
            self.btn_deny_control.setEnabled(False)
        else:
            if self.git_status != False:
                self.btn_deny_control.setEnabled(True)
            self.btn_kill_fw.setEnabled(False)

    def set_confirmation_status(self):
        status = str(CP.get_gitlab_configs()["gitlab_confirmation"])
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
        if status == "on":
            subprocess.call([cmd_cp_with],shell=True)
        else:
            subprocess.call([cmd_cp_without],shell=True)

    def auto_refresh(self):
        self.centralwidget.setEnabled(False)
        self.lbl_error_start.setText(u"<p></p>")
        if self.git != False:
            GC.set_project_id(self.git,CP.get_gitlab_connection()["gitlab_project_name"])
        self.auto_check_and_refresh()
        self.warn_if_fw_runs()
        self.centralwidget.setEnabled(True)

    def auto_check_and_refresh(self):
        new_config = CP.get_configs()
        check_gitlab_conn=[False,False]
        check_path = start_fw.check_config_paths(CP.get_path_configs())
        if new_config != self.old_config:
            check_gitlab_conn = GC.check_gitlab_connection(CP.get_gitlab_configs())
        else:
            check_gitlab_conn[0]=True
            check_gitlab_conn[1]=self.git
        if check_gitlab_conn[0] == True:
            if check_gitlab_conn[1]!=self.git:
                self.git = check_gitlab_conn[1]
            check_gitlab_sett = GC.check_gitlab_settings(self.git,CP.get_gitlab_configs())

        if check_path == True and check_gitlab_conn[0] == True and check_gitlab_sett == True:
            self.lbl_error_start.setText("")
            self.btn_merge_control.setEnabled(True)
            self.btn_deny_control.setEnabled(True)
            self.btn_start_fwbuilder.setEnabled(True)
            self.btn_watch_merge.setEnabled(True)
            self.auto_check_git_merge(self.git)
            self.warn_if_fw_runs()
            return True
        else:
            self.git_status = False
            self.btn_merge_control.setEnabled(False)
            self.btn_deny_control.setEnabled(False)
            self.btn_start_fwbuilder.setEnabled(False)
            self.btn_watch_merge.setEnabled(False)
            self.lbl_merge_control.setText("")
            self.lbl_merge_control.setText("")
            if check_path != True:
                self.set_error_message(check_path)
            elif check_gitlab_conn[0] != True:
                self.set_error_message(check_gitlab_conn[0])
            else:
                self.set_error_message(check_gitlab_sett)
            return False

    def auto_check_git_merge(self,git):
        self.lbl_error_start.setText("<p></p>")
        self.centralwidget.setEnabled(False)

        git_status = GC.check_mergerequest(git,CP.get_configs()["gitlab_project_id"]) #<<<<<
        self.git_status = git_status
        self.set_last_commit(GC.get_master_commit_id(git,CP.get_configs()["gitlab_project_id"],CP.get_configs()["gitlab_master_branch"]))
        if git_status == False:
            self.lbl_merge_control.setText(u"<p>Sistemde onay bekleyen kurallar bulunuyor.<br/>Son durumunu kontrol etmek için lütfen <br/>\"Onay Kontrol\" butonuna basınız.<br/><b>Not:</b> Onayda bekleyen istek olduğu sürece <br/>FWBuilder sadece okunabilir modda çalışacaktır</p>")
            self.btn_deny_control.setEnabled(False)
            self.btn_watch_merge.setEnabled(True)
        else:
            if GC.get_mergerequest_status(git,CP.get_configs()["gitlab_project_id"]) == "closed" and GC.check_merge_confirm() == True:
                self.lbl_merge_control.setText(u"<p><b>Son kural değişiklikleri reddedilmiş :</b> <br/>"+git.getmergerequestcomments(CP.get_configs()["gitlab_project_id"],git.getmergerequests(CP.get_configs()["gitlab_project_id"])[0]["id"])[-1]["note"]+"</p>")
            elif GC.get_mergerequest_status(git,CP.get_configs()["gitlab_project_id"]) == "merged":
                self.check_merge_file()
            self.btn_merge_control.setEnabled(False)
            self.btn_start_fwbuilder.setEnabled(True)
            self.btn_deny_control.setEnabled(True)
            self.btn_watch_merge.setEnabled(True)
        self.centralwidget.setEnabled(True)

    def kill_all(self):
        self.logger = Syslogger("FWBUILDER-AHTAPOT",'%(name)s %(levelname)s %(message)s',"/dev/log", self.current_user)
        self.filelogger = Filelogger("FWBUILDER-AHTAPOT",'%(asctime)s %(name)s %(levelname)s %(message)s',"/var/log/ahtapot/gdys-gui.log","a",self.current_user)
        start_fw.kill_fw()
        try:
            start_fw.kill_gui_user(self.current_user)
        except Exception as e :
            self.filelogger.send_log("error", "Error While Killing Previous GUI {}".format(str(e)))
        abs_path = os.path.abspath(__file__)
        path_list = abs_path.split("/")
        del path_list[-1]
        path_name="/".join(path_list)
        full_path = path_name + "/"
        with open(full_path + "current_user.dmr", "w") as current_user:
            current_user.write(self.current_user)
        self.filelogger.send_log("warning", " previous gui was killed by " + self.current_user + " : gui ")
        self.btn_kill_fw.setEnabled(False)
        sleep(2)
        self.load_new_rules()
        sleep(3)
        self.auto_refresh()
        self.lbl_error_start.setText(u"<b>SONLANDIRILDI</b>")
