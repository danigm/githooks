#!/usr/bin/python

import sys
import re
import subprocess

modified = re.compile('^(?:M|A)..(?P<name>.*\.py)')


def main():
    p = subprocess.Popen(['git', 'status', '--porcelain'],
                         stdout=subprocess.PIPE)
    out, err = p.communicate()
    modifieds = modified.findall(out)

    rrcode = 0
    for file in modifieds:
        p = subprocess.Popen(['pep8', file],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out or err:
            sys.stdout.write(" * pep8:\n%s\n%s" % (out, err))
            rrcode = rrcode | 1
        retcode = subprocess.call(['pyflakes', file])
        rrcode = retcode | rrcode

    sys.exit(rrcode)

if __name__ == '__main__':
    main()
