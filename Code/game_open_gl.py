import pygame
from pygame.locals import *
from turtle import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
# from threading import Thread, Lock
import threading

# Connect to Firebase
cred = credentials.Certificate(
    '../FirebaseKey/fingergesturerecognitionsystem-firebase-adminsdk-xcpqf-cf83d06251.json')  # get service account key JSON
# Initialize with service account to get admin privileges
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': "https://fingergesturerecognitionsystem-default-rtdb.firebaseio.com/"
})

gesture_ref = firebase_admin.db.reference('/Prediction/Gesture')
lock = threading.Lock()


def resetShape():
    if currentShape == 'Cube':
        glLoadIdentity()
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -10)  # x-y-z parameters, us moving about the objet
        glRotatef(25, 2, 1, 0)  # (degree,x,y,z)

    elif currentShape == 'Triangle':
        glLoadIdentity()
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -10)  # x-y-z parameters, us moving about the objet
        glRotatef(25, 2, 1, 0)  # (degree,x,y,z)


def getGesture(gest_rec):
    global gesture
    lock.acquire()
    gesture = gest_rec
    lock.release()


def listener(event):
    if event.path == "/":
        print("SKIP")
    elif event.path == "/Test":
        getGesture(gesture_ref.get())


gesture_listener = firebase_admin.db.reference('/Prediction').listen(listener)

# a cube has 8 verticies
verticies_cube = (
    # (1, -1, -1),  # coordinates of node 0
    # (1, 1, -1),
    # (-1, 1, -1),
    # (-1, -1, -1),
    # (1, -1, 1),
    # (1, 1, 1),
    # (-1, -1, 1),
    # (-1, 1, 1),

    #VERTICES FOR SOLID CUBE WITH DIFFERENT COLOURS ON EACH PHASE
    (1, 1, 1),
    (1, -1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
    (1, 1, -1),
    (1, -1, -1),
    (-1, -1, -1),
    (-1, 1, -1),

)

verticies_triangle = (
    (-1, 0, 1),
    (-1, 0, -1),
    (1, 0, 0),
    (0, 3, 0),
)

#NOT NEEDED FOR NEW CUBE
edges_cube = (

    (0, 1),  # node 0 connected to node 1
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),

)

edges_triangle = (

    (0, 1),
    (0, 2),
    (1, 2),
    (3, 0),
    (3, 1),
    (3, 2),

)

# surfaces of the cube
surfaces = (
    # (0, 1, 2, 3),  # surface connecting node 0,1,2,3
    # (3, 2, 7, 6),
    # (6, 7, 5, 4),
    # (4, 5, 1, 0),
    # (1, 5, 7, 2),
    # (4, 0, 3, 6),

    #SURFACES FOR SOLID CUBE WITH DIFFERENT COLOURS ON EACH PHASE
    (0, 1, 2, 3),
    (4, 5, 1, 0),
    (0, 1, 5, 4),
    (3, 2, 6, 7),
    (0, 3, 7, 4),
    (1, 2, 6, 5),
)

surfaces_triangle = (
    (0, 1, 2),  # surface connecting node 0,1,2
    (0, 1, 3),
    (0, 2, 3),
    (1, 2, 3)
)

# colours
colors = (
    # (1, 0, 0),
    # (0, 1, 0),
    # (0, 0, 1),
    # (0, 0, 0),
    # (1, 1, 1),
    # (0, 1, 1),
    # (1, 0, 0),
    # (0, 1, 0),
    # (0, 0, 1),
    # (0, 0, 0),
    # (1, 1, 1),
    # (0, 1, 1),

    ##############
    #GHAITH COLOURS -> OLD CUBE
    # (1, 1, 0),  # yellow
    # (0, 1, 0),  # green
    # (0.75, 0.38, 0),  # Orange
    # (1, 1, 1),  # white
    # (0.9, 0, 0),  # Red
    # (0, 0, 1)  # Blue
    ########

    #DIFFERENT COLOURS ON EACH PHASE
    # (1, 0, 1),
    # (1, 1, 0),
    # (0, 1, 1),
    # (1, 0, 0),
    # (0, 0, 1),
    # (0, 1, 0),
    # (1, 1, 1),
    #(1, 0, 0), # red
    #(1, 0, 0), # red
    (0.714, 0.839, 0.89), #b6d6e3 -> pretty blue
    (0.612, 0.925, 0.357), # 9CEC5B
    (0.843, 0.992, 0.925),  # D7FDEC
    (0.663, 0.984, 0.843),  # A9FBD7
    (0.698, 0.894, 0.859),  # B2E4DB
    (0.690, 0.776, 0.808),  # B0C6CE
    (0, 0, 1), # blue
    #(0.576, 0.545, 0.631),   # 938BA1

)


# making our cube
# everytime we do gl code/object, we have to encase it with glBegin and glEnd
def Cube():
    glBegin(GL_QUADS)
    #glColor3f(0.0, 1.0, 0.0)
    glColor3f(0.714, 0.839, 0.89) #b6d6e3
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)

    #glColor3f(1.0, 0.0, 0.0)
    glColor3f(0.612, 0.925, 0.357) # 9CEC5B
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)

    #glColor3f(0.0, 1.0, 0.0)
    glColor3f(0.843, 0.992, 0.925) # D7FDEC
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    #glColor3f(1.0, 1.0, 0.0)
    glColor3f(0.663, 0.984, 0.843),  # A9FBD7
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)

    #glColor3f(0.0, 0.0, 1.0)
    glColor3f(0.698, 0.894, 0.859),  # B2E4DB
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)

    #glColor3f(1.0, 0.0, 1.0)
    glColor3f(0.690, 0.776, 0.808),  # B0C6CE
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)

    glEnd()

    # NOT NEEDED F0R NEW NEW CUBE
    # x = 0
    # for surface in surfaces:
    #     #x = 0
    #     x += 1
    #     #glColor3fv(colors[x])
    #     for vertex in surface:
    #
    #         # for original colour matrix
    #         # x += 2
    #         #
    #         # # for green/red matrix
    #         # x += 1
    #         #glDisable(GL_CULL_FACE)
    #         glColor3fv(colors[x])  # colour, rgb
    #         glVertex3fv(verticies_cube[vertex])
    #NOT NEEDED FOR NEW CUBE
    # glBegin(GL_LINES)  # here we notify opengl what kindof graphics we are putting here (consant)

    # for edge in edges_cube:
    #     x += 1
    #     glColor3fv(colors[x])
    #     for vertex in edge:
    #         glVertex3fv(verticies_cube[vertex])  # basically drawing the vertices and connecting them
    # glEnd()  # this one stays empty


def Triangle():
    glBegin(GL_TRIANGLES)

    for surface in surfaces_triangle:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])  # colour, rgb
            glVertex3fv(verticies_triangle[vertex])

    glEnd()

    glBegin(GL_LINES)
    for edge in edges_triangle:
        for vertex in edge:
            glVertex3fv(verticies_triangle[vertex])

    glEnd()


# def main():
if __name__ == "__main__":
    global changeCount
    global currentShape
    global currentMatrix

    # REMOVED THESE WHEN CHANGED FROM main() TO "__main__"
    # lock = threading.Lock()
    # global gesture

    # ADDED THESE WHEN CHANGED FROM main() TO "__main__"
    # lock = Lock()
    changeCount = 0
    # currentShape = ''
    gesture = ""

    pygame.init()  # pygame initialization
    display = (800, 600)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)  # we have to tell pygame we r using opengl
    glEnable(GL_DEPTH_TEST)

    # (field of view, aspect ratio=width/height, clipping planes = plane tht clips away showimng the object
    # ie when u zoom out a lot it's going to disapear, 0,1 then 50 is pretty wide)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)  # x-y-z parameters, us moving about the objet
    glRotatef(25, 2, 1, 0)  # (degree,x,y,z)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # FOR RESET
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    resetShape()

        if gesture == "up":
            glTranslatef(0, 1, 0)
            print("GESTUTRE ", gesture)
        elif gesture == "down":
            glTranslatef(0, -1, 0)
            print("GESTUTRE ", gesture)
        elif gesture == "left":
            glTranslatef(-1, 0, 0)
            print("GESTUTRE ", gesture)
        elif gesture == "right":
            glTranslatef(1, 0, 0)
            print("GESTUTRE ", gesture)
        elif gesture == "clock":
            #glRotatef(25, -1, -1, -1)
            glRotatef(30, 0, 0, -1)
            print("GESTUTRE ", gesture)
        elif gesture == "counter":
            #glRotatef(25, 1, 1, 1) #all axis
            glRotatef(30, 0, 1, 0) # only y
            #glRotatef(30, 0, 0, 1)  # only x
            print("GESTUTRE ", gesture)

        # FOR WHEN WE HAVE ALL GESTURES
        elif gesture == "snap":
            changeCount = changeCount + 1
            print("GESTUTRE ", gesture)
        elif gesture == "pinch_in":
            glTranslatef(0, 1.0, 1.0)
            print("GESTUTRE ", gesture)
        elif gesture == "pinch_out":
            glTranslatef(0, 0, -1.0)
            print("GESTUTRE ", gesture)
        gesture = ""

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # BACKGROUND COLOUR
        #glClearColor(0.7, 0.8, 0.88, 1)  # (red, green, blue, alpha)
        #glClearColor(0, 0, 0, 1) # black
        glClearColor(1, 1, 1, 1) # white -> POSSIBILITY
        #glClearColor(0.576, 0.545, 0.631,0)  # 938BA1
        #glClearColor(0.502, 0.502, 0.502, 1) #808080 grey
        #glClearColor(0.792, 0.808, 0.812, 1) #cacecf light grey
        #glClearColor(0.753, 0.753, 0.753, 0) #C0C0C0 silver
        #glClearColor(0.753, 0.824, 0.851, 1) # c0d2d9 -> light blue: POSSIBILITY
        #glClearColor(0.953, 1, 1, 1) # f3ffff -> twilight : POSSIBILITY

        glClear(GL_COLOR_BUFFER_BIT)

        # Changing Shapes
        if changeCount % 2 != 0:
            Triangle()
            currentShape = 'Triangle'
        elif changeCount % 2 == 0:
            #glEnable(GL_DEPTH_TEST)
            Cube()
            currentShape = 'Cube'


        pygame.display.flip()  # an alternative could be display.update()
        pygame.time.wait(10)  # in ms

# if __name__ == "__main__":
#     main()
