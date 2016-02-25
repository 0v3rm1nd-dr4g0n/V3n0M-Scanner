#!/usr/bin/python
# -*- coding: latin-1 -*-
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
import asyncio
import aiohttp

global maxc
global usearch
global numthreads
global threads
global finallist
global finallist2
global col
global darkurl
global sitearray
global loaded_Dorks
threads = []
finallist = []
finallist2 = []
col = []
darkurl = []
loaded_Dorks = []


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


@asyncio.coroutine
def search(maxc, connector, progress):
    urls = []
    progress.set(0, 1000)
    logger = logging.getLogger(__name__)
    urls_len_last = 0
    for site in sitearray:
        dark = 0
        for dork in loaded_Dorks:  # load dorks selected earlier to run checks with
            dark += 1
            page = 0
            try:
                while page < int(maxc):
                    try:
                        query = dork + "+site:" + site
                        results_web = 'http://www.bing.com/search?q=' + query + '&go=Submit+Query&qs=ds' \
                                      + 'ds&form=QBLH' + repr(page) + '&count=50'
                        response = yield from aiohttp.request('GET', results_web)
                        assert response.status == 200
                        content = yield from response.text()
                        stringreg = re.compile('(?<=href=")(.*?)(?=")')
                        names = stringreg.findall(content)
                        page += 1
                        progress.tick()
                        connector.ack()
                        for name in names:
                            if name not in urls:
                                if re.search(r'\(', name) or re.search("<", name) or re.search("\A/",
                                                                                               name) or re.search(
                                    "\A(http://)\d", name):
                                    pass
                                elif re.search(search_Ignore, name):
                                    pass
                                elif re.search(site, name):
                                    urls.append(name)
                        darklen = len(loaded_Dorks)
                        percent = int((1.0 * dark / int(darklen)) * 100)
                        urls_len = len(urls)
                        logger.info(
                            "\r\x1b[KSite: %s | Collected urls: %s | D0rks: %s/%s | Percent Done: %s | Current page no.: <%s> | Dork: %s" % (
                                site, repr(urls_len), dark, darklen, repr(percent), repr(page), dork))
                        if urls_len == urls_len_last:
                            page = int(maxc)
                        urls_len_last = len(urls)
                    except(
                            KeyboardInterrupt,
                            SystemExit):  # following except throws me connection debug info it it breaks
                        raise
            except(socket.gaierror, socket.error, socket.timeout):
                pass
    tmplist = []
    print("\n\n[+] URLS (unsorted): ", len(urls))
    for url in urls:
        try:
            host = url.split("/", 3)
            domain = host[2]
            if domain not in tmplist and "=" in url:
                finallist.append(url)
                tmplist.append(domain)

        except:
            pass
    logger.info(_("[+] URLS (sorted)  : ", len(finallist)))
    return finallist


if __name__ == '__main__':
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)
