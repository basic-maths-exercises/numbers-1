import AssCheck.funcchecks as fc
import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_function(self) :
        inputs, outputs = np.zeros(20), np.zeros(20)
        for i in range(20) :
            inputs[i] = np.random.randint(1,9999)
            outputs[i] = int( np.floor( inputs[i] / 1000) )
        assert( fc.check_func('numberOfThousands', inputs, outputs ) ) 
