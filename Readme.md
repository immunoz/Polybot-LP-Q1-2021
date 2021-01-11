# PolyBot - @UltraSamBot

This project implements a telegram bot that makes computation with polygons. The bot creates convex polygons given a set of vertices and can execute operations with them like:
* Intersection
* Convex Union
* Bounding Box
* Check if a polygon is inside other
* Check whether two polygons are equal
* Draw polygons
* Compute the centroid of a polygon
* Compute the number of vertices of a polygon

You can find the statement of this project in the following [link](https://github.com/jordi-petit/lp-polimomis-2020)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Important!

This project was developed on Windows, so, if you have any problems when trying to execute it, just checkout the libraries, modules and imports of the project.


### Prerequisites

To configure environment of the project on your machine, first install python 3 (checkout Built With section of this readme) and execute the following commands on your machine:

```
pip3 install pillow
pip3 install python-telegram-bot
pip3 install antlr4-python3-runtime or pip install antlr4-python3-runtime

```
to install antlr4:
* Download the jar file from this [link](https://www.antlr.org/download.html)
* Follow the instructions on this [link](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md)

Apart from those installations, you can use PyCharm with Antlr4 plugin to work more comfortably.

## Running the tests

Inside the project you will find this distribution of files:
* cl
	* PolygonTreeVisitor.py (Contains the implementation of our visitor)
	* main.py (Has a code to interact with the visitor)
	* ConvexPolygon.g (Contains the grammar of our programming language)
	* Polygons.py (Contains the code of the ConvexPolygon class)
* bot.py (Contains the implementation of the Telegram bot)
* token.txt (Contains the token of our Telegram bot)
* requirements.txt (File that contains the requirements of this project)
* Readme.md

The statement was divided in three parts.

### First part: create a class to work with convex polygons
You can find the implementation in the Polygons.py file and use this class to do operations with convex polygons, just import it to your project.

Inside the code there are some annotations of each function explaining what it does.

### Second part: create a programming language to work with convex polygons using antlr with python

To compile the grammar use the following command inside the cl folder:
```
antlr4 -Dlanguage=Python3 -no-listener -visitor ConvexPolygon.g
```

Once the grammar is compiled, you can use the PolygonTreeVisitor.py to make operations with polygons.

Inside the PolygonTreeVisitor class there is a map named variables that will store the variables created by the user.

Most of the operations inside the visitor return Polygons, but sometimes just returns a string with the result of the operation done.

### Third part: create a bot to interact with convex polygons
When the grammar has been created, execute the bot using the following command inside the project folder:
````
python bot.py
````
Once the bot is running, just talk to @UltraSamBot, he will guide you with the polygons operations. Also, there is a /help command if you feel lost at any moment.
### Coding style

This project has been written following the PEP8 style rules.

## Built With

* [Python](https://docs.python.org/3/) - Language used to code this project
* [ANTLR](https://www.antlr.org/download.html) - Used to create the grammar
* [Telegram](https://core.telegram.org/bots) - Used to create this bot
* [Pillow](https://xn--llions-yua.jutge.org/grafics/) - Library used to draw the polygons
* [PyCharm](https://www.jetbrains.com/es-es/pycharm/) - IDE used in this project

## Authors

* **Isaac Marcelo Muñoz Cruz** - *Polybot: UltraSam* - [Polybot Repo](https://github.com/immunoz/PolyBot-LP-2021-Q1)
