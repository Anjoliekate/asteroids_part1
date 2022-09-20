"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
Do Not Move on to the next function until its tests report 'ok' or your code
may not work as expected.
"""

import unittest

def suite( ):
    test_modules = [
        "test_001_movable_001_constructor_and_getters",
        "test_001_movable_002_move",
        "test_001_movable_003_abstract",
    ]

    s = unittest.TestSuite( )
    for m in test_modules:
        s.addTest( __import__(m ).suite( ) )

    return s

runner = unittest.TextTestRunner( )
runner.run( suite( ) )
