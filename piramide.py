from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

h = int (sys.argv[1]) if len(sys.argv) > 1 else 1.7

vertices = (
    ( 0, h, 0),
    ( 1, 0, 1),
    ( 1, 0,-1),
    (-1, 0,-1),
    (-1, 0, 1)
    )

linhas = (
    (0,1),
    (0,2),
    (0,3),
    (0,4),
    (1,2),
    (2,3),
    (3,4),
    (4,1)
    )

faces = (
    (0,1,2),
    (0,2,3),
    (0,3,4),
    (0,4,1),
    (1,2,3),
    (1,3,4)
    )

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(0,0,1) )

def Piramide():
    glBegin(GL_TRIANGLES)
    i = 0
    for face in faces:
        glColor3fv(cores[i])
        for vertex in face:
            glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()

    glColor3fv((0,0.5,0))
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()

def desenhar():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(3,2,4,0)
    Piramide()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Piramide")
glutDisplayFunc(desenhar)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
