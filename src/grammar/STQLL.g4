/**
 * Spatio-Temporal Quality Logic Lexer (STQLL).
 */

lexer grammar STQLL;

WS
    : [ \t\r\n]+ -> skip ;

SET
    : ('EMPTYSET' | 'UNIVERSE') ;

LPAREN
    : '(' ;

RPAREN
    : ')' ;

LBRACK
    : '[' ;

RBRACK
    : ']' ;

AT
    : '@' ;

COMMA
    : ',' ;

UNDERSCORE
    : '_' ;

NEGATION
    : ('~' | '!' | 'not') ;

MINUS
    : '-' ;

RELOP
    : ('<' | '>' | '<=' | '>=') ;

EQUALITYOP
    : ('==' | '!=') ;

NEXTOP
    : ('next' | 'X') ('_')? (TIME_RNGE | FRAME_RNGE)? ;

FUTUREOP
    : ('finally' | 'eventually' | 'F' | '<>') ('_')? (TIME_RNGE | FRAME_RNGE)? ;

GLOBALLYOP
    : ('globally' | 'always' | 'G' | '[]')+ ('_')? (TIME_RNGE | FRAME_RNGE)? ;

UNTILOP
    : ('until' | 'U') ('_')? (TIME_RNGE | FRAME_RNGE)? ;

RELEASEOP
    : ('release' | 'R') ('_')? (TIME_RNGE | FRAME_RNGE)? ;

UNTILNSOP
    : ('untilns' | 'Uns') ('_')? (TIME_RNGE | FRAME_RNGE)? ;

RELEASENSOP
    : ('releasens' | 'Rns') ('_')? (TIME_RNGE | FRAME_RNGE)? ;

ANDOP
    : ('and' | '/\\' | '&&' | '&') ;

OROP
    : ('or' | '\\/' | '||' | '|') ;

QUANTIFIEROP
    : (ExistsOp | ForAllOp) ;

fragment ExistsOp
    : ('EXISTS' | 'E') ;

fragment ForAllOp
    : ('FORALL' | 'A') ;

SPQUANTIFIEROP
    : ('is_nonempty' | 'is_universe') ;

PROPOP
    : (IMPLIESOP | EQUIVOP) ;

IMPLIESOP
    : ('implies' | '->') ;

EQUIVOP
    : ('iff' | '<->') ;

SPACEOP
    : ('I' | 'C') ;

// Constants
CONST_TIME
    : 'C_TIME' ;

CONST_FRAME
    : 'C_FRAME' ;

CRT
    : ('LM' | 'RM' | 'TM' | 'BM' | 'CT') ;

// Literals
BOOLEAN
    : (TRUE | FALSE) ;

fragment TRUE
    : ('TRUE' | 'true') ;

fragment FALSE
    : ('FALSE' | 'false') ;

INF
    : 'inf' ;

REAL
    : (Digits '.' Digits) ;

INT
    : (Digits) ;

fragment Digits
    : [0-9]+ ;

// Variables
VAR
    : PREFIX LETTER (LETTER | [0-9] | '_')* ;

fragment PREFIX
    : 'Var_' ;

fragment LETTER
    : [a-zA-Z]+ ;

fragment TIME_RNGE
    : 'ts:' ;

fragment FRAME_RNGE
    : 'fr:' ;

PREDICATE
    : [a-z]+ ([a-zA-Z] | [0-9] | '_')* ;
