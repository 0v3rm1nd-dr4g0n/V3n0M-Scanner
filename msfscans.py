import gettext
import logging
import string
import sys
import time
import urllib
import re
import random
import blessings
import threading
import socket
import os
import subprocess
import itertools

_ = gettext.gettext
d0rk = [line.strip() for line in open("statics/d0rks", 'r')]
header = [line.strip() for line in open("statics/header", 'r')]
xsses = [line.strip() for line in open("statics/xsses", 'r')]
lfis = [line.strip() for line in open("statics/lfi", 'r')]
search_Ignore = str(line.rsplit('\n') for line in open("statics/search_ignore", 'r'))
msf_search_Ignore = str(line.rsplit('\n') for line in open("statics/scannerblocklist", 'r'))
random.shuffle(d0rk)
random.shuffle(header)
random.shuffle(lfis)
ProxyEnabled = False


def msfscans(connector, progress):
    logger = logging.getLogger(__name__)
    progress.set(0, 1000)
    while ProxyEnabled = False
    tempvar1 = ""
    tempvar2 = ""
    tempvar3 = ""
    tempvar4 = ""
    for i in range(100, 0, -1):
        logger.info(_('Countdown value is %i'), i)
        progress.tick()
        connector.ack()

    logger.info(_('Done!'))


if __name__ == '__main__':
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)
