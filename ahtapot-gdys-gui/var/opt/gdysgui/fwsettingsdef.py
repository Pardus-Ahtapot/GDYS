# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fwsettingsdef.ui'
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
        Form.move(350,250)
        Form.resize(522, 512)
        Form.setMinimumSize(QtCore.QSize(522, 512))
        Form.setMaximumSize(QtCore.QSize(522, 512))
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 521, 511))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Açıklamalar - Yapılandırma Ayarları", None))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Kilidi Aç:</span> Yapılandırmaları düzenleyebilmek için merkezi yönetim sistemi sunucusunda root kullanıcısı yetkilerine parola ile geçiş sağlar. Bu özellikle yapılandırmalarımıza bir güvenlik katmanı eklemiş oluyoruz. Uygulamanın yardımcı yan uygulamalara erişim bilgileri gibi hassas bilgilerin bulunduğu bu alana erişim parola kullanımı ile sağlanmaktadır.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Onay Mekanizması:</span> Açık olduğunda yapılan değişiklikler merkezi sürüm takip sistemine (GitLab) onay alınması için deponun onay dalından ana dala birleştirme isteği gönderilir; kapalı olduğunda onay dalını atlayarak ana dala direk birleşir. Ana dala birleşen değişiklik merkezi yapılandırma aracı tarafından işleme alınır.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">GitLab Yapılandırma:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">- GitLab Bağlantı Adresi:</span> GitLab uygulamasına erişmek için, tarayıcınızda da kullanılan bağlantı adresi. Uygulama, GitLab yani merkezi sürüm takip sistemine HTTP veya HTTPS protokolü üzerinden bağlanarak Onay Kontrol, Son Onaylanmış Commit ID gibi özelliklerin çalışmasını sağlar. Bu veri yanlış girildiğinde uygulama çalışmayacaktır.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">- GitLab Kullanıcı Adı:</span> GitLab uygulamasında oturum açmak için kullanılan API kullanıcı adı. GitLab bağlantı adresi ile birlikte bağlantıda gerçekleşecek kimlik doğrulamasında kullanılacak kullanıcı adıdır. Bu veri yanlış girildiğinde uygulama çalışmayacaktır.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">- GitLab Kullanıcı Parolası:</span> GitLab uygulamasında oturum açmak için kullanılan kullanıcı parolası. Merkezi sürüm takip sistemine gerçekleşecek bağlantıda kimlik doğrulaması yapılırken kullanılacak parola bilgisinin girildiği yerdir. Bu veri yanlış girildiğinde uygulama çalışmayacaktır.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">- GitLab Onay Dalı:</span> Yapılan değişikliklerin üst birim tarafından denetlenip onaylanacağı git deposu dalının adı. Denetleme işlemleri güncellenecek yapılandırmaların uç noktadaki güvenlik duvarı sunucularında sistemin bütünlüğü ve kararlı çalışmasını sağlamak açısından büyük önem taşımaktadır.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">- GitLab Ana Dal:</span> Git deposunun ana dalının adı. Değişiklikler onay dalında onaylandıktan sonra ana dalda birleştirilir. Bu birleştirme işleminde sonra değişiklikler uç noktalarda bulunan güvenlik duvarı sunucularında çalıştırılacak şekilde merkezi yapılandırma aracı tarafından işleme alınır.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">- GitLab Proje Adı:</span> GitLab’de bulunan deponun adı. Bu depo yapılandırmalarda yapılan değişikliklerin geçmişe yönelik takip edilmesi için sistemde konumlandırılmıştır. Güvenlik duvarı sistemlerinde yapılan her türlü değişiklik bu depoda kayıt altına alınır. Verinin yanlış girilmesi halinde uygulama çalışmayacaktır.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Dizin Yapılandırma:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">- Yapılandırma Dosya Adı:</span> Güvenlik duvarı ayarlarının bulunduğu Firewall Builder yapılandırma dosyası. Firewall Builder uygulamasında yapılan değişiklikler bu dosyaya kaydedilir ve Firewall Builder arayüzünden yapılan Install işlemi ile değişiklikler ilgili uç birimlere göndermek için hazırlanır. Dosyanın uzantısı .fwb olmalıdır. Verinin yanlış girilmesi halinde uygulama çalışmayacaktır.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">- Test Betikleri Dizini:</span> Firewall Builder ile oluşturulan kural betikleri, test makinasında iptables kurallarının doğru çalışıp çalışmadığını test etmek için gerekli olmayan fonksiyonları (verify_interfaces, change_interfaces vb.) ayrıştırır ve yeni bir betik dosyası oluşturulur. Bu dosya test makinasına gönderilmeden önce bu dizine konumlandırılır. Bu dizinden de test makinasına kopyalama işlemi yapılır. Test işlemi yapıldıktan sonra, kopya betikler silinir, bu şekilde bir sonraki çalışmalarla çakışmalar önlenir. Bu dizin uygulamanın çalıştığı dosya sistemi üzerindedir. Verinin yanlış girilmesi halinde uygulama çalışmayacaktır.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">- Hata Bildirim Dizini:</span> Test makinasına yapılan değişikliklerin denetimi esnasında karşılaşılan hataların yazıldığı dizin. Hataları .stderr ve .stdout son ekine sahip dosyalara yazar. Uygulamada karşılaşılan sorunların geçmişe yönelik araştırılması ve hata giderme süreçleri için bu dosyalar önem taşımaktadır. Verinin yanlış girilmesi halinde uygulama çalışmayacaktır.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">- Test Makinası IP Adresi:</span> Bu sunucunun erişilebilir IP adresinin girileceği alandır. Güvenlik duvarlarında yapılan değişikliklerin ağ arabirim ile ilgili bölümleri devre dışı bırakarak önceden kurulmuş ve yapılandırılmış bir sunucuya gönderilir ve ilgili sunucuda test edilir. Bu aşama değişen güvenlik duvarı kurallarının onaydan önce test edilmesi açısından önemlidir. Bu sunucu altyapıda bulunmadığı ve verilerinin yanlış girilmesi halinde uygulama çalışmayacaktır.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">- Test Makinası Kullanıcı Adı:</span> Test makinasına erişim kimlik doğrulamasında sağlanacak kullanıcı adı. Bu veri girilmediyse uygulama çalışmayacaktır.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">- Test Makinası Betik Dizini:</span> Yapılan değişiklikler sonucu yaratılan betik dosyasının test makinasında konumlanacağı dizin. İlgili sunucuda bu dizin oluşturulup dizin hakları doğru verilmediyse uygulama çalışmayacaktır.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Yardım:</span> Uygulamanın çalışma yöntemi ve özelliklerini gösterir.</p></body></html>", None))



