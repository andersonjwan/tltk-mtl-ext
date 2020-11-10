import tltk_mtl as MTL
import antlr4

from STQLLexer import STQLLexer as Lexer
from STQLParser import STQLParser as Parser
from STQLVisitor import STQLVisitor as Visitor

# parse_mtl is used to translate a string MTL formula
# into an MTL representation using the TLTk Python module developed
# by Nogthar_ and Bardh Hoxha.
#
# @param formula:    A string representing the formula to be parsed. It
#                    should be noted that predicate names should correspond
#                    to the names in the predicates parameter.
#
# @param predicates: A dictionary of MTL.Predicate()'s.
#
# @param mode:       The specified computation mode to be used for MTL. The
#                    default mode is 'cpu_threaded'

def parse_mtl(formula, predicates, mode='cpu_threaded'):
    # convert string to ANTLRv4 InputStream
    inputstream = antlr4.InputStream(formula)

    # create a token stream from the STQL lexer
    lexer = Lexer(inputstream)
    stream = antlr4.CommonTokenStream(lexer)

    # return a ParseTree from the STQL parser
    parser = Parser(stream)
    tree = parser.stqlSpecification()

    # visit the tree and generate equivalent MTL from formula
    visitor = Visitor(lexer, predicates, mode)
    return visitor.visit(tree)
