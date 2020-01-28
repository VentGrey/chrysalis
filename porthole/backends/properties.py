#!/usr/bin/env python3

import datetime
id = datetime.datetime.now().microsecond
print "PROPERTIES: id initialized to ", id


class Properties:
    """Contains all variables in an ebuild."""
    def __init__(self, dict = None):
        self.__dict = dict
        #dprint("PORTAGELIB: Properties=")
        #dprint(dict)
        
    def __getattr__(self, name):
        try: return self.__dict[name]
        except: return ''
        
    def get_slot(self):
        """Return ebuild slot"""
        return self.slot

    def get_keywords(self):
        """Returns a list of strings."""
        return self.keywords.split()

    def get_use_flags(self):
        """Returns a list of strings."""
        return self.iuse.split()

    def get_homepages(self):
        """Returns a list of strings."""
        return self.homepage.split()
