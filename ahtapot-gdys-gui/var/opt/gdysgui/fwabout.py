# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fwabout.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(500, 400)
        Form.move(350,250)
        Form.setMinimumSize(QtCore.QSize(500, 400))
        Form.setMaximumSize(QtCore.QSize(500, 400))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 221, 381))
        self.label.setText(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(240, 10, 251, 381))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        abs_path = os.path.abspath(__file__)
        path_list = abs_path.split("/")
        del path_list[-1]
        path_name="/".join(path_list)
        full_path = path_name + "/"

        #stylesheet
        Form.setStyleSheet(_fromUtf8("QMainWindow#Form {border-image: url("+full_path+"img/ahtapot_logo.png);}"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Ahtapot - GDYS - Hakkında", None))
        self.label.setText(_fromUtf8("<html><head></head><body>\
            <br/><br/>Ahtapot GDYS arayüz uygulaması,<br/> güvenlik duvarlarına uygulanacak<br/> yapılandırma kurallarının\
            onay <br/>mekanizmasından geçerek, merkezi <br/>yönetim sistemiyle uygulanmasını <br/>sağlar.\
            <br/><br/><br/>Bu arayüz, onay mekanizması<br/> hakkında son durumu kontrol<br/> eder ve sonuca göre\
            kullanıcının<br/> yapabileceği işlemler hakkında <br/>kullanıcıyı bilgilendirir.\
            </body></html>"))
        self.label_2.setText(_fromUtf8("<html><head></head><body>\
         <br/><br/><br/><br/><b>Ahtapot</b><br/> www.ahtapot.org.tr<br/>\
         <b>ULAKBİM</b><br/> ulakbim.tubitak.gov.tr\
            </body></html>"))


