import tltk_mtl as MTL
import tltk_mtl_ext as MTLE
import antlr4

from STQLLexer import STQLLexer as Lexer
from STQLParser import STQLParser as Parser
from STQLVisitor import STQLVisitor as Visitor

def testOrRule():
	preds = {}
	preds['pred1'] = MTL.Predicate('pred1', 1, 2)
	preds['pred2'] = MTL.Predicate('pred2', 2, 4)
	preds['pred3'] = MTL.Predicate('pred3', 4, 8)
	
	assert isinstance(MTLE.parse_mtl('pred1 || pred1', preds), MTL.Or), printFail(1)
	printPass(1)
	assert isinstance(MTLE.parse_mtl('pred1 | pred1 || pred1 or pred1', preds), MTL.Or), printFail(2)
	printPass(2)
	assert isinstance(MTLE.parse_mtl('pred1 or !pred2 || pred3', preds), MTL.Or), printFail(3)
	printPass(3)
	assert isinstance(MTLE.parse_mtl('pred1 and pred2 or pred3', preds), MTL.Or), printFail(4)
	printPass(4)
	assert isinstance(MTLE.parse_mtl('pred2 and pred3 & pred2 and pred2 or pred1', preds), MTL.Or), printFail(5)
	printPass(5)

def printPass(test_num):
    print('[Or Rule Test] Assertion No. %02d PASSED.' % (test_num))

def printFail(test_num):
    return '[Or Rule Test] Assertion No. %02d FAILED' % (test_num)

testOrRule()
