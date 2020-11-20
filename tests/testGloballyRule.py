import tltk_mtl as MTL
import tltk_mtl_ext as MTLE

def testGloballyRule():
	preds = {}
	preds['pred1'] = MTL.Predicate('pred1', 1, 2)
	preds['pred2'] = MTL.Predicate('pred2', 2, 4)
	preds['pred3'] = MTL.Predicate('pred3', 4, 8)
	
	assert isinstance(MTLE.parse_mtl('[]_ts:(1, inf) pred1', preds), MTL.Global), printFail(1)
	printPass(1)
	assert isinstance(MTLE.parse_mtl('[]_ts:(1, 100) G_ts:(1, 100) (pred1 && pred2)', preds), MTL.Global), printFail(2)
	printPass(2)
	assert isinstance(MTLE.parse_mtl('[]_ts:(1, 100) []_ts:(5, 50) G_ts:(25, 35) []_ts:(27, 30) pred1', preds), MTL.Global), printFail(3)
	printPass(3)
	assert isinstance(MTLE.parse_mtl('G_ts:(1, 1000) (pred1 && pred2)', preds), MTL.Global), printFail(4)
	printPass(4)
	assert isinstance(MTLE.parse_mtl('[]_ts:(25, 3000) (pred2 | pred3)', preds), MTL.Global), printFail(5)
	printPass(5)

def printPass(test_num):
    print('[Globally Rule Test] Assertion No. %02d PASSED.' % (test_num))

def printFail(test_num):
    return '[Globally Rule Test] Assertion No. %02d FAILED' % (test_num)

testGloballyRule()
