import sys
import unittest

def additional_tests():
    if sys.version_info < (2, 7) and 'nosetests' not in sys.argv:
        print((
                "ERROR: not compatible Python version: %s" % sys.version.split()[0]), file=sys.stderr)
        print((
                "This tests uses class level fixtures that is not supported\n"
                "by unittest on Python prior version 2.7.\n"
                "To run tests on Python < 2.7 use the nose extension\n"
                "<http://pypi.python.org/pypi/nose/>\n"
                "\n"
                "  $ easy_install nose\n"
                "  $ python setup.py nosetests\n"
                ), file=sys.stderr)
        sys.exit(1)
    return unittest.TestSuite()
