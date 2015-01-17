# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Super_ADB2.ui'
#
# Created: Sat Jan 17 22:05:27 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import idaapi
import sys
import os
import subprocess
import inspect

idahome = idaapi.idadir("QTApps\\SuperADB")

if idahome not in sys.path:
     sys.path.insert(0, cmd_folder)


from subprocess import Popen, PIPE
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

class Ui_Adb_Helper(object):
    def setupUi(self, Adb_Helper):
        Adb_Helper.setObjectName(_fromUtf8("Adb_Helper"))
        Adb_Helper.resize(970, 765)
        Adb_Helper.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Adb_Helper.setStyleSheet(_fromUtf8("QWidget { \n"
"    background-color: #363636;\n"
"    color: #ddd;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: #2d2d2d;\n"
"    border: 1px solid #363636;\n"
"}\n"
"\n"
"QMenuBar, QMenuBar::item {\n"
"    background-color: #444444;\n"
"    color: #ddd;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #474747;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QLineEdit:hover, QLineEdit:focus {\n"
"    border: 1px solid #00aaaa;    \n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #555555, stop: 1 #444444);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #777777;\n"
"}\n"
"\n"
"QTreeView::item {\n"
"    font-size: 8px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #444;\n"
"    border-left: 3px solid #666;\n"
"\n"
"}\n"
"\n"
"QTableView {\n"
"    border: 1px solid #474747;\n"
"}\n"
"\n"
"QTableView {\n"
"    background-color: #2d2d2d;\n"
"}\n"
"\n"
"IDAView, hexview_t, CustomIDAMemo {\n"
"    font-family: \"Consolas\";\n"
"    font-size: 9pt;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar {\n"
"    background-color: #363636;\n"
"    width: 20px;\n"
"    margin: 0 0 0 0;\n"
"}\n"
"\n"
"QScrollBar::sub-line, QScrollBar::add-line {\n"
"    background: none;\n"
"}\n"
"\n"
"/*\n"
"QScrollBar:horizontal {\n"
"    padding: 0 20px 0 20px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    padding: 20px 0 20px 0;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    image: url(%down-arrow.png%);\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"    width: 20px;\n"
"}*/\n"
"\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background-color: #585858;\n"
"    margin: 3px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QToolBar {\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 1px solid #077;\n"
"    text-align: center;\n"
"    min-height: 20px;\n"
"    min-width: 50px;\n"
"    \n"
"    padding: 0 6px 0 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 1px solid #0aa;\n"
"}\n"
"\n"
"QPushButton::text {\n"
"    background-color: red;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid #474747;\n"
"}\n"
"\n"
"GraphQObject {\n"
"    background-color: red;\n"
"    padding: 100px;\n"
"}\n"
"\n"
"ChooserContainer {\n"
"    border: 1px solid green;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 6px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"min-width: 80px;\n"
"}\n"
" \n"
"QPushButton:hover {\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb);\n"
"}\n"
" \n"
"QPushButton:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}\n"
""))
        self.tab_android = QtGui.QWidget()
        self.tab_android.setObjectName(_fromUtf8("tab_android"))
        self.but_1 = QtGui.QPushButton(self.tab_android)
        self.but_1.setGeometry(QtCore.QRect(10, 10, 251, 91))
        self.but_1.setObjectName(_fromUtf8("but_1"))
        self.but_2 = QtGui.QPushButton(self.tab_android)
        self.but_2.setGeometry(QtCore.QRect(10, 110, 251, 71))
        self.but_2.setObjectName(_fromUtf8("but_2"))
        self.but_3 = QtGui.QPushButton(self.tab_android)
        self.but_3.setGeometry(QtCore.QRect(10, 190, 251, 81))
        self.but_3.setObjectName(_fromUtf8("but_3"))
        self.but_4 = QtGui.QPushButton(self.tab_android)
        self.but_4.setGeometry(QtCore.QRect(10, 280, 251, 91))
        self.but_4.setObjectName(_fromUtf8("but_4"))
        self.but_5 = QtGui.QPushButton(self.tab_android)
        self.but_5.setGeometry(QtCore.QRect(10, 380, 251, 101))
        self.but_5.setObjectName(_fromUtf8("but_5"))
        Adb_Helper.addTab(self.tab_android, _fromUtf8(""))
        self.tab_gdb = QtGui.QWidget()
        self.tab_gdb.setObjectName(_fromUtf8("tab_gdb"))
        self.but_7 = QtGui.QPushButton(self.tab_gdb)
        self.but_7.setGeometry(QtCore.QRect(10, 120, 251, 71))
        self.but_7.setObjectName(_fromUtf8("but_7"))
        self.but_8 = QtGui.QPushButton(self.tab_gdb)
        self.but_8.setGeometry(QtCore.QRect(10, 200, 251, 81))
        self.but_8.setObjectName(_fromUtf8("but_8"))
        self.but_9 = QtGui.QPushButton(self.tab_gdb)
        self.but_9.setGeometry(QtCore.QRect(10, 290, 251, 91))
        self.but_9.setObjectName(_fromUtf8("but_9"))
        self.but_6 = QtGui.QPushButton(self.tab_gdb)
        self.but_6.setGeometry(QtCore.QRect(10, 20, 251, 91))
        self.but_6.setObjectName(_fromUtf8("but_6"))
        self.but_10 = QtGui.QPushButton(self.tab_gdb)
        self.but_10.setGeometry(QtCore.QRect(10, 390, 251, 101))
        self.but_10.setObjectName(_fromUtf8("but_10"))
        Adb_Helper.addTab(self.tab_gdb, _fromUtf8(""))
        self.tab_pids = QtGui.QWidget()
        self.tab_pids.setObjectName(_fromUtf8("tab_pids"))
        self.textEdit_3 = QtGui.QTextEdit(self.tab_pids)
        self.textEdit_3.setGeometry(QtCore.QRect(0, 0, 791, 731))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.but_Pids = QtGui.QPushButton(self.tab_pids)
        self.but_Pids.setGeometry(QtCore.QRect(800, 660, 161, 71))
        self.but_Pids.setObjectName(_fromUtf8("but_Pids"))
        Adb_Helper.addTab(self.tab_pids, _fromUtf8(""))
        self.tab_Logcat = QtGui.QWidget()
        self.tab_Logcat.setObjectName(_fromUtf8("tab_Logcat"))
        self.textEdit_2 = QtGui.QTextEdit(self.tab_Logcat)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 0, 781, 731))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.but_logcat = QtGui.QPushButton(self.tab_Logcat)
        self.but_logcat.setGeometry(QtCore.QRect(790, 660, 161, 71))
        self.but_logcat.setObjectName(_fromUtf8("but_logcat"))
        Adb_Helper.addTab(self.tab_Logcat, _fromUtf8(""))
        self.tab_shell = QtGui.QWidget()
        self.tab_shell.setObjectName(_fromUtf8("tab_shell"))
        self.textEdit = QtGui.QTextEdit(self.tab_shell)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 771, 701))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.but_shell = QtGui.QPushButton(self.tab_shell)
        self.but_shell.setGeometry(QtCore.QRect(810, 630, 141, 71))
        self.but_shell.setObjectName(_fromUtf8("but_shell"))
        Adb_Helper.addTab(self.tab_shell, _fromUtf8(""))
        self.tab_misc = QtGui.QWidget()
        self.tab_misc.setObjectName(_fromUtf8("tab_misc"))
        self.But_su = QtGui.QPushButton(self.tab_misc)
        self.But_su.setGeometry(QtCore.QRect(20, 20, 181, 71))
        self.But_su.setObjectName(_fromUtf8("But_su"))
        self.but_reboot = QtGui.QPushButton(self.tab_misc)
        self.but_reboot.setGeometry(QtCore.QRect(20, 100, 181, 71))
        self.but_reboot.setObjectName(_fromUtf8("but_reboot"))
        Adb_Helper.addTab(self.tab_misc, _fromUtf8(""))
        self.tab_sheet = QtGui.QWidget()
        self.tab_sheet.setObjectName(_fromUtf8("tab_sheet"))
        self.textEdit_4 = QtGui.QTextEdit(self.tab_sheet)
        self.textEdit_4.setGeometry(QtCore.QRect(0, 0, 971, 741))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        Adb_Helper.addTab(self.tab_sheet, _fromUtf8(""))

        self.retranslateUi(Adb_Helper)
        Adb_Helper.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(Adb_Helper)
        Adb_Helper.setTabOrder(self.but_1, self.but_2)
        Adb_Helper.setTabOrder(self.but_2, self.but_3)
        Adb_Helper.setTabOrder(self.but_3, self.but_4)
        Adb_Helper.setTabOrder(self.but_4, self.but_5)
        Adb_Helper.setTabOrder(self.but_5, self.but_6)
        Adb_Helper.setTabOrder(self.but_6, self.but_7)
        Adb_Helper.setTabOrder(self.but_7, self.but_8)
        Adb_Helper.setTabOrder(self.but_8, self.but_9)
        Adb_Helper.setTabOrder(self.but_9, self.but_10)
        Adb_Helper.setTabOrder(self.but_10, self.textEdit_3)
        Adb_Helper.setTabOrder(self.textEdit_3, self.but_Pids)
        Adb_Helper.setTabOrder(self.but_Pids, self.textEdit_2)
        Adb_Helper.setTabOrder(self.textEdit_2, self.but_logcat)
        Adb_Helper.setTabOrder(self.but_logcat, self.textEdit)
        Adb_Helper.setTabOrder(self.textEdit, self.but_shell)
        Adb_Helper.setTabOrder(self.but_shell, self.But_su)
        Adb_Helper.setTabOrder(self.But_su, self.but_reboot)
        Adb_Helper.setTabOrder(self.but_reboot, self.textEdit_4)

    def retranslateUi(self, Adb_Helper):
        Adb_Helper.setWindowTitle(_translate("Adb_Helper", "Ida Pro Adb Helper", None))
        Adb_Helper.setToolTip(_translate("Adb_Helper", "<html><head/><body><p><br/></p></body></html>", None))
        self.but_1.setToolTip(_translate("Adb_Helper", "<html><head/><body><p>restart daemon as root</p></body></html>", None))
        self.but_1.setText(_translate("Adb_Helper", "1. adb Restart as Root", None))
        self.but_2.setToolTip(_translate("Adb_Helper", "<html><head/><body><p>Push to /data/data</p></body></html>", None))
        self.but_2.setText(_translate("Adb_Helper", "2. push android server to rooted phone", None))
        self.but_3.setToolTip(_translate("Adb_Helper", "<html><head/><body><p>permission 755 for android_server</p></body></html>", None))
        self.but_3.setText(_translate("Adb_Helper", "3. chmod android server 755", None))
        self.but_4.setToolTip(_translate("Adb_Helper", "<html><head/><body><p>Forward ports 23946 to / from Ida Pro</p></body></html>", None))
        self.but_4.setText(_translate("Adb_Helper", "4. adb Forward ports for debugging", None))
        self.but_5.setToolTip(_translate("Adb_Helper", "<html><head/><body><p>If everything is working ida should connect.</p><p>Showing list of Pids to attach.</p><p>Happy Debugging.</p></body></html>", None))
        self.but_5.setText(_translate("Adb_Helper", "5. connect to android server", None))
        Adb_Helper.setTabText(Adb_Helper.indexOf(self.tab_android), _translate("Adb_Helper", "Android Server Menu", None))
        self.but_7.setToolTip(_translate("Adb_Helper", "<html><head/><body><p>Push to /data/data</p></body></html>", None))
        self.but_7.setText(_translate("Adb_Helper", "2. push Gdbserver to rooted phone", None))
        self.but_8.setToolTip(_translate("Adb_Helper", "<html><head/><body><p>permission 755 for Gdbserver</p></body></html>", None))
        self.but_8.setText(_translate("Adb_Helper", "3. chmod gdbserver 755", None))
        self.but_9.setToolTip(_translate("Adb_Helper", "<html><head/><body><p>Forward ports 23946 to / from Ida Pro</p></body></html>", None))
        self.but_9.setText(_translate("Adb_Helper", "4. adb Forward ports for debugging", None))
        self.but_6.setToolTip(_translate("Adb_Helper", "<html><head/><body><p>restart daemon as root</p></body></html>", None))
        self.but_6.setText(_translate("Adb_Helper", "1. adb Restart as Root", None))
        self.but_10.setToolTip(_translate("Adb_Helper", "<html><head/><body><p>If everything is working ida should connect.</p><p>NP !! use Pids tab to get running Pids.</p><p>Attach to GDB Server and put in the PID.</p><p>If you loaded a File in ida allready you can just attach to target.</p><p>Happy Debugging.</p></body></html>", None))
        self.but_10.setText(_translate("Adb_Helper", "5. Start gdbserver for attaching", None))
        Adb_Helper.setTabText(Adb_Helper.indexOf(self.tab_gdb), _translate("Adb_Helper", "GDB Server Menu", None))
        self.but_Pids.setText(_translate("Adb_Helper", "Show runing Pids", None))
        Adb_Helper.setTabText(Adb_Helper.indexOf(self.tab_pids), _translate("Adb_Helper", "Pids", None))
        self.but_logcat.setText(_translate("Adb_Helper", "Connect to Logcat", None))
        Adb_Helper.setTabText(Adb_Helper.indexOf(self.tab_Logcat), _translate("Adb_Helper", "Logcat", None))
        self.but_shell.setText(_translate("Adb_Helper", "Connect Adb shell", None))
        Adb_Helper.setTabText(Adb_Helper.indexOf(self.tab_shell), _translate("Adb_Helper", "Adb Shell", None))
        self.But_su.setText(_translate("Adb_Helper", "Push SuperUser to Phone", None))
        self.but_reboot.setText(_translate("Adb_Helper", "Reboot phone", None))
        Adb_Helper.setTabText(Adb_Helper.indexOf(self.tab_misc), _translate("Adb_Helper", "Misc", None))
        self.textEdit_4.setHtml(_translate("Adb_Helper", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Android Debug Bridge</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Cheat Sheet</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Selecting a device</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">adb devices                                        List of devices</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">by serial number.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">adb devices -l                       List of devices</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">by product/model.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">adb -s &lt;serial&gt; ...            Command line selection.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">export ANDROID_SERIAL=&lt;serial&gt;  Env. variable selection.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">If a command starts with $ it has to be run from the Android shell or via adb shell &lt;command&gt;, or </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">even better</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">adb shell &lt;command&gt; | less.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Package installation</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">adb install &lt;apk&gt;                    Installs app.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ pm install &lt;path&gt;              Install app from phone path.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ pm install -r &lt;path&gt;         Reinstall app from phone path.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ pm uninstall &lt;name&gt;            Remove the app.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$  pm  get-install-location    Install location:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">0 - Auto</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1 - Internal</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2 - External</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Package info</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ pm list packages                 List package names.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ pm list packages -f         As above + path to apks.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ pm list packages -3             Only third party packages.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ pm list packages -s            Only system packages.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ pm list packages -u            Also uninstalled packages.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ dumpsys package packages   List info on all apps.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ pm dump &lt;name&gt;                    List info on one package.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ pm path &lt;package&gt;                Path to the apk file.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Permissions</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ pm permission groups            Permission groups definitions.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ pm list permissions -g -f  List permissions details.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">File  operations</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">adb push &lt;local&gt; &lt;remote&gt;    Copy file/dir to device. adb pull &lt;remote&gt; [&lt;local&gt;]  Copy file/dir </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">from device.  adb backup -f &lt;file&gt; [&lt;packages...&gt;]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Backup the phone.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Paths</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">/data/data/&lt;package&gt;     App data, as described below.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">databases/             App databases.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">shared prefs/          Shared preferences.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">/data/app                 APK files installed by user.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">/system/app               Pre-installed APK files.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">/mnt/asec                 Encrypted apps (App2SD).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">/mnt/emmc                 Internal SD Card.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">/mnt/sdcard               External/Internal SD Card.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">/mnt/sdcard/external sd  External SD Card.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Phone info</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$  sqlite3  /data/data/</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">com.android.providers.settings/ databases/settings.db .dump</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Dump phone settings.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ getprop                          Get properties (e.g. model).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ dumpsys iphonesubinfo   Get the IMEI.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">adb get-serialno                Get the serial number.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ dumpsys battery              Battery status.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ pm list users                Lists phone users (4.1+).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ pm list features                                tures.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Services &amp; activities</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ service list                   List all services.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ dumpsys activity &lt;package&gt;/&lt;activity&gt;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Activity info.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Activity Manager usage:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$  am  start|startservice|broadcast  &lt;INTENT&gt;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">[&lt;COMPONENT&gt;]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">where &lt;INTENT&gt; is specified with following options:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">-a  &lt;ACTION&gt;          e.g.  android.intent.action.VIEW</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">-c &lt;CATEGORY&gt;   e.g. android.intent.category.LAUNCHER</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Common actions</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">To open the URL:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$  am  start  -a  android.intent.action.VIEW  -d  URL</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Logs</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">All logs are accessed by using either</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ logcat  [options] [filter] [filter] . . .</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">adb  logcat  [options]  [filter] [filter] . . .</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Useful options are:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">-d                              Only dump logs (do not block).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">-c                              Flush the buffers.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">-b &lt;buffer&gt;             Buffer to display (default: system, main).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">&lt;tag&gt;[:priority]   filter spec at the end of command.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Available priorities are:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">V   Verbose</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">D   Debug</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">I  Info</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">W    Warn</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">E   Error</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">F    Fatal</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">S   Silent (suppress all output)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Other useful log information:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ dumpstate   Dump current phone state.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ dumpsys      Dump all system data.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Miscellaneous</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ screencap -p &lt;path&gt;.png    Screenshot (saved on device).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">$ screenrecord &lt;path&gt;.mp4    Screen capture (path on device).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">ADB daemon</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">adbd runs on TCP/5037.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">adb kill-server     Kill the server if it is running.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">adb start-server   Ensure that there is a server running.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">adb root                 Restarts the adbd with root permissions.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">v 0.2 by @maldr0id</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">based on LATEX cheat sheet by Winston Chang</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">http://www.stdout.org/∼winston/latex/</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        Adb_Helper.setTabText(Adb_Helper.indexOf(self.tab_sheet), _translate("Adb_Helper", "Cheat sheet", None))



        '''
        Buttons tab androis
        '''

        self.but_1.clicked.connect(self.Restart)
        self.but_2.clicked.connect(self.Pusha)
        self.but_3.clicked.connect(self.chmoda)
        self.but_4.clicked.connect(self.portsa)
        self.but_5.clicked.connect(self.connecta)

        '''
        buttons tab gdbserver
        '''
        self.but_6.clicked.connect(self.Restartb)
        self.but_7.clicked.connect(self.Pushb)
        self.but_8.clicked.connect(self.chmodb)
        self.but_9.clicked.connect(self.portsb)
        self.but_10.clicked.connect(self.connectb)


        '''
        buttons PIDS Tempory to i figure out howto paste to screen
        '''
        self.but_Pids.clicked.connect(self.Showless)

        '''
        Button logcar temperay to i fugure out howto paste to screen
        '''
        self.but_logcat.clicked.connect(self.Logger)

        '''
        button for shell tab for now
        '''
        self.but_shell.clicked.connect(self.Shelf)

        '''
        button for misc
        '''
        self.But_su.clicked.connect(self.Installsu)
        self.but_reboot.clicked.connect(self.Boot)



    '''
    define buttons android group
    '''
    def Restart(self):
        subprocess.Popen('adb.exe root')

    def Pusha(self):
        subprocess.Popen('adb.exe push android_server /data/data/android_server')

    def chmoda(self):
        subprocess.Popen('adb.exe shell chmod 755 /data/data/android_server')

    def portsa(self):
        subprocess.Popen('adb forward tcp:23946 tcp:23946')

    def connecta(self):
        subprocess.Popen('adb.exe shell ./data/data/android_server')
        print 'Should be connected'
    '''
    define buttons gdbserver group
    '''
    def Restartb(self):
        subprocess.Popen('adb.exe root')

    def Pushb(self):
        subprocess.Popen('adb.exe push gdbserver /data/data/gdbserver')

    def chmodb(self):
        subprocess.Popen('adb.exe shell chmod 755 /data/data/gdbserver')

    def portsb(self):
        subprocess.Popen('adb forward tcp:23946 tcp:23946')

    def connectb(self):
        subprocess.Popen('adb.exe shell ./data/data/gdbserver --multi localhost:23946')
        print 'Should be connected'


    '''
    DEfine Pids button
    '''
    def Showless(self):
        import sys
        import os

        from subprocess import Popen, PIPE
        output = subprocess.Popen('adb shell ps', stdout=PIPE)
        print output.stdout.read()

    '''
    DEfine logcat button
    '''

    def Logger(self):
         subprocess.Popen('adb logcat')

    '''
    define shell button
    '''
    def Shelf(self):
        subprocess.Popen('adb shell')
        print "Look at CheatSheet for help""
    '''
    Define misc buttons
    '''
    def Installsu(self):
        subprocess.Popen('adb install busybox.apk')

    def Boot(self):
        subprocess.Popen('adb reboot')

    #def callProgramps(self):
        # run the process
        # `start` takes the exec and a list of arguments
        #self.process.start('adb shell ')
        #self.output = QtGui.QTextEdit()

        #layout.addWidget(self.output)
        #layout.addWidget(self.but_Pids)
        # QProcess object for external app
        #self.process = QtCore.QProcess(self)


        # QProcess emits `readyRead` when there is data to be read

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication.instance()
    if not app:
        app = QtGui.QApplication([])
    Adb_Helper = QtGui.QTabWidget()
    ui = Ui_Adb_Helper()
    ui.setupUi(Adb_Helper)
    Adb_Helper.show()
    app.exec_()

