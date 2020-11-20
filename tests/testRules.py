import tltk_mtl as MTL
import tltk_mtl_ext as MTLE

from testNegationRule import *

from testAndRule import *
from testOrRule  import *

from testNextRule import *
from testFinallyRule import *
from testGloballyRule import *

from testImpliesRule import *

def testRules():
    testNegationRule()
    
    testAndRule()
    testOrRule()
    
    testNextRule()
    testFinallyRule()
    testGloballyRule()
    
    testImpliesRule()

testRules
