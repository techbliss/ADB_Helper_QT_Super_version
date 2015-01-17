__author__ = 'zadow aka Storm Shadow'
import re
import idaapi
import idc
from idc import *
from idaapi import *
import PyQt4
from PyQt4 import QtCore, QtGui
import idautils

class Adb(idaapi.plugin_t):
    flags = idaapi.PLUGIN_FIX
    comment = "This is a comment"

    help = "Plugin "
    wanted_name = "ADB PyQT ADB connector for android server & gdbserver"
    wanted_hotkey = "Alt-F7"



    def init(self):
        idaapi.msg(" ADB Plugin is found. \n")
        return idaapi.PLUGIN_OK

    def run(self, arg):
        idaapi.msg("run() called with %d!\n" % arg)

    def term(self):
        idaapi.msg("")

    def AddMenuElements(self):
        '''Menus are better than no GUI at all *sigh*'''

        idaapi.add_menu_item("Edit/Plugins/", "ADB Super Connector", "", 0, self.AdbCall, ())




    def run(self, arg = 0):
        idaapi.msg("Looks like its working")

        self.AddMenuElements()

    def AdbCall(self):
        g = globals()
        idahome = idaapi.idadir("QTApps\\SuperADB")
        IDAPython_ExecScript(idahome +  "\\ADB_QT.py", g)



def PLUGIN_ENTRY():
    return Adb()
