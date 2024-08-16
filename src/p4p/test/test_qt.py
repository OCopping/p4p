import unittest

try:
    from qtpy.QtCore import QCoreApplication, QObject
except ImportError:

    class TestDummy(unittest.TestCase):
        def test_asyncio(self):
            raise unittest.SkipTest("Missing qtpy")

else:
    from .qttest import *
