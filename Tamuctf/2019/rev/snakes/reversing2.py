# uncompyle6 version 3.2.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15rc1 (default, Nov 12 2018, 14:31:15)
# [GCC 7.3.0]
# Embedded file name: reversing2.py
# Compiled at: 2018-10-07 19:28:58
from datetime import datetime
Fqaa = [102, 108, 97, 103, 123, 100, 101, 99, 111, 109, 112, 105, 108, 101, 125]
XidT = [83, 117, 112, 101, 114, 83, 101, 99, 114, 101, 116, 75, 101, 121]

def main():
    print 'Clock.exe'
    input = raw_input('>: ').strip()
    kUIl = ''
    for i in XidT:
        kUIl += chr(i)

    if input == kUIl:
        alYe = ''
        for i in Fqaa:
            alYe += chr(i)

        print alYe
    else:
        print datetime.now()


if __name__ == '__main__':
    kUIl = ''
    for i in XidT:
        kUIl += chr(i)

    print (kUIl)

    alYe = ''
    for i in Fqaa:
        alYe += chr(i)

    print (alYe)

# okay decompiling reversing2.pyc
# flag{decompile}
