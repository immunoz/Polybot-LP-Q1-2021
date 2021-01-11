from antlr4 import *

from ConvexPolygonLexer import ConvexPolygonLexer
from ConvexPolygonParser import ConvexPolygonParser


def get_expression_tree(in_val, visitor):
    parsed_input = InputStream(in_val)
    lexer = ConvexPolygonLexer(parsed_input)
    token_stream = CommonTokenStream(lexer)
    parser = ConvexPolygonParser(token_stream)
    return visitor.visit(parser.root())