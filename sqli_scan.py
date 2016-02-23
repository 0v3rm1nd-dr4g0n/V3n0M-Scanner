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


def sqli(connector, progress):
    logger = logging.getLogger(__name__)
    progress.set(0, 100)
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
