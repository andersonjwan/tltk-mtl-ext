import tltk_mtl as MTL
import tltk_mtl_ext as MTLE

def testNextRule():
	preds = {}
	preds['pred1'] = MTL.Predicate('pred1', 1, 2)
	preds['pred2'] = MTL.Predicate('pred2', 2, 4)
	preds['pred3'] = MTL.Predicate('pred3', 4, 8)
	
	assert isinstance(MTLE.parse_mtl('next pred1', preds), MTL.Next), printFail(1)
	printPass(1)
	assert isinstance(MTLE.parse_mtl('next X pred1', preds), MTL.Next), printFail(2)
	printPass(2)
	assert isinstance(MTLE.parse_mtl('next (pred1 && pred2)', preds), MTL.Next), printFail(3)
	printPass(3)
	assert isinstance(MTLE.parse_mtl('X (pred1 && X X X pred3)', preds), MTL.Next), printFail(4)
	printPass(4)
	assert isinstance(MTLE.parse_mtl('X X X X X X X X (pred1 & pred2)', preds), MTL.Next), printFail(5)
	printPass(5)

def printPass(test_num):
    print('[Next Rule Test] Assertion No. %02d PASSED.' % (test_num))

def printFail(test_num):
    return '[Next Rule Test] Assertion No. %02d FAILED' % (test_num)

testNextRule()
