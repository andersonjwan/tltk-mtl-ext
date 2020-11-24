/**
 * Spatio-Temporal Quality Logic Grammar (STQL).
 */

grammar STQL;
import STQLL;

stqlSpecification
    : phi EOF;

phi
    : LPAREN phi RPAREN                        #parenPhiExpr
    
    | BOOLEAN                                  #boolAtom
    | NEGATION phi                             #opNegExpr
    
    | NEXTOP          (interval)? phi          #opNextExpr
    | FUTUREOP        (interval)? phi          #opFutureExpr
    | GLOBALLYOP      (interval)? phi          #opGloballyExpr
    
    | phi UNTILOP     (interval)? phi          #opUntilExpr
    | phi RELEASEOP   (interval)? phi          #opReleaseExpr
    | phi UNTILNSOP   (interval)? phi          #opUntilNotStrictExpr
    | phi RELEASENSOP (interval)? phi          #opReleaseNotStrictExpr
    
    | phi (ANDOP | OROP) phi                   #opLogicalExpr
    | phi PROPOP phi                           #opPropExpr
    
    | CONST_TIME  MINUS VAR RELOP (REAL | INT) #timeConstraintExpr
    | CONST_FRAME MINUS VAR RELOP INT          #frameConstraintExpr
    
    | VAR EQUALITYOP VAR                       #variableEquivalenceExpr
    
    | freezeTime phi                           #opFreezeTimeExpr
    
    | SPQUANTIFIEROP tau                       #tauExpr
    | pi                                       #piExpr
    | theta                                    #thetaExpr
    
    | PREDICATE                                #predicateExpr
;

tau
    : LPAREN tau RPAREN                        #parenTauExpr
    
    | SET                                      #setTauExpr
    | funcBB                                   #funcBoundingBoxTauExpr
    
    | NEGATION tau                             #opNegationTauExpr
    | tau (ANDOP | OROP) tau                   #opLogicalTauExpr
    | SPACEOP tau                              #opSpaceTauExpr
    
    | NEXTOP          (interval)? tau          #opNextTauExpr
    | FUTUREOP        (interval)? tau          #opFutureTauExpr
    | GLOBALLYOP      (interval)? tau          #opGloballyTauExpr
    
    | phi UNTILOP     (interval)? tau          #opUntilTauExpr
    | phi RELEASEOP   (interval)? tau          #opReleaseTauExpr
    | phi UNTILNSOP   (interval)? tau          #opUntilNotStrictTauExpr
    | phi RELEASENSOP (interval)? tau          #opReleaseNotStrictTauExpr
;

pi
    : LPAREN pi RPAREN                         #parenPiExpr
    | funcAreaTau      RELOP REAL              #funcAreaTauExpr
    | funcRatioAreaTau RELOP REAL              #funcRatioAreaTauExpr
;

theta
    : LPAREN theta RPAREN                      #parenThetaExpr
    
    | funcDist    RELOP REAL                   #funcEuclideanDistancExpr
    | funcLatDist RELOP REAL                   #funcLatituteExpr
    | funcLonDist RELOP REAL                   #funcLongitudeExpr
    
    | funcRatioLatLon RELOP REAL               #funcRatioLatLonExpr
    
    | funcAreaTheta RELOP REAL                 #funcAreaThetaExpr
    | funcRatioArea RELOP REAL                 #funcRatioAreaThetaExpr
    
    | funcClass RELOP INT                      #funcClassExpr
    | funcClass EQUALITYOP funcClass           #funcCompareClassExpr
    
    | funcProb      RELOP REAL                 #funcProbExpr
    | funcRatioProb RELOP REAL                 #funcRatioProbExpr
;

freezeTime
    : AT LPAREN (timeVarDecl | objVarDecl | timeVarDecl COMMA objVarDecl) RPAREN
;

timeVarDecl
    : (VAR | UNDERSCORE) ;

objVarDecl
    : QUANTIFIEROP COMMA varList;

varList
    : (VAR | VAR COMMA varList) ;

interval
    : (LPAREN | LBRACK) (INT | REAL | INF) COMMA (INT | REAL | INF) (RPAREN | RBRACK)
;

funcBB
    : 'BB' LPAREN VAR RPAREN ;

funcAreaTau
    : 'area' LPAREN tau RPAREN ;

funcRatioAreaTau
    : 'ratio' LPAREN funcAreaTau COMMA funcAreaTau RPAREN ;

funcDist
    : 'dist' LPAREN VAR COMMA CRT COMMA VAR COMMA CRT RPAREN ;

funcLatDist
    : 'lat_dist' LPAREN VAR COMMA CRT RPAREN ;

funcLonDist
    : 'lon_dist' LPAREN VAR COMMA CRT RPAREN ;

funcRatioLatLon
    : 'ratio' LPAREN (funcLatDist | funcLonDist) COMMA (funcLatDist | funcLonDist) RPAREN ;

funcAreaTheta
    : 'area' LPAREN VAR RPAREN ;

funcRatioArea
    : 'ratio' LPAREN funcAreaTau COMMA funcAreaTau RPAREN ;

funcClass
    : 'class' LPAREN VAR RPAREN ;

funcProb
    : 'prob' LPAREN VAR RPAREN ;

funcRatioProb
    : 'ratio' LPAREN funcProb COMMA funcProb RPAREN ;
