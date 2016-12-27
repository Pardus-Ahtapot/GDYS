# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fwstartdef.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        Form.resize(522, 512)
        Form.move(350,250)
        Form.setMinimumSize(QtCore.QSize(522, 512))
        Form.setMaximumSize(QtCore.QSize(522, 512))
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 521, 511))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Açıklamalar - Yönetim Ekranı", None))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p ><span style=\" font-weight:600;\">Yerel Ayarlar ile Çalıştır:</span>Firewall Builder uygulamasını istemci bilgisayarın çalışma ortamında bulunan yapılandırma (.fwb) dosyası ile çalıştırır. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Onaylanmış Ayarlar ile Çalıştır:</span> Firewall Builder uygulamasını merkezi sürüm takip sisteminde en son onaylanmış kurallar ile çalıştırır ve istemci bilgisayarın yerel yapılandırmaları üstüne kayıt eder. Bu yapılandırmalar onaylandıktan sonra uç noktada bulunan güvenlik duvarı sunucularında etkin ve güncel çalışan kurallardır.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Onaylanmış Ayarları Göster:</span> Merkezi sürüm takip sisteminde onaylanmış son kuralları istemci bilgisayarın yerel yapılandırması üzerine yazmadan, Firewall Builder uygulamasını sadece okuma kipinde açar. Bu özellik uç noktada bulunan güvenlik duvarlarında etkin kuralları gözlemleyerek yeni kuralların düzgün ve başarılı girilmesine yardımcı olur.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Onay Kontrol:</span> Onay dalına gönderilen birleştirme talebinin durumunu sorgulayıp yeniler. Güvenlik duvarları için yapmış olduğumuz değişikliklerin onay dalındaki durumunu sorgulayıp işin takibini kolaylaştırmayı hedefleyen bir özelliktir.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Son Onaylanmış Commit ID:</span> Merkezi sürüm takip sisteminde onaylanmış son commit’in kimliği. Merkezi sürüm takip sistemi, yapılan bütün değişikliklere bir kimlik atar. Bu yöntem geçmişe yönelik yapılacak işlemlerde kolaylık sağlar.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))



