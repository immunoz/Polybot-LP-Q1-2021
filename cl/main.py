from antlr4 import *

from ConvexPolygonLexer import ConvexPolygonLexer
from PolygonTreeVisitor import PolygonTreeVisitor
from ConvexPolygonParser import ConvexPolygonParser


def get_expression_tree(in_val, visitor):
    parsed_input = InputStream(in_val)
    lexer = ConvexPolygonLexer(parsed_input)
    token_stream = CommonTokenStream(lexer)
    parser = ConvexPolygonParser(token_stream)
    return visitor.visit(parser.root())


# main function to test the grammar created
def main():
    running = True
    visitor = PolygonTreeVisitor()
    while running:
        input_stream = InputStream(input('Introduce a command: '))
        if str(input_stream) != "quit":
            lexer = ConvexPolygonLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = ConvexPolygonParser(token_stream)
            tree = parser.root()
            visitor.visit(tree)
        else:
            running = False
            print("Bye Bye :)")

# uncomment this line of code in order to test the grammar from the console
# main()
