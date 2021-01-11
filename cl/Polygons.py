import math
from decimal import Decimal

from PIL import Image, ImageDraw


# Pre: vertices_result and points are a set of points
# Post: those points inside points that are not inside vertices_result are inserted into vertices_result
def add_points(vertices_result, points):
    for p in points:
        found = False
        for p2 in vertices_result:
            if p == p2:
                found = True
                break
        if not found:
            vertices_result.append(p)


# Pre: p1 and p2 are points and x, y are coordinates
# Post: returns true if the point represented by x, y is inside the segment p1-p2
def on_segment(p1, p2, x, y):
    cond1 = (min(p1[0], p2[0]) < x or min(p1[0], p2[0]) == x)
    cond2 = (max(p1[0], p2[0]) > x or max(p1[0], p2[0]) == x)
    cond3 = (min(p1[1], p2[1]) < y or min(p1[1], p2[1]) == y)
    cond4 = (max(p1[1], p2[1]) > y or max(p1[1], p2[1]) == y)
    return cond1 and cond2 and cond3 and cond4


# Pre: p1, p2, e1, e2 are points
# Post: If edge p1-p2 and e1-e2 intersect returns the intersection point, otherwise returns ()
def getIntersectionPoint(p1, p2, e1, e2):
    A1 = p2[1] - p1[1]
    B1 = p1[0] - p2[0]
    C1 = A1 * p1[0] + B1 * p1[1]

    A2 = e2[1] - e1[1]
    B2 = e1[0] - e2[0]
    C2 = A2 * e1[0] + B2 * e1[1]

    det = A1 * B2 - A2 * B1
    if det == 0:
        return ()
    else:
        x = (B2 * C1 - B1 * C2) / det
        y = (A1 * C2 - A2 * C1) / det
        on_segment_one = on_segment(p1, p2, x, y)
        on_segment_two = on_segment(e1, e2, x, y)
        if on_segment_one and on_segment_two:
            return (x, y)
    return ()


# Pre: p1 and p2 are points, and vertices are the vertices of a polygon
# Post: returns a list of the intersection points between edge p1-p2 and the polygon represented by vertices
def getIntersectionPoints(p1, p2, vertices):
    intersection_points = []
    n = len(vertices)
    for i in range(0, n):
        j = (i + 1) % n
        intersection = getIntersectionPoint(p1, p2, vertices[i], vertices[j])
        if intersection != ():
            intersection_points.append(intersection)
    return intersection_points


class ConvexPolygon:
    # this value is used to simulate the infinity of a segment, and we set it because the operation
    # do intersect uses orientation, and inside orientation some multiplications are done. Setting
    # this number as limit we avoid overflow problems.
    INT_MAX = 10000

    # Constructor of the convex polygon
    def __init__(self):
        self.hull = []
        self.color = [0, 0, 0]

    # Pre:
    # Returns the points of the polygon in string format
    def print(self):
        n = len(self.hull)
        i = 0
        txt = ''
        while i < n:
            txt += str(self.hull[i][0]) + ' ' + str(self.hull[i][1])
            if i != n - 1:
                txt += ' '
            else:
                txt += '\n'
            i += 1
        print(txt)
        return txt

    # Pre: p1, p2, x are points
    # Post: returns true if x is on segment p1-p2, otherwise returns false
    def onSegment(self, p1, x, p2):
        if ((x[0] <= max(p1[0], p2[0])) & (x[0] >= min(p1[0], p2[0])) & (x[1] <= max(p1[1], p2[1])) & (
                x[1] >= min(p1[1], p2[1]))):
            return True
        return False

    # Pre: p1, p2 and p3 are points
    # Post: Given p1, p2, p3, returns a value that indicates if the three points are
    # collinear, clockwise, counterclockwise:
    # value = 0 -> Collinear
    # value = 1 -> Clockwise
    # value = 2 -> Counterclockwise
    def orientation(self, p1, p2, p3):
        val = (((p2[1] - p1[1]) * (p3[0] - p2[0])) - ((p2[0] - p1[0]) * (p3[1] - p2[1])))

        if val == 0:
            return 0
        if val > 0:
            return 1
        else:
            return 2

    # Pre: p1, q1, p2, q2 are points
    # Returns true if edge p1-q1 and p2-q2 intersect
    def doIntersect(self, p1, q1, p2, q2):
        # Find the four orientations needed for
        # general and special cases
        o1 = self.orientation(p1, q1, p2)
        o2 = self.orientation(p1, q1, q2)
        o3 = self.orientation(p2, q2, p1)
        o4 = self.orientation(p2, q2, q1)

        # General case
        if (o1 != o2) and (o3 != o4):
            return True

        # Special Cases
        # p1, q1 and p2 are colinear and
        # p2 lies on segment p1q1
        if (o1 == 0) and (self.onSegment(p1, p2, q1)):
            return True

        # p1, q1 and p2 are colinear and
        # q2 lies on segment p1q1
        if (o2 == 0) and (self.onSegment(p1, q2, q1)):
            return True

        # p2, q2 and p1 are colinear and
        # p1 lies on segment p2q2
        if (o3 == 0) and (self.onSegment(p2, p1, q2)):
            return True

        # p2, q2 and q1 are colinear and
        # q1 lies on segment p2q2
        if (o4 == 0) and (self.onSegment(p2, q1, q2)):
            return True

        return False

    def iteration(self, p, setOfVertices):
        self.hull.append(setOfVertices[p])
        n = len(setOfVertices)
        q = (p + 1) % n
        for i in range(0, n):
            if self.orientation(setOfVertices[p], setOfVertices[q], setOfVertices[i]) == 2:
                q = i
        return q

    # Pre: setOfVertices is a non null list
    # Body: Constructs a convex hull and it's stored in the class instance
    def constructPolygon(self, setOfVertices):
        n = len(setOfVertices)
        left = 0

        for i in range(1, n):
            if setOfVertices[i][0] < setOfVertices[left][0] or (
                    setOfVertices[i][0] == setOfVertices[left][0] and setOfVertices[i][1] < setOfVertices[left][1]):
                left = i

        p = left
        p = self.iteration(p, setOfVertices)
        # self.hull.append(setOfVertices[p])
        # q = (p + 1) % n
        # for j in range(0, n):
        #    if self.orientation(setOfVertices[p], setOfVertices[q], setOfVertices[j]) == 2:
        #        q = j
        # p = q
        while p != left:
            p = self.iteration(p, setOfVertices)
            # self.hull.append(setOfVertices[p])
            # q = (p + 1) % n
            # for j in range(0, n):
            #    if self.orientation(setOfVertices[p], setOfVertices[q], setOfVertices[j]) == 2:
            #        q = j
            # p = q

    # Pre: points are the vertices of a polygon and p is a point
    # Post: returns true if p is inside points
    def is_inside_polygon(self, points, p):
        n = len(points)

        # Create a point for line segment
        # from p to infinite
        extreme = (self.INT_MAX, p[1])
        count = i = 0

        while True:
            next = (i + 1) % n
            if self.doIntersect(points[i], points[next], p, extreme):
                if self.orientation(points[i], p, points[next]) == 0:
                    return self.onSegment(points[i], p, points[next])

                count += 1

            i = next
            if i == 0:
                break
        return count % 2 == 1

    # Pre: p is a point with x and y coordinates
    # Post: Returns true if p is inside the current polygon, otherwise, returns false
    def CheckPointInside(self, p):
        return self.is_inside_polygon(self.hull, p)

    # Pre:
    # Post: Returns the number of vertices or edges (number of vertices and edges are the same) that form the polygon
    def numberOfVerticesAndEdges(self):
        return len(self.hull)

    # Pre: p is a polygon to be checked if it's inside the polygon
    # Post: returns true if p is inside the current polygon (edges are included), otherwise, returns false.
    def checkIfPolygonIsInside(self, p):
        k = len(p.hull)
        for i in range(0, k):
            if not self.CheckPointInside(p.hull[i]):
                return False
        return True

    # Pre:
    # Post: Returns the area of the Polygon (shoelace(Gauss) method)
    def area(self):
        n = len(self.hull)
        area = Decimal(0.0)
        j = n - 1
        for i in range(0, n):
            area += (self.hull[j][0] + self.hull[i][0]) * (self.hull[j][1] - self.hull[i][1])
            j = i

        return abs(area / Decimal(2.0))

    # Post: Returns the perimeter of the polygon by computing summing the distances between all the vertices that
    # composite the polygon
    def perimeter(self):
        n = len(self.hull)
        perimeter = 0.0
        j = n - 1
        for i in range(0, n):
            perimeter += self.distance(self.hull[i], self.hull[j])
            j = i
        return Decimal(perimeter)

    # Pre: x and y are two points
    # Post: Returns the distance between the two points
    def distance(self, x, y):
        return math.sqrt(pow(x[0] - y[0], 2) + pow(x[1] - y[1], 2))

    # Pre:
    # Post Returns true if the current polygon is regular or not
    def isRegular(self):
        n = len(self.hull)
        j = n - 1
        edgeLength = self.distance(self.hull[0], self.hull[j])
        for i in range(0, n):
            if not edgeLength == self.distance(self.hull[i], self.hull[j]):
                return False
            j = i
        return True

    # Pre:
    # Body: Returns the centroid in the form of a tuple C(x,y), where x and y are the coordinates of the centroid
    def centroid(self):
        cX = cY = det = 0
        n = len(self.hull)
        for i in range(0, n):
            if i + 1 == n:
                j = 0
            else:
                j = i + 1

            td = self.hull[i][0] * self.hull[j][1] - self.hull[j][0] * self.hull[i][1]
            det += td

            cX += (self.hull[i][0] + self.hull[j][0]) * td
            cY += (self.hull[i][1] + self.hull[j][1]) * td
        cX /= 3 * det
        cY /= 3 * det

        cX = Decimal(cX)
        cY = Decimal(cY)
        return (round(cX, 3), round(cY, 3))

    # Pre: poly is a convex polygon
    # Post: returns the union of the current polygon with poly
    def union(self, poly):
        result = ConvexPolygon()
        result.constructPolygon(self.unitePoints(self, poly))
        return result

    # Pre: a and b are a set of vertices (tuple (x,y), being x and y coordinates of the point)
    # Body: returns the union of both list of vertices, a and b
    def unitePoints(self, a, b):
        result = list(set(a.hull) | set(b.hull))
        return result

    # Pre:
    # Body: returns te points that forms the current convex polygon
    def getHull(self):
        return self.hull

    # Pre:
    # Body: returns the first point of the current convex polygon
    def getFirstPoint(self):
        return self.hull[0]

    # Pre: poly is the polygon that we are going to intersect
    # Post: result is the intersection of the current polygon with poly
    def intersection(self, poly):
        vertices_result = []
        for p in self.hull:
            if poly.CheckPointInside(p):
                add_points(vertices_result, [p])

        for p in poly.hull:
            if self.CheckPointInside(p):
                add_points(vertices_result, [p])

        n = len(self.hull)
        for i in range(0, n):
            j = (i + 1) % n
            add_points(vertices_result, getIntersectionPoints(self.hull[i], self.hull[j], poly.hull))
        result = ConvexPolygon()
        result.constructPolygon(vertices_result)
        return result

    # Pre: p is a polygon
    # Post: returns true if the current polygon is equal to p, otherwise returns false
    def equals(self, p):
        return self.hull == p.hull

    # Pre: colors is an array representing an RGB color
    # Post: Changes the color of the current polygon
    def setColor(self, colors):
        R = int(colors[0] * 255)
        G = int(colors[1] * 255)
        B = int(colors[2] * 255)
        self.color = [R, G, B]

    # Pre:
    # Post: returns the color of the polygon in hexadecimal format
    def getColorHex(self):
        result = '#%02x%02x%02x' % (self.color[0], self.color[1], self.color[2])
        return result

    # Pre: xScale and yScale are the factors to scale the points in the convex hull
    # Post: result has the set of vertices of the current polygon with all the vertices scaled
    def scale(self, xScale, yScale):
        result = []
        for p in self.hull:
            scaledPoint = (p[0] * xScale, p[1] * yScale)
            result.append(scaledPoint)
        return result


# Pre: polygons is the list of polygons from where we are getting the bounding box
# Body: returns the coordinates of the bounding box containing all the polygons in the input list
def boundingBox(polygons):
    min_x = polygons[0].getFirstPoint()[0]
    min_y = polygons[0].getFirstPoint()[1]
    max_x = polygons[0].getFirstPoint()[0]
    max_y = polygons[0].getFirstPoint()[1]
    for polygon in polygons:
        vertices = polygon.getHull()
        for vertex in vertices:
            if vertex[0] < min_x:
                min_x = vertex[0]
            if vertex[0] > max_x:
                max_x = vertex[0]
            if vertex[1] < min_y:
                min_y = vertex[1]
            if vertex[1] > max_y:
                max_y = vertex[1]
    return [(round(Decimal(min_x), 3), round(Decimal(min_y), 3)), (round(Decimal(max_x), 3), round(Decimal(max_y), 3))]


# Pre: polygons are the set of polygons to draw and filename is the name of the output file.
# Post: on the directory there is a new file called as 'filename', and it's an image of the polygons
def drawPolygons(polygons, filename):
    bounding = boundingBox(polygons)
    if bounding[0] == bounding[1]:
        raise NameError('Polygon with one point cannot be drawn')

    x_scale = 1
    if bounding[1][0] - bounding[0][0] != 0:
        x_scale = Decimal(Decimal(398) / (bounding[1][0] - bounding[0][0]))

    y_scale = 1
    if bounding[1][1] - bounding[0][1] != 0:
        y_scale = Decimal(Decimal(398.0) / (bounding[1][1] - bounding[0][1]))

    img = Image.new('RGB', (400, 400), 'White')
    dib = ImageDraw.Draw(img)
    for polygon in polygons:
        dib.polygon(polygon.scale(x_scale, y_scale), 'White', polygon.getColorHex())
    img.save(filename)
    return filename
