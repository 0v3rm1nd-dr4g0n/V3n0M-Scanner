import gettext
import logging
import tkinter as Tkinter
from tkinter import *
import ActionWindow
import sqli_scan
import thread_Handler
import view_Log

_ = gettext.gettext


class MainWindowApp:
    def __init__(self, log):
        """ Remember cumulative log, get logger """
        self.log = log
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self):
        """ Create and run GUI """
        self.root = root = Tkinter.Tk()
        root.title(_('Venom-Scanner V.4.0.4'))
        Tkinter.Button(root, text=_('Start SQL Dork Scan'), command=self.onStart, width=40).pack(side=Tkinter.TOP)
        d0rks = Entry(root)
        d0rks.insert(END, 'dorks amount')
        domain = Entry(root)
        domain.insert(END, 'domain, ie .com')
        d0rks.pack(side=Tkinter.TOP)
        domain.pack(side=Tkinter.TOP)
        Tkinter.Button(root, text=_('View SQL Log'), command=self.onViewLog, width=40).pack(side=Tkinter.TOP)
        Tkinter.Button(root, text=_('Start Msf-Exploitable Scan'), command=self.onViewLog, width=40).pack(
            side=Tkinter.TOP)
        Tkinter.Button(root, text=_('View Msf-Exploits Log'), command=self.onViewLog, width=40).pack(side=Tkinter.TOP)
        Tkinter.Button(root, text=_('Start Admin Panel Finder'), command=self.onViewLog, width=40).pack(
            side=Tkinter.TOP)
        Tkinter.Button(root, text=_('Exit'), command=self.onExit, width=40).pack(side=Tkinter.TOP)
        root.mainloop()

    def onExit(self):
        """ Process 'Exit' command """
        self.root.quit()
        self.root.destroy()

    def onViewLog(self):
        """ Process 'View Log' command """
        view_Log.ViewLog(self.root, self.log)

    def onStart(self):
        """ Process 'Start' command """
        self.logger.info(_('Preparing and starting calculations'))
        conn = thread_Handler.ThreadsConnector()
        wnd = ActionWindow.ActionWindow(self.root, _('Countdown Calculations'), _('Counting down from 100 to 1'))
        conn.runInGui(wnd, conn, None, sqli_scan, 'sqli')
