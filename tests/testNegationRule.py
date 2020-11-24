import tltk_mtl as MTL
import tltk_mtl_ext as MTLE

def testNegationRule():
	preds = {}
	preds['pred1'] = MTL.Predicate('pred1', 1, 2)
	preds['pred2'] = MTL.Predicate('pred2', 2, 4)
	preds['pred3'] = MTL.Predicate('pred3', 4, 8)
	
	assert isinstance(MTLE.parse_mtl('!pred1', preds), MTL.Not), printFail(1)
	printPass(1)
	assert isinstance(MTLE.parse_mtl('!!(pred2)', preds), MTL.Not), printFail(2)
	printPass(2)
	assert isinstance(MTLE.parse_mtl('!pred3', preds), MTL.Not), printFail(3)
	printPass(3)
	assert isinstance(MTLE.parse_mtl('!(pred1 and pred2)', preds), MTL.Not), printFail(4)
	printPass(4)
	assert isinstance(MTLE.parse_mtl('!!!!!(pred1 and pred2 and pred3)', preds), MTL.Not), printFail(5)
	printPass(5)

def printPass(test_num):
    print("%-20s Assertion No. %02d PASSED." % ('[Negation Rule Test]', test_num))

def printFail(test_num):
    return '%-20s Assertion No. %02d FAILED' % ('[Negation Rule Test]', test_num)

testNegationRule()
