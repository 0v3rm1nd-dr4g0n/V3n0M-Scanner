import gettext
import logging

import CumulativeLogger
import MainWindowApp

_ = gettext.gettext

logging.basicConfig()
l = logging.getLogger()
l.setLevel(logging.INFO)
cl = CumulativeLogger.CumulativeLogger()
l.info(_('Starting Dork Scanner Logging'))
MainWindowApp.MainWindowApp(cl).run()
