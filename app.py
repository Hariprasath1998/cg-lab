from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

from lineDrawing import DDA
from lineDrawing import bresenhamLine
from circleDrawing import circleDrawing
from ellipseDrawing import ellipseDrawing

Vertices =[]
xAxis = [(x, 0) for x in range(-250, 251)]
yAxis = [(0, y) for y in range(-250, 251)]




def basicInit(windowSize = 500):
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)   
    glutInitWindowSize(windowSize, windowSize)  
    glutInitWindowPosition(0, 0)  
    glutCreateWindow("CG Algorithms")
    glClearColor(0.95, 0.95, 0.95, 1.0) 
    glColor3f(1.0,1.0,0.0)
    glPointSize(2.0)
    gluOrtho2D(-(windowSize / 2), (windowSize / 2), -(windowSize / 2), (windowSize / 2))
 
def display():
    counter = 0
    global Vertices
    global xAxis
    global yAxis
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    
    for x in Vertices:
        glColor3f(0.0,0.0,0.8)
        glVertex2f(x[0],x[1])
    for x in xAxis:
        glColor3f(0.0,0.7,0.0)
        glVertex2f(x[0],x[1])
    for x in yAxis:
        glColor3f(0.0,0.7,0.0)
        glVertex2f(x[0],x[1])
    glEnd()

    glFlush()

def prompt():
    global Vertices
    algorithms = [DDA, bresenhamLine, circleDrawing, ellipseDrawing]
    print("0)DDA\n1)Bresenham's\n2)Circle\n3)Ellipse")
    choice = int(input("Enter your Choice: "))
    # choice = 0
    Vertices = algorithms[choice]()

def main():
    basicInit()
    prompt()
    glutDisplayFunc(display)
    glutMainLoop()

main()