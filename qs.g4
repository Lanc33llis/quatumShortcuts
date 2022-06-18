grammar qs;

parse
    : expression EOF
    ;

expression
    : function
    | expression MULTDIV expression
    | expression ADDSUB expression
    | expression KEYWORD expression
    | '(' expression ')'
    | unit
    | TEXT
    | ID
    ;

unit
    : NUMBER ID
    | NUMBER
    ;

function
    : ID '(' arguments? ')'
    ;

arguments
    : expression ( ',' expression )*
    ;

KEYWORD
    : 'to'
    | '='
    ;

NUMBER       : [-]* ( [0-9]* '.' )? [0-9]+;
ID           : [a-zA-Z_] [a-zA-Z0-9_]*;
TEXT         : '\'' ~[\r\n']* '\'';
MULTDIV      : [*/];
ADDSUB       : [+\-];
SPACE        : [ \t\r\n]+ -> skip;
