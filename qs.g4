grammar qs;

parse
    : expression EOF
    ;

expression
    : function
    | expression MULTDIV expression
    | expression ADDSUB expression
    | '(' expression ')'
    | unit
    | NUMBER
    | TEXT
    | ID
    ;

unit
    : NUMBER ID
    ;

function
    : ID '(' arguments? ')'
    ;

arguments
    : expression ( ',' expression )*
    ;

NUMBER       : ( [0-9]* '.' )? [0-9]+;
ID           : [a-zA-Z_] [a-zA-Z0-9_]*;
TEXT         : '\'' ~[\r\n']* '\'';
MULTDIV      : [*/];
ADDSUB       : [+\-];
SPACE        : [ \t\r\n]+ -> skip;
