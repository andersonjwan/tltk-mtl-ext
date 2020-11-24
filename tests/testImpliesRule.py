import tltk_mtl as MTL
import tltk_mtl_ext as MTLE

def testImpliesRule():
	preds = {}
	preds['pred1'] = MTL.Predicate('pred1', 1, 2)
	preds['pred2'] = MTL.Predicate('pred2', 2, 4)
	preds['pred3'] = MTL.Predicate('pred3', 4, 8)
	
	assert isinstance(MTLE.parse_mtl('pred1 -> pred1', preds), MTL.Or), printFail(1)
	printPass(1)
	assert isinstance(MTLE.parse_mtl('(pred1 && pred2) -> TRUE', preds), MTL.Or), printFail(2)
	printPass(2)
	assert isinstance(MTLE.parse_mtl('pred1 -> pred2 -> pred3', preds), MTL.Or), printFail(3)
	printPass(3)
	assert isinstance(MTLE.parse_mtl('pred1 -> (pred1 && pred2 && pred3)', preds), MTL.Or), printFail(4)
	printPass(4)
	assert isinstance(MTLE.parse_mtl('pred1 -> pred2 -> (pred1 || pred2) -> TRUE', preds), MTL.Or), printFail(5)
	printPass(5)

def printPass(test_num):
    print("%-20s Assertion No. %02d PASSED." % ('[Implies Rule Test]', test_num))

def printFail(test_num):
    return '%-20s Assertion No. %02d FAILED' % ('[Implies Rule Test]', test_num)

testImpliesRule()
