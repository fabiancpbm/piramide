from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

# Altura do  triângulo.
height = int (sys.argv[1]) if len(sys.argv) > 1 else 1.7

# Porcentagem de corte da altura (valor de 0 a 1). 0 significa 0% de corte, 1 significa 100% de corte.
cutPercentage = float (sys.argv[2]) if len(sys.argv) > 2 else 0

# Altura cortada em cutPercentage porcento.
cutH = height * (cutPercentage)

# Altura restante pós corte.
h = height * (1 - cutPercentage)

# Ângulo do triângulo
theta = math.pi/6

# Hipotenusa do triângulo cujo cateto oposto é cutH e ângulo theta.
hip = cutH/math.sin(theta)

# O valor de corte é o cateto adjacente do triângulo cujo cateto oposto é cutH e ângulo theta.
cutValue = (hip**2 - cutH**2)**0.5

vertices = (
    ( 1,-1,-1),
    ( cutValue, h,-cutValue),
    (-cutValue, h,-cutValue),
    (-1,-1,-1),
    ( 1,-1, 1),
    ( cutValue, h, cutValue),
    (-1,-1, 1),
    (-cutValue, h, cutValue),
    )

linhas = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    )

faces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )
def Piramide():
    glBegin(GL_QUADS)
    i = 0
    for face in faces:
        glColor3fv(cores[i])
        for vertex in face:
            glColor3fv(cores[vertex])
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
