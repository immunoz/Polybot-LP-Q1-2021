from telegram.ext import Updater, CommandHandler
from sys import path
from os import getcwd
path.append(getcwd() + "\\cl")

from cl.main import get_expression_tree
from cl.PolygonTreeVisitor import PolygonTreeVisitor

my_visitor = PolygonTreeVisitor()


# Function to send messages to a user
def message(context, result, update):
    context.bot.send_message(chat_id=update.effective_chat.id, text=result)


polygon_text = 'To create a polygon it is necessary to specify a set of points that represent each ' \
               'vertex of the polygon. A set of points is represented by a pair of numbers (Integers ' \
               'or decimals) separated by double blank space each one and surrounded by brackets ([]).\n' \
               'Example:\n' \
               '- [1 1] ✅\n' \
               '- [0 0  0 2  2 0] ✅\n' \
               '- [0 0 1 1] ❌\n' \
               'A polygon can also be the result of an expression of any operation with polygons (like: ' \
               '+, *, #, !)\n' \
               'Example\n:' \
               '- [1 1] + [0 2  0 0  2 0] ✅\n' \
               '- !10 + [0  2  0 0] ✅\n' \
               '- #[2 0  3 4] * [1 1  2 0  4 5] ❌\n'

help_text = 'Hello again, if you don\'t know how to create convex polygons, please, checkout this command: ' \
            '/polygon_format. Once you know how to create polygons, use following commands to do operations ' \
            'with them:\n' \
            '/color -> Assigns a color to a given polygon\n' \
            '/draw -> Draws one or more polygons\n' \
            '/area -> Computes the area of a given polygon\n' \
            '/perimeter -> Computes the perimeter of a given polygon\n' \
            '/vertices -> Shows the number of vertices of a given polygon\n' \
            '/centroid -> Shows the centroid of a given polygon\n' \
            '/inside -> Tells whether a polygon is inside of other one\n' \
            '/equal -> Tells whether two polygons are equal or not\n' \
            '/print -> Prints a content given by the user\n' \
            '/assign -> Creates a variable\n' \
            'If you need to go in details with any command just write /[command]_format, ' \
            'in example, if you want to go in details with the /color command, you should write /color_format'


# Function that handles the /assign_format command, just gives information to the user about how create variables of polygons
def assign_format(update, context):
    message(context, 'The format to assign a name to a polygon is like the following:\n'
                     '/assign ID := polygon\n'
                     'ID is the name of the polygon\n'
                     'Polygon is the instantiation of a polygon, but also can be the result of a polygon operation (check /polygon_format)\n'
                     'Example:\n'
                     '/assign p1 := [2 2  1 1  0 2]\n'
                     '/assign p2 := [1 1] + p1', update)


# Function that handles the /my_print_format command, just gives information to the user about how print content
def my_print_format(update, context):
    message(context, 'The format to print a content is like the following:\n'
                     '/print polygon\n'
                     '/print "text"\n'
                     'The first form is to print a polygon, but also can be the result of a polygon operation (check /polygon_format)\n'
                     'The second form is to print a text. The user has to write the content surrounded by quotes (")\n'
                     'Example:\n'
                     '/print "--------"\n'
                     '/print !10 * p1', update)


# Function that handles the /area_format command, just gives information to the user about how get the area of a polygon
def area_format(update, context):
    message(context, 'The format to get the area of a polygon is like the following:\n'
                     '/area polygon\n'
                     'Polygon is the instantiation of a polygon, but also can be the result of a polygon operation (check /polygon_format)\n'
                     'Example:\n'
                     '/area [1 1  0 0  0 1]\n'
                     '/area p1 + [1 1]', update)


# Function that handles the /perimeter_format command, just gives information to the user about how get the perimeter of a polygon
def perimeter_format(update, context):
    message(context, 'The format to get the perimeter of a polygon is like the following:\n'
                     '/perimeter polygon\n'
                     'Polygon is the instantiation of a polygon, but also can be the result of a polygon operation (check /polygon_format)\n'
                     'Example:\n'
                     '/perimeter [1 1  0 0  0 1]\n'
                     '/perimeter p1 + [1 1]', update)


# Function that handles the /vertices_format command, just gives information to the user about how get the number of vertices of a polygon
def vertices_format(update, context):
    message(context, 'The format to get the number of vertices of a polygon is like the following:\n'
                     '/vertices polygon\n'
                     'Polygon is the instantiation of a polygon, but also can be the result of a polygon operation (check /polygon_format)\n'
                     'Example:\n'
                     '/vertices [1 1  0 0  0 1]\n'
                     '/vertices p1 + [1 1]', update)


# Function that handles the /centroid_format command, just gives information to the user about how get the centroid of a polygon
def centroid_format(update, context):
    message(context, 'The format to get the centroid of a polygon is like the following:\n'
                     '/centroid polygon\n'
                     'Polygon is the instantiation of a polygon, but also can be the result of a polygon operation (check /polygon_format)\n'
                     'Example:\n'
                     '/centroid [1 1  0 0  0 1]\n'
                     '/centroid p1 + [1 1]', update)


# Function that handles the /equal_format command, just gives information to the user about how to check whether two polygons are equal
def equal_format(update, context):
    message(context, 'The format to check whether a polygon A is equal to B is like the following:\n'
                     '/equal A, B\n'
                     'A and B are instantiations of a polygon, but also can be the result of a polygon operation (check /polygon_format)\n'
                     'Example:\n'
                     '/equal [1 1  0 0  0 1], [1 1  0 0  0 1]\n'
                     '/equal [1 1], p1', update)


# Function that handles the /inside_format command, just gives information to the user about how to check whether a polygon is inside another
def inside_format(update, context):
    message(context, 'The format to check whether a polygon A is inside B is like the following:\n'
                     '/inside A, B\n'
                     'A and B are instantiations of a polygon, but also can be the result of a polygon operation (check /polygon_format)\n'
                     'Example:\n'
                     '/inside p1, [1 1  0 0  0 1]\n'
                     '/inside [1 1], p1', update)


# Function that handles the /color command, just gives information to the user about how to assign a color to a polygon
def color_format(update, context):
    message(context, 'The format to assign a color to a polygon is like the following:\n'
                     '/color ID, {R, G, B}\n'
                     'ID is the name of a polygon created previously with the /assign command\n'
                     'Example:\n'
                     '/color p1, {0.9,0.7,0}', update)


# Function that handles the /draw_format command, just gives information to the user about how one or more polygons
def draw_format(update, context):
    message(context, 'The format to draw one or more polygons is like the following:\n'
                     '/draw "FILENAME.png", p1, p2, p3, ...\n'
                     'p1, p2 and p3 are polygons (either created with /assign command or directly created with the coordinates).\n'
                     'Example:\n'
                     '/draw "name.png", p1, [1 1  0 0]', update)


# Function that handles the /start command, just gives information to the user about how to start using the bot
def start(update, context):
    message(context, 'Hello, I\'m Sam, I like to do computation with convex polygons when my owner is'
                     'programming, if you need to do any computation with polygons just text me. '
                     'Before making me any questions check the /help command. Woof woof 🐕', update)


# Function that handles the /polygon_format command, just gives information to the user about how specify a polygon
def polygon_format(update, context):
    message(context, polygon_text, update)


# Function that handles the /help command, shows the user which commands can be used with the bot
def help(update, context):
    message(context, help_text, update)


# Function that handles the /assign command, basically, assigns a name to a polygon
def assign(update, context):
    try:
        get_expression_tree(update.message.text[8:], my_visitor)
        message(context, 'Variable created successfully', update)
    except Exception as e:
        message(context, 'Variable not created, an error has been thrown:' + str(e), update)
        message(context, 'If you have any errors, maybe it\'s due to the syntax of the operation,'
                         'checkout the /assign_format to see how to assign a value to a variable.', update)


# Function that handles the /print command, basically, prints a content given by the user (it can be a polygon or a text)
def my_print(update, context):
    try:
        message(context, get_expression_tree(update.message.text[1:], my_visitor), update)
    except Exception as e:
        message(context, 'Couldn\'t print the specified content, An error has been thrown:' + str(e), update)
        message(context,
                'You can only print texts and polygons. If you want to print a text, you need to surround'
                'it by quotes ("), otherwise, if you want to print a polygon, check the format needed to'
                'create polygons typing /polygon_format',
                update)


# Function that handles the /area command, tells the area of a polygon indicated by the user
def area(update, context):
    try:
        message(context, 'This is the area of your polygon:', update)
        message(context, str(get_expression_tree(update.message.text[1:], my_visitor)), update)
    except Exception as e:
        message(context,
                'Area could not be computed, an error has been thrown:' + str(e), update)
        message(context,
                'Remember that polygons in order to be created need a format. Type /polygon_format to check it out',
                update)


# Function that handles the /perimeter command, tells the perimeter of a polygon given by the user
def perimeter(update, context):
    try:
        result = str(get_expression_tree(update.message.text[1:], my_visitor))
        message(context, 'The perimeter of your polygon is the following:', update)
        message(context, result, update)
    except Exception as e:
        message(context, 'Perimeter could not be computed, an error has been thrown:' + str(e), update)
        message(context,
                'Remember that polygons in order to be created need a format. Type /polygon_format to check it out',
                update)


# Function that handles the /vertices command, tells the number of vertices of a polygon given by the user
def vertices(update, context):
    try:
        result = str(get_expression_tree(update.message.text[1:], my_visitor))
        message(context, 'The number of vertices of your polygon is the following:', update)
        message(context, result, update)
    except Exception as e:
        message(context, 'The number of vertices could not be computed, an error has been thrown:' + str(e), update)
        message(context,
                'Remember that polygons in order to be created need a format. Type /polygon_format to check it out',
                update)


# Function that handles the /centroid command, tells the centroid of a polygon given by the user
def centroid(update, context):
    try:
        message(context, 'The centroid of your polygon is the following:', update)
        result = get_expression_tree(update.message.text[1:], my_visitor)
        x = str(float(result[0]))
        y = str(float(result[1]))
        message(context, '(' + x + ',' + y + ')', update)
    except Exception as e:
        message(context, 'Centroid could not be computed, an error has been thrown: ' + str(e), update)
        message(context,
                'Remember that polygons in order to be created need a format. Type /polygon_format to check it out',
                update)


# Function that handles the /color command, assigns a color to a polygon given by the user
def color(update, context):
    try:
        get_expression_tree(update.message.text[1:], my_visitor)
        message(context, "Color assigned correctly! :)", update)
    except Exception as e:
        message(context, 'Color could not be assigned, an error has been thrown:' + str(e), update)
        message(context,
                'Remember, in order to assign a color to a polygon, you need to create a variable and write the color command '
                'correctly (check /color_format for more details)',
                update)


# Function that handles the /inside command, tell whether a polygon is inside of another polygon (both given by the user)
def inside(update, context):
    try:
        if get_expression_tree(update.message.text[1:], my_visitor):
            message(context, 'The first polygon is inside the second one', update)
        else:
            message(context, 'The first polygon is not inside the second', update)

    except Exception as e:
        message(context, 'Could not check if a polygon is inside the other, an error has been thrown: ' + str(e),
                update)
        message(context,
                'Remember that polygons in order to be created need a format. Type /polygon_format to check it out',
                update)


# Function that handles the /equal command, tell whether a polygon is equal to other polygon (both given by the user)
def equal(update, context):
    try:
        if get_expression_tree(update.message.text[1:], my_visitor):
            message(context, 'Both polygons are equal', update)
        else:
            message(context, 'The polygons are not equal', update)
    except Exception as e:
        message(context, 'Could not check if a polygon is equal the other, an error has been thrown: ' + str(e), update)
        message(context,
                'Remember that polygons in order to be created need a format. Type /polygon_format to check it out',
                update)


# Function that handles the /draw command, sends a picture of the polygons indicated by the user
def draw(update, context):
    try:
        filename = get_expression_tree(update.message.text[1:], my_visitor)
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(filename, 'rb'))
    except Exception as e:
        message(context, 'An error has been thrown: ' + str(e), update)
        message(context,
                'Remember, in order to draw a polygon, check that the polygons are created correctly. Type /polygon_format '
                'to check the format of creation of polygons. Also remember to write the draw command correctly (checkout '
                'the /draw_format for more details)',
                update)


TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('assign', assign))
dispatcher.add_handler(CommandHandler('print', my_print))
dispatcher.add_handler(CommandHandler('area', area))
dispatcher.add_handler(CommandHandler('perimeter', perimeter))
dispatcher.add_handler(CommandHandler('vertices', vertices))
dispatcher.add_handler(CommandHandler('centroid', centroid))
dispatcher.add_handler(CommandHandler('color', color))
dispatcher.add_handler(CommandHandler('inside', inside))
dispatcher.add_handler(CommandHandler('equal', equal))
dispatcher.add_handler(CommandHandler('draw', draw))
dispatcher.add_handler(CommandHandler('assign_format', assign_format))
dispatcher.add_handler(CommandHandler('print_format', my_print_format))
dispatcher.add_handler(CommandHandler('area_format', area_format))
dispatcher.add_handler(CommandHandler('perimeter_format', perimeter_format))
dispatcher.add_handler(CommandHandler('vertices_format', vertices_format))
dispatcher.add_handler(CommandHandler('centroid_format', centroid_format))
dispatcher.add_handler(CommandHandler('color_format', color_format))
dispatcher.add_handler(CommandHandler('inside_format', inside_format))
dispatcher.add_handler(CommandHandler('equal_format', equal_format))
dispatcher.add_handler(CommandHandler('draw_format', draw_format))
dispatcher.add_handler(CommandHandler('polygon_format', polygon_format))

updater.start_polling()
