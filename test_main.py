import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_function(self) :
        for i in range(20) :
            val = np.random.randint(1,9999)
            nthou = int( np.floor( val / 1000) )
            self.assertTrue( nthou==numberOfThousands(val), "Your function for determining the number of thousands is not working" )
