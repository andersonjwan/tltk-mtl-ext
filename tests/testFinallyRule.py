import tltk_mtl as MTL
import tltk_mtl_ext as MTLE

def testFinallyRule():
	preds = {}
	preds['pred1'] = MTL.Predicate('pred1', 1, 2)
	preds['pred2'] = MTL.Predicate('pred2', 2, 4)
	preds['pred3'] = MTL.Predicate('pred3', 4, 8)
	
	assert isinstance(MTLE.parse_mtl('<>_ts:(1, inf) pred1', preds), MTL.Finally), printFail(1)
	printPass(1)
	assert isinstance(MTLE.parse_mtl('<>_ts:(1, 100) (finally_ts:(1.0, 200) (pred1 && pred2))', preds), MTL.Finally), printFail(2)
	printPass(2)
	assert isinstance(MTLE.parse_mtl('<>_ts:(1, 100) <>_ts:(5, 50) F_ts:(25, 35) <>_ts:(27, 30) pred1', preds), MTL.Finally), printFail(3)
	printPass(3)
	assert isinstance(MTLE.parse_mtl('F_ts:(1, 1000) (pred1 && pred2)', preds), MTL.Finally), printFail(4)
	printPass(4)
	assert isinstance(MTLE.parse_mtl('<>_ts:(25, 3000) (pred2 | pred3)', preds), MTL.Finally), printFail(5)
	printPass(5)

def printPass(test_num):
    print("%-20s Assertion No. %02d PASSED." % ('[Finally Rule Test]', test_num))

def printFail(test_num):
    return '%-20s Assertion No. %02d FAILED' % ('[Finally Rule Test]', test_num)

testFinallyRule()
