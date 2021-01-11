# Generated from ConvexPolygon.g by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ConvexPolygonParser import ConvexPolygonParser
else:
    from ConvexPolygonParser import ConvexPolygonParser

# This class defines a complete generic visitor for a parse tree produced by ConvexPolygonParser.

class ConvexPolygonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ConvexPolygonParser#root.
    def visitRoot(self, ctx:ConvexPolygonParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConvexPolygonParser#point.
    def visitPoint(self, ctx:ConvexPolygonParser.PointContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConvexPolygonParser#convex_polygon.
    def visitConvex_polygon(self, ctx:ConvexPolygonParser.Convex_polygonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConvexPolygonParser#assignment.
    def visitAssignment(self, ctx:ConvexPolygonParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConvexPolygonParser#color.
    def visitColor(self, ctx:ConvexPolygonParser.ColorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConvexPolygonParser#my_print.
    def visitMy_print(self, ctx:ConvexPolygonParser.My_printContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConvexPolygonParser#area.
    def visitArea(self, ctx:ConvexPolygonParser.AreaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConvexPolygonParser#perimeter.
    def visitPerimeter(self, ctx:ConvexPolygonParser.PerimeterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConvexPolygonParser#vertices.
    def visitVertices(self, ctx:ConvexPolygonParser.VerticesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConvexPolygonParser#centroid.
    def visitCentroid(self, ctx:ConvexPolygonParser.CentroidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConvexPolygonParser#inside.
    def visitInside(self, ctx:ConvexPolygonParser.InsideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConvexPolygonParser#equal.
    def visitEqual(self, ctx:ConvexPolygonParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConvexPolygonParser#draw.
    def visitDraw(self, ctx:ConvexPolygonParser.DrawContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConvexPolygonParser#operator.
    def visitOperator(self, ctx:ConvexPolygonParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConvexPolygonParser#rgb.
    def visitRgb(self, ctx:ConvexPolygonParser.RgbContext):
        return self.visitChildren(ctx)



del ConvexPolygonParser