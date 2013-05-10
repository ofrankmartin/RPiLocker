#!/usr/bin/python
import sys

from RPiLocker.locker import Locker


def main(args):
    commands = {'open': ['open', 'o', 1, True],
                'close': ['close', 'c', 0, False]}
    locker = Locker()
    
    if args[1] in commands['open']:
        locker.open()
    elif args[1] in commands['close']:
        locker.close()
    elif args[1].isdigit():
        locker.setAbsolutePosition(args[1])
        
    locker.disable()

if __name__ == '__main__':
    main(sys.argv)