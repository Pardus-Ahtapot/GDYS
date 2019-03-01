#!/usr/bin/env python
#coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import fwsettings, fwstart, fwsettingsdef, fwstartdef, fwabout
from time import sleep
import start_fw
import gitlab_check as GC
import config_parser as CP
import os
import time
import subprocess

class MovieSplashScreen(QtGui.QSplashScreen):
     def __init__(self, movie, parent = None):
        movie.jumpToFrame(0)
        pixmap = QtGui.QPixmap(movie.frameRect().size())
        QtGui.QSplashScreen.__init__(self, pixmap)
        self.movie = movie
        self.movie.frameChanged.connect(self.repaint)
     def showEvent(self, event):
        self.movie.start()

     def hideEvent(self, event):
        self.movie.stop()

     def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        pixmap = self.movie.currentPixmap()
        self.setMask(pixmap.mask())
        painter.drawPixmap(0, 0, pixmap)
     def sizeHint(self):
        return self.movie.scaledSize()

if __name__ == "__main__":
    import sys

    args = sys.argv
    active_user = ""
    if len(args) == 1:
        active_user = "BilgiYok"
    elif len(args) == 2:
        active_user = args[1]
    else:
        active_user = "BilgiYok"



    app = QtGui.QApplication(sys.argv)
    abs_path = os.path.abspath(__file__)
    path_list = abs_path.split("/")
    del path_list[-1]
    path_name="/".join(path_list)
    full_path = path_name + "/"

    app.setWindowIcon(QtGui.QIcon(full_path + "img/" + 'ahtapot_icon.png'))

    movie = QtGui.QMovie(full_path+"img/"+"splash.gif")
    splash = MovieSplashScreen(movie)
    splash.show()
    #app.aboutToQuit.connect(start_fw.kill_fw)

    #for commit message
    if start_fw.check_if_runs() is False:
        with open(full_path + "current_user.dmr", "w") as current_user:
            current_user.write(active_user)

    FwStartWindow = QtGui.QMainWindow()
    ui_start = fwstart.Ui_FwStartWindow()
    ui_start.setupUi(FwStartWindow)

    FwSettingsWindow = QtGui.QMainWindow()
    ui_settings = fwsettings.Ui_FwSettingsWindow()
    ui_settings.setupUi(FwSettingsWindow)



    FwSettingsDefWindow = QtGui.QMainWindow()
    ui_settings_def = fwsettingsdef.Ui_Form()
    ui_settings_def.setupUi(FwSettingsDefWindow)

    FwStartDefWindow = QtGui.QMainWindow()
    ui_start_def = fwstartdef.Ui_Form()
    ui_start_def.setupUi(FwStartDefWindow)

    FwAboutWindow = QtGui.QMainWindow()
    ui_about = fwabout.Ui_Form()
    ui_about.setupUi(FwAboutWindow)


    ui_settings.set_windows(FwSettingsWindow,FwStartWindow)
    ui_start.set_windows(FwStartWindow,FwSettingsWindow)

    ui_settings.def_window = FwSettingsDefWindow
    ui_start.def_window = FwStartDefWindow
    ui_start.about_window = FwAboutWindow
    ui_settings.about_window = FwAboutWindow

    ui_start.child = ui_settings
    ui_settings.parent = ui_start

    ui_start.current_user = active_user
    ui_settings.current_user = active_user


    start = time.time()

    while movie.state() == QtGui.QMovie.Running and time.time() < start + 3 :
        app.processEvents()

    gitlab_connection = GC.check_gitlab_connection(CP.get_gitlab_connection())
    if gitlab_connection[0] == True:
        git = gitlab_connection[1]
        GC.set_project_id(git,CP.get_gitlab_connection()["gitlab_project_name"])
        ui_start.check_and_refresh()
    else:
        ui_start.btn_merge_control.setEnabled(False)
        ui_start.btn_deny_control.setEnabled(False)
        ui_start.btn_start_fwbuilder.setEnabled(False)
        ui_start.btn_watch_merge.setEnabled(False)
        ui_start.lbl_merge_control.setText("")
        ui_start.set_error_message(u"Gitlab'a Bağlanılamıyor. Bilgileri ve Bağlantıyı Kontrol Ediniz...")

    ui_start.logger.send_log("info"," GUI Started")
    ui_start.filelogger.send_log("info"," GUI Started")
    FwStartWindow.show()
    splash.finish(ui_start)
    ret = app.exec_()
    subprocess.Popen(["/var/opt/gdysgui/seteditable.py", "/etc/fw/gdys/gdys.fwb", "revert"])
    sys.exit(ret)

