import pygame
from pygame.locals import *
from turtle import *
from OpenGL.GL import *
from OpenGL.GLU import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from threading import Thread, Lock

# Connect to Firebase
cred = credentials.Certificate(
    '../FirebaseKey/fingergesturerecognitionsystem-firebase-adminsdk-xcpqf-cf83d06251.json')  # get service account key JSON
# Initialize with service account to get admin privileges
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': "https://fingergesturerecognitionsystem-default-rtdb.firebaseio.com/"
})

gesture_ref = firebase_admin.db.reference('/Prediction/Gesture')


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
    (1, -1, -1),  # coordinates of node 0
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),

)

verticies_triangle = (
    (-1, 0, 1),
    (-1, 0, -1),
    (1, 0, 0),
    (0, 3, 0),
)

# an edge ( i.e. cnxn between two nodes)
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
    (0, 1, 2, 3),  # surface connecting node 0,1,2,3
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6),
)

surfaces_triangle = (
    (0, 1, 2),  # surface connecting node 0,1,2
    (0, 1, 3),
    (0, 2, 3),
    (1, 2, 3)
)

# colours
colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 0, 0),
    (1, 1, 1),
    (0, 1, 1),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 0, 0),
    (1, 1, 1),
    (0, 1, 1),
)


# making our cube
# everytime we do gl code/object, we have to encase it with glBegin and glEnd
def Cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0

        for vertex in surface:
            x += 2
            glColor3fv(colors[x])  # colour, rgb
            glVertex3fv(verticies_cube[vertex])
    glEnd()

    glBegin(GL_LINES)  # here we notify opengl what kindof graphics we are putting here (consant)
    for edge in edges_cube:
        for vertex in edge:
            glVertex3fv(verticies_cube[vertex])  # basically drawing the vertices and connecting them
    glEnd()  # this one stays empty


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
    global resetShape
    global currentShape

    # REMOVED THESE WHEN CHANGED FROM main() TO "__main__"
    # lock = threading.Lock()
    # global gesture

    # ADDED THESE WHEN CHANGED FROM main() TO "__main__"
    lock = Lock()
    changeCount = 0
    currentShape = ''
    resetShape = False
    gesture = ""

    pygame.init()  # pygame initialization
    display = (800, 600)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)  # we have to tell pygame we r using opengl

    # (field of view, aspect ratio=width/height, clipping planes = plane tht clips away showimng the object
    # ie when u zoom out a lot it's going to disapear, 0,1 then 50 is pretty wide)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -10)  # x-y-z parameters, us moving about the objet
    glRotatef(25, 2, 1, 0)  # (degree,x,y,z)

    # ADDED THREAD T1 & START WHEN CHAINED main() TO "__main__"
    t1 = Thread(target=getGesture, args=(lock,))
    t1.start()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # FOR RESET
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    resetShape = True

        if gesture == "up":
            glTranslatef(0, 1, 0)
        elif gesture == "down":
            glTranslatef(0, -1, 0)
        elif gesture == "left":
            glTranslatef(-1, 0, 0)
        elif gesture == "right":
            glTranslatef(1, 0, 0)
        elif gesture == "clock":
            glTranslatef(25, 1, 1, 1)
        elif gesture == "counter":
            glTranslatef(25, -1, -1, -1)

        # FOR WHEN WE HAVE ALL GESTURES
        elif gesture == "snap":
            changeCount = changeCount + 1
        elif gesture == "pinch_in":
            glTranslatef(0, 1.0, 1.0)
        elif gesture == "pinch_out":
            glTranslatef(0, 0, -1.0)
        gesture = ""
        print("EMPTY GESTURE", gesture)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # colour of background
        glClearColor(0.7, 0.8, 0.88, 1)  # (red, green, blue, alpha)
        glClear(GL_COLOR_BUFFER_BIT)

        # Changing Shapes
        if changeCount % 2 != 0:
            Triangle()
            currentShape = 'Triangle'
        elif changeCount % 2 == 0:
            Cube()
            currentShape = 'Cube'

        # Resetting Shapes
        if resetShape:
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

        pygame.display.flip()  # an alternative could be display.update()
        pygame.time.wait(10)  # in ms

    # JOINING THREAD
    t1.join()

# if __name__ == "__main__":
#     main()
