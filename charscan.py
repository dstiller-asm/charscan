from os import listdir
from os.path import join as joinpath
from os.path import isdir, isfile
from string import printable
from sys import argv, exit

if len(argv) != 2:
    print('Invocation: charscan.py <base path>')
    exit()

basedir = argv[1]

def scan(d):
    contents = listdir(d)

    files = [f for f in contents if isfile(joinpath(d, f))]

    for f in files:
        if f.startswith('.'): continue
        is_printable = True
        for char in f:
            if char not in printable:
                is_printable = False
                break
        if not is_printable:
            print(joinpath(d, f))

    subdirs = [f for f in contents if isdir(joinpath(d, f))]
    for d2 in subdirs: scan(joinpath(d, d2))

scan(basedir)