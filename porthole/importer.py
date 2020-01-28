#!/usr/bin/env python3

# taken from the python reference on the __import__()
# returns the last module in the name as __import__ only returns the first one

def my_import(name):
    print "IMPORTER: name = ", name
    mod = __import__(name)
    print "IMPORTER: mod = ", mod
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
        print "IMPORTER: mod = ", mod
    return mod
    
