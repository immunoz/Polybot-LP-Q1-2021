grammar ConvexPolygon;

root : (assignment | color | my_print | area | perimeter | vertices | centroid | inside | equal | draw | operator) EOF;

point: REAL SPACE REAL;

convex_polygon : '[' (point (SPACE SPACE point)+) ']'
              | '[' point ']'
              | '[' ']'
              ;

assignment:
    ID SPACE EQUAL SPACE convex_polygon
    | ID SPACE EQUAL SPACE operator
    ;

color: 'color ' ID COMMA SPACE rgb;
my_print: 'print ' (operator | STRING);
area: 'area ' operator;
perimeter: 'perimeter ' operator;
vertices: 'vertices ' operator;
centroid: 'centroid ' operator;
inside: 'inside ' operator COMMA SPACE operator;
equal: 'equal ' operator COMMA SPACE operator;
draw: 'draw ' '"' FILENAME '"' COMMA SPACE( (operator (COMMA SPACE operator)+) | operator);


operator: '(' operator ')'
    | '#' operator
    | operator ' * ' operator
    | operator ' + ' operator
    | '!' REAL
    | convex_polygon
    | ID
    ;

REAL: [0-9]+ '.'* [0-9]*;
EQUAL: ':=';
ID: [a-zA-Z0-9] [a-zA-Z0-9]*;
COMMA: ',';
SPACE: ' ';
rgb: '{' REAL SPACE REAL SPACE REAL '}';
FILENAME: [a-zA-Z] [a-zA-Z0-9]* '.' [a-z]+;

STRING: '"' CHAR+ '"';
CHAR: [a-z]
    | [A-Z]
    | '-'
    | '_'
    | SPACE
    ;