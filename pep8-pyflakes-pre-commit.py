#!/usr/bin/python

import sys
import re
import subprocess

modified = re.compile('modified:\s+(?P<name>.*\.py)')
new = re.compile('new file:\s+(?P<name>.*\.py)')

def main():
    p = subprocess.Popen(['git', 'status'], stdout=subprocess.PIPE)
    out, err = p.communicate()
    modifieds = modified.findall(out)
    news = new.findall(out)

    modifieds += news

    rrcode = 0
    for file in set(modifieds):
        retcode = subprocess.call(['pep8', file])
        retcode = subprocess.call(['pyflakes', file])
        rrcode = retcode | rrcode

    sys.exit(rrcode)

if __name__ == '__main__':
    main()
