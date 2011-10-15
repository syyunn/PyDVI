#####################################################################################################
#
# PyDVI - Python Library to Process DVI Stream
# Copyright (C) 2009 Salvaire Fabrice
#
#####################################################################################################

#####################################################################################################

import unittest

#####################################################################################################

from PyDVI.EnumFactory import *

#####################################################################################################

class TestEnumFactory(unittest.TestCase):

    def test(self):

        enum1 = EnumFactory('Enum1', ('cst1', 'cst2'))
        
        self.assertEqual(enum1.cst1, 0)
        self.assertEqual(enum1.cst2, 1)
        self.assertEqual(len(enum1), 2)
        
        enum2 = ExplicitEnumFactory('Enum2', {'cst1':1, 'cst2':3})
 
        self.assertEqual(enum2.cst1, 1)
        self.assertEqual(enum2.cst2, 3)

        self.assertTrue(enum2.cst2 in enum2)

#####################################################################################################

if __name__ == '__main__':

    unittest.main()

#####################################################################################################
#
# End
#
#####################################################################################################