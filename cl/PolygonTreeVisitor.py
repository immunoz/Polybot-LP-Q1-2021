import random
from decimal import Decimal
from Polygons import ConvexPolygon, boundingBox, drawPolygons

if __name__ is not None and "." in __name__:
    from .ConvexPolygonParser import ConvexPolygonParser
    from .ConvexPolygonVisitor import ConvexPolygonVisitor
else:
    from ConvexPolygonParser import ConvexPolygonParser
    from ConvexPolygonVisitor import ConvexPolygonVisitor


class PolygonTreeVisitor(ConvexPolygonVisitor):

    def __init__(self):
        self.variables = {}

    # Visit a parse tree produced by ConvexPolygonParser#Root.
    def visitRoot(self, ctx: ConvexPolygonParser.RootContext):
        n = next(ctx.getChildren())
        return self.visit(n)

    # Visit a parse tree produced by ConvexPolygonParser#Assignment.
    def visitAssignment(self, ctx: ConvexPolygonParser.AssignmentContext):
        components = [n for n in ctx.getChildren()]
        polygon = self.visit(components[4])
        self.variables[components[0].getText()] = polygon
        return polygon

    # Visit a parse tree produced by ConvexPolygonParser#Point.
    def visitPoint(self, ctx: ConvexPolygonParser.PointContext):
        coordinates = [n for n in ctx.getChildren()]
        x = round(Decimal(coordinates[0].getText()), 3)
        y = round(Decimal(coordinates[2].getText()), 3)
        result = (x, y)
        return result

    # Visit a parse tree produced by ConvexPolygonParser#Convex_polygon.
    def visitConvex_polygon(self, ctx: ConvexPolygonParser.Convex_polygonContext):
        components = [n for n in ctx.getChildren()]
        points = []
        for p in components:
            if p.getText() != '[' and p.getText() != ']' and p.getText() != ' ':
                points.append(self.visit(p))
        polygon = ConvexPolygon()
        polygon.constructPolygon(points)
        return polygon

    # Visit a parse tree produced by ConvexPolygonParser#Operator.
    def visitOperator(self, ctx: ConvexPolygonParser.OperatorContext):
        components = [n for n in ctx.getChildren()]
        if len(components) == 1:
            nodeText = components[0].getText()
            if nodeText[0] == '[':
                poly = self.visit(components[0])
                return poly
            elif nodeText in self.variables.keys():
                poly = self.variables[nodeText]
                return poly
            else:
                raise Exception("Error: variable '" + nodeText + "' not exists")
        elif ctx.getChildCount() == 2:
            sign = components[0].getText()
            operator = components[1].getText()
            if sign == '#':
                # case polygon
                if operator[0] == '[' or operator[0] == '(':
                    polygon = self.visit(components[1])
                    bounding = boundingBox([polygon])
                    result = ConvexPolygon()
                    if len(bounding) == 0:
                        return result
                    point_a = (bounding[0][0], bounding[1][1])
                    point_b = (bounding[1][0], bounding[0][1])
                    result.constructPolygon([bounding[0], point_a, bounding[1], point_b])
                    return result
                # case ID
                elif operator in self.variables.keys():
                    polygon = self.variables[components[1].getText()]
                    bounding = boundingBox([polygon])
                    point_a = (bounding[0][0], bounding[1][1])
                    point_b = (bounding[1][0], bounding[0][1])
                    result = ConvexPolygon()
                    result.constructPolygon([bounding[0], point_a, bounding[1], point_b])
                    return result
                # case operator
                else:
                    return self.visit(components[1])
            # '!'
            else:
                num = int(float(components[1].getText()))
                vertices = []
                for i in range(0, num):
                    x = round(Decimal(random.random()), 3)
                    y = round(Decimal(random.random()), 3)
                    vertices.append((x, y))
                result = ConvexPolygon()
                result.constructPolygon(vertices)
                return result
        else:
            sign = components[1].getText()
            left_polygon = self.visit(components[0])
            right_polygon = self.visit(components[2])
            if sign == ' * ':
                return left_polygon.intersection(right_polygon)
            elif sign == ' + ':
                result = left_polygon.union(right_polygon)
                return result
            else:
                result = self.visit(components[1])
                return result

    # Visit a parse tree produced by ConvexPolygonParser#My_print.
    def visitMy_print(self, ctx: ConvexPolygonParser.My_printContext):
        components = [n for n in ctx.getChildren()]
        value = components[1].getText()
        if value[0] == '"':
            print(value[1:len(value) - 1])
            return value[1:len(value) - 1]
        else:
            return self.visit(components[1]).print()

    # Visit a parse tree produced by ConvexPolygonParser#Perimeter.
    def visitPerimeter(self, ctx: ConvexPolygonParser.PerimeterContext):
        components = [n for n in ctx.getChildren()]
        perimeter = self.visit(components[1]).perimeter()
        print(round(perimeter, 3))
        return round(perimeter, 3)

    # Visit a parse tree produced by ConvexPolygonParser#Area.
    def visitArea(self, ctx: ConvexPolygonParser.AreaContext):
        components = [n for n in ctx.getChildren()]
        area = self.visit(components[1]).area()
        print(round(area, 3))
        return round(area, 3)

    # Visit a parse tree produced by ConvexPolygonParser#Vertices.
    def visitVertices(self, ctx: ConvexPolygonParser.VerticesContext):
        components = [n for n in ctx.getChildren()]
        vertices = self.visit(components[1]).numberOfVerticesAndEdges()
        print(vertices)
        return vertices

    # Visit a parse tree produced by ConvexPolygonParser#Centroid.
    def visitCentroid(self, ctx: ConvexPolygonParser.CentroidContext):
        components = [n for n in ctx.getChildren()]
        centroid = self.visit(components[1]).centroid()
        if centroid == ():
            return centroid
        x = centroid[0]
        y = centroid[1]
        print(str(x) + ' ' + str(y))
        return centroid

    # Visit a parse tree produced by ConvexPolygonParser#Inside.
    def visitInside(self, ctx: ConvexPolygonParser.InsideContext):
        components = [n for n in ctx.getChildren()]
        left_polygon = self.visit(components[1])
        right_polygon = self.visit(components[4])
        if right_polygon.checkIfPolygonIsInside(left_polygon):
            print("yes")
            return True
        else:
            print("no")
            return False

    # Visit a parse tree produced by ConvexPolygonParser#Equal.
    def visitEqual(self, ctx: ConvexPolygonParser.EqualContext):
        components = [n for n in ctx.getChildren()]
        left_polygon = self.visit(components[1])
        right_polygon = self.visit(components[4])
        if left_polygon.equals(right_polygon):
            print("yes")
            return True
        else:
            print("no")
            return False

    # Visit a parse tree produced by ConvexPolygonParser#Color.
    def visitColor(self, ctx: ConvexPolygonParser.ColorContext):
        components = [n for n in ctx.getChildren()]
        nodeText = components[1].getText()

        if nodeText in self.variables.keys():
            color = self.visit(components[4])
            if color[0] > 1.0 or color[1] > 1.0 or color[2] > 1.0:
                raise Exception("Error: one color parameter is over 1 (color work only for range [0, 1])")
            polygon = self.variables[nodeText]
            polygon.setColor(color)
            self.variables[nodeText] = polygon
        else:
            raise Exception("Error: variable '" + nodeText + "' not exists")

    # Visit a parse tree produced by ConvexPolygonParser#RGB.
    def visitRgb(self, ctx: ConvexPolygonParser.RgbContext):
        components = [n for n in ctx.getChildren()]
        R = float(components[1].getText())
        G = float(components[3].getText())
        B = float(components[5].getText())
        return [R, G, B]

    # Visit a parse tree produced by ConvexPolygonParser#Draw.
    def visitDraw(self, ctx: ConvexPolygonParser.DrawContext):
        components = [n for n in ctx.getChildren()]
        n = len(components)
        filename = components[2].getText()
        i = 6
        pols = []
        while i < n:
            p = self.visit(components[i])
            pols.append(p)
            i += 3
        return drawPolygons(pols, filename)
