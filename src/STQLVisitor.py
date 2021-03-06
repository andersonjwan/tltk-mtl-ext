# Generated from STQL.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .STQLParser import STQLParser
else:
    from STQLParser import STQLParser

import tltk_mtl as MTL

class STQLVisitor(ParseTreeVisitor):
    def __init__(self, lexer, predicates, mode):
        self.lexer = lexer           # STQL lexer
        self.predicates = predicates # dictionary of MTL predicates
        self.mode = mode             # MTL computation mode (default: 'cpu_threaded')

    # Visit a parse tree produced by STQLParser#stqlSpecification.
    def visitStqlSpecification(self, ctx:STQLParser.StqlSpecificationContext):
        return self.visit(ctx.getRuleContext().getChild(0))


    # Visit a parse tree produced by STQLParser#opReleaseNotStrictExpr.
    def visitOpReleaseNotStrictExpr(self, ctx:STQLParser.OpReleaseNotStrictExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#opUntilExpr.
    def visitOpUntilExpr(self, ctx:STQLParser.OpUntilExprContext):
        pred1 = self.visit(ctx.getRuleContext().getChild(0))
        pred2 = self.visit(ctx.getRuleContext().getChild(3))

        bounds = self.visit(ctx.getRuleContext().getChild(2))

        return MTL.Until(bounds[0], bounds[1], pred1, pred2, self.mode)


    # Visit a parse tree produced by STQLParser#timeConstraintExpr.
    def visitTimeConstraintExpr(self, ctx:STQLParser.TimeConstraintExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#piExpr.
    def visitPiExpr(self, ctx:STQLParser.PiExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#opNextExpr.
    def visitOpNextExpr(self, ctx:STQLParser.OpNextExprContext):
        pred = self.visit(ctx.getRuleContext().getChild(1))

        return MTL.Next(pred)


    # Visit a parse tree produced by STQLParser#variableEquivalenceExpr.
    def visitVariableEquivalenceExpr(self, ctx:STQLParser.VariableEquivalenceExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#opUntilNotStrictExpr.
    def visitOpUntilNotStrictExpr(self, ctx:STQLParser.OpUntilNotStrictExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#thetaExpr.
    def visitThetaExpr(self, ctx:STQLParser.ThetaExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#predicateExpr.
    def visitPredicateExpr(self, ctx:STQLParser.PredicateExprContext):
        return self.predicates[ctx.getRuleContext().getText()]


    # Visit a parse tree produced by STQLParser#opFutureExpr.
    def visitOpFutureExpr(self, ctx:STQLParser.OpFutureExprContext):
        pred = self.visit(ctx.getRuleContext().getChild(2))
        bounds = self.visit(ctx.getRuleContext().getChild(1))

        return MTL.Finally(bounds[0], bounds[1], pred, self.mode)


    # Visit a parse tree produced by STQLParser#parenPhiExpr.
    def visitParenPhiExpr(self, ctx:STQLParser.ParenPhiExprContext):
        return self.visit(ctx.getRuleContext().getChild(1))


    # Visit a parse tree produced by STQLParser#frameConstraintExpr.
    def visitFrameConstraintExpr(self, ctx:STQLParser.FrameConstraintExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#opGloballyExpr.
    def visitOpGloballyExpr(self, ctx:STQLParser.OpGloballyExprContext):
        pred = self.visit(ctx.getRuleContext().getChild(2))
        bounds = self.visit(ctx.getRuleContext().getChild(1))

        return MTL.Global(bounds[0], bounds[1], pred, self.mode)


    # Visit a parse tree produced by STQLParser#opLogicalExpr.
    def visitOpLogicalExpr(self, ctx:STQLParser.OpLogicalExprContext):
        pred1 = self.visit(ctx.getRuleContext().getChild(0))
        pred2 = self.visit(ctx.getRuleContext().getChild(2))

        type = ctx.getRuleContext().getChild(1).getSymbol().type

        if type == self.lexer.ANDOP:
            return MTL.And(pred1, pred2, self.mode)
        elif type == self.lexer.OROP:
            return MTL.Or(pred1, pred2, self.mode)
        else:
            return None


    # Visit a parse tree produced by STQLParser#opFreezeTimeExpr.
    def visitOpFreezeTimeExpr(self, ctx:STQLParser.OpFreezeTimeExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#tauExpr.
    def visitTauExpr(self, ctx:STQLParser.TauExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#boolAtom.
    def visitBoolAtom(self, ctx:STQLParser.BoolAtomContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#opReleaseExpr.
    def visitOpReleaseExpr(self, ctx:STQLParser.OpReleaseExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#opPropExpr.
    def visitOpPropExpr(self, ctx:STQLParser.OpPropExprContext):
        pred1 = self.visit(ctx.getRuleContext().getChild(0))
        pred2 = self.visit(ctx.getRuleContext().getChild(2))
        
        return MTL.Or(MTL.Not(pred1), pred2, self.mode)


    # Visit a parse tree produced by STQLParser#opNegExpr.
    def visitOpNegExpr(self, ctx:STQLParser.OpNegExprContext):
        pred = self.visit(ctx.getRuleContext().getChild(1))

        return MTL.Not(pred, self.mode)


    # Visit a parse tree produced by STQLParser#funcBoundingBoxTauExpr.
    def visitFuncBoundingBoxTauExpr(self, ctx:STQLParser.FuncBoundingBoxTauExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#opGloballyTauExpr.
    def visitOpGloballyTauExpr(self, ctx:STQLParser.OpGloballyTauExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#opReleaseTauExpr.
    def visitOpReleaseTauExpr(self, ctx:STQLParser.OpReleaseTauExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#parenTauExpr.
    def visitParenTauExpr(self, ctx:STQLParser.ParenTauExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#opUntilNotStrictTauExpr.
    def visitOpUntilNotStrictTauExpr(self, ctx:STQLParser.OpUntilNotStrictTauExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#opFutureTauExpr.
    def visitOpFutureTauExpr(self, ctx:STQLParser.OpFutureTauExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#opReleaseNotStrictTauExpr.
    def visitOpReleaseNotStrictTauExpr(self, ctx:STQLParser.OpReleaseNotStrictTauExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#opSpaceTauExpr.
    def visitOpSpaceTauExpr(self, ctx:STQLParser.OpSpaceTauExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#setTauExpr.
    def visitSetTauExpr(self, ctx:STQLParser.SetTauExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#opLogicalTauExpr.
    def visitOpLogicalTauExpr(self, ctx:STQLParser.OpLogicalTauExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#opNextTauExpr.
    def visitOpNextTauExpr(self, ctx:STQLParser.OpNextTauExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#opUntilTauExpr.
    def visitOpUntilTauExpr(self, ctx:STQLParser.OpUntilTauExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#opNegationTauExpr.
    def visitOpNegationTauExpr(self, ctx:STQLParser.OpNegationTauExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#parenPiExpr.
    def visitParenPiExpr(self, ctx:STQLParser.ParenPiExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#funcAreaTauExpr.
    def visitFuncAreaTauExpr(self, ctx:STQLParser.FuncAreaTauExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#funcRatioAreaTauExpr.
    def visitFuncRatioAreaTauExpr(self, ctx:STQLParser.FuncRatioAreaTauExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#parenThetaExpr.
    def visitParenThetaExpr(self, ctx:STQLParser.ParenThetaExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#funcEuclideanDistancExpr.
    def visitFuncEuclideanDistancExpr(self, ctx:STQLParser.FuncEuclideanDistancExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#funcLatituteExpr.
    def visitFuncLatituteExpr(self, ctx:STQLParser.FuncLatituteExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#funcLongitudeExpr.
    def visitFuncLongitudeExpr(self, ctx:STQLParser.FuncLongitudeExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#funcRatioLatLonExpr.
    def visitFuncRatioLatLonExpr(self, ctx:STQLParser.FuncRatioLatLonExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#funcAreaThetaExpr.
    def visitFuncAreaThetaExpr(self, ctx:STQLParser.FuncAreaThetaExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#funcRatioAreaThetaExpr.
    def visitFuncRatioAreaThetaExpr(self, ctx:STQLParser.FuncRatioAreaThetaExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#funcClassExpr.
    def visitFuncClassExpr(self, ctx:STQLParser.FuncClassExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#funcCompareClassExpr.
    def visitFuncCompareClassExpr(self, ctx:STQLParser.FuncCompareClassExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#funcProbExpr.
    def visitFuncProbExpr(self, ctx:STQLParser.FuncProbExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#funcRatioProbExpr.
    def visitFuncRatioProbExpr(self, ctx:STQLParser.FuncRatioProbExprContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#freezeTime.
    def visitFreezeTime(self, ctx:STQLParser.FreezeTimeContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#timeVarDecl.
    def visitTimeVarDecl(self, ctx:STQLParser.TimeVarDeclContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#objVarDecl.
    def visitObjVarDecl(self, ctx:STQLParser.ObjVarDeclContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#varList.
    def visitVarList(self, ctx:STQLParser.VarListContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#interval.
    def visitInterval(self, ctx:STQLParser.IntervalContext):
        bounds = []
        bounds.append(float(ctx.getRuleContext().getChild(1).getText()))
        bounds.append(float(ctx.getRuleContext().getChild(3).getText()))

        return bounds


    # Visit a parse tree produced by STQLParser#funcBB.
    def visitFuncBB(self, ctx:STQLParser.FuncBBContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#funcAreaTau.
    def visitFuncAreaTau(self, ctx:STQLParser.FuncAreaTauContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#funcRatioAreaTau.
    def visitFuncRatioAreaTau(self, ctx:STQLParser.FuncRatioAreaTauContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#funcDist.
    def visitFuncDist(self, ctx:STQLParser.FuncDistContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#funcLatDist.
    def visitFuncLatDist(self, ctx:STQLParser.FuncLatDistContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#funcLonDist.
    def visitFuncLonDist(self, ctx:STQLParser.FuncLonDistContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#funcRatioLatLon.
    def visitFuncRatioLatLon(self, ctx:STQLParser.FuncRatioLatLonContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#funcAreaTheta.
    def visitFuncAreaTheta(self, ctx:STQLParser.FuncAreaThetaContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#funcRatioArea.
    def visitFuncRatioArea(self, ctx:STQLParser.FuncRatioAreaContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#funcClass.
    def visitFuncClass(self, ctx:STQLParser.FuncClassContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#funcProb.
    def visitFuncProb(self, ctx:STQLParser.FuncProbContext):
        return NotImplemented


    # Visit a parse tree produced by STQLParser#funcRatioProb.
    def visitFuncRatioProb(self, ctx:STQLParser.FuncRatioProbContext):
        return NotImplemented



del STQLParser
