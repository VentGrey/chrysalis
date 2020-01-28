#!/usr/bin/env python3

import datetime
id = datetime.datetime.now().microsecond
print "BACKENDS: id initialized to ", id

import time

from chrysalis import config
from chrysalis.importer import my_import

while config.Prefs == None:
    print "BACKENDS: waiting for config.Prefs"
    # wait 50 ms and check again
    time.sleep(0.05)

print "BACKENDS: PORTAGE setting = ", config.Prefs.PORTAGE

if config.Prefs.PORTAGE == "portagelib":
    from chrysalis.backends import portagelib
    portage_lib = portagelib
#portage_lib = my_import(config.Prefs.PORTAGE)

print "BACKENDS: portage_lib import complete :", portage_lib

del config
del my_import


