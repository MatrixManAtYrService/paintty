import textwrap
import argparse
from collections import namedtuple

def parse_setup():
    parser = argparse.ArgumentParser(description=textwrap.dedent(
        '''
        foo
        ''')[1:-1])
    parser.add_argument('--local', action='store_true')
    return parser.parse_args()


def setup():
    args = parse_setup()
    print(args.local)


def parse_unsetup():
    parser = argparse.ArgumentParser(description=textwrap.dedent(
        '''
        bar
    return EnvActions('bar')
        ''')[1:-1])
    parser.add_argument('--local', action='store_true')
    return parser.parse_args()

def unsetup():
    args = parse_unsetup()
    print(args.local)
