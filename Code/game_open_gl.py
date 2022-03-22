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
import math

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

verticies_triangle = (
    (-1, 0, 1),
    (-1, 0, -1),
    (1, 0, 0),
    (0, 3, 0),
)

edges_triangle = (

    (0, 1),
    (0, 2),
    (1, 2),
    (3, 0),
    (3, 1),
    (3, 2),

)

surfaces_triangle = (
    (0, 1, 2),  # surface connecting node 0,1,2
    (0, 1, 3),
    (0, 2, 3),
    (1, 2, 3)
)

# colours
colors = (

    # DIFFERENT COLOURS ON EACH PHASE
    (0.714, 0.839, 0.89),  # b6d6e3 -> pretty blue
    (0.612, 0.925, 0.357),  # 9CEC5B
    (0.843, 0.992, 0.925),  # D7FDEC
    (0.663, 0.984, 0.843),  # A9FBD7
    (0.698, 0.894, 0.859),  # B2E4DB
    (0.690, 0.776, 0.808),  # B0C6CE
    (0, 0, 1),  # blue

)


# making our cube
def Cube():
    glBegin(GL_QUADS)

    # FRONT
    glColor3f(0.808, 0.259, 0.341)  # CE4247 CHERRY RED
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    # TOP
    glColor3f(1.0, 0.498, 0.318)  # FF7F51 REDISH ORANGE
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)

    # LEFT SIDE
    glColor3f(0.447, 0.0, 0.149)  # 720026 BURGUNDY
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)

    # RIGHT SIDE
    glColor3f(0.31, 0.0, 0.043)  # 4F000B DARK RED
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)

    # BOTTOM
    glColor3f(1.0, 0.608, 0.329)  # FF9B54 LIGHT ORANGE
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)

    # BACK
    # glColor3f(0.663, 0.984, 0.843)  # A9FBD7 -> MAGIC MINT
    glColor3f(0.576, 0.545, 0.631)  # 938BA1 -> COOL GREY
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)

    glEnd()


def Triangle():
    glBegin(GL_TRIANGLES)

    # BOTTOM
    # glColor3f(0.714, 0.839, 0.89)  # b6d6e3
    # glColor3f(1.0, 0.867, 0.29) #FFD4A YELLOW
    glColor3f(0.38, 0.518, 0.847)  # 6184D8
    glVertex3f(-1.0, 0.0, 1.0)
    glVertex3f(-1.0, 0.0, -1.0)
    glVertex3f(1.0, 0.0, 0.0)

    # LEFT
    # glColor3f(0.612, 0.925, 0.357)  # 9CEC5B
    # glColor3f(0.996, 0.565, 0.0) #FE900 ORANGE
    glColor3f(0.612, 0.925, 0.357)  # 9CEC5B
    glVertex3f(-1.0, 0.0, 1.0)
    glVertex3f(-1.0, 0.0, -1.0)
    glVertex3f(0.0, 3.0, 0.0)

    # FRONT
    # glColor3f(0.843, 0.992, 0.925)  # D7FDEC
    # glColor3f(0.353, 0.859, 1.0) #5ADBFF BLUE
    glColor3f(0.314, 0.773, 0.718)  # 50CB7
    glVertex3f(-1.0, 0.0, 1.0)
    glVertex3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 3.0, 0.0)

    # RIGHT
    # glColor3f(0.663, 0.984, 0.843),  # A9FBD7
    glColor3f(0.235, 0.412, 0.592)  # 3C6997 GREY BLUE
    glVertex3f(-1.0, 0.0, -1.0)
    glVertex3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 3.0, 0.0)

    glEnd()


# def main():
if __name__ == "__main__":
    global changeCount
    global currentShape
    global currentMatrix
    global angle
    angle = 0

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
    glViewport(0, 0, display[0], display[1])
    glTranslatef(0, 0, -10)  # x-y-z parameters, us moving about the objet
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
                    angle = 0

        if gesture == "up":
            if angle == 30 or angle == -330:
                glTranslatef(-0.5, math.sqrt(3) / 2, 0)
                print("GESTURE ", gesture)
            elif angle == 60 or angle == -300:
                glTranslatef(-math.sqrt(3) / 2, 0.5, 0)
                print("GESTURE ", gesture)
            elif angle == 90 or angle == -270:
                glTranslatef(-1, 0, 0)
                print("GESTURE ", gesture)
            elif angle == 120 or angle == -240:
                glTranslatef(-math.sqrt(3) / 2, -0.5, 0)
                print("GESTURE ", gesture)
            elif angle == 150 or angle == -210:
                glTranslatef(-0.5, -math.sqrt(3) / 2, 0)
                print("GESTURE ", gesture)
            elif angle == 180 or angle == -180:
                glTranslatef(0, -1, 0)
                print("GESTURE ", gesture)
            elif angle == 210 or angle == -150:
                glTranslatef(0.5, -math.sqrt(3) / 2, 0)
                print("GESTURE ", gesture)
            elif angle == 240 or angle == -120:
                glTranslatef(math.sqrt(3) / 2, -0.5, 0)
                print("GESTURE ", gesture)
            elif angle == 270 or angle == -90:
                glTranslatef(1, 0, 0)
                print("GESTURE ", gesture)
            elif angle == 300 or angle == -60:
                glTranslatef(math.sqrt(3) / 2, 0.5, 0)
                print("GESTURE ", gesture)
            elif angle == 330 or angle == -30:
                glTranslatef(0.5, math.sqrt(3) / 2, 0)
                print("GESTURE ", gesture)
            else:
                glTranslatef(0, 1, 0)
                print("GESTURE ", gesture)

        elif gesture == "down":
            if angle == 30 or angle == -330:
                glTranslatef(0.5, -math.sqrt(3) / 2, 0)
                print("GESTURE ", gesture)
            elif angle == 60 or angle == -300:
                glTranslatef(math.sqrt(3) / 2, -0.5, 0)
                print("GESTURE ", gesture)
            elif angle == 90 or angle == -270:
                glTranslatef(1, 0, 0)
                print("GESTURE ", gesture)
            elif angle == 120 or angle == -240:
                glTranslatef(math.sqrt(3) / 2, 0.5, 0)
                print("GESTURE ", gesture)
            elif angle == 150 or angle == -210:
                glTranslatef(0.5, math.sqrt(3) / 2, 0)
                print("GESTURE ", gesture)
            elif angle == 180 or angle == -180:
                glTranslatef(0, 1, 0)
                print("GESTURE ", gesture)
            elif angle == 210 or angle == -150:
                glTranslatef(-0.5, math.sqrt(3) / 2, 0)
                print("GESTURE ", gesture)
            elif angle == 240 or angle == -120:
                glTranslatef(-math.sqrt(3) / 2, 0.5, 0)
                print("GESTURE ", gesture)
            elif angle == 270 or angle == -90:
                glTranslatef(-1, 0, 0)
                print("GESTURE ", gesture)
            elif angle == 300 or angle == -60:
                glTranslatef(-math.sqrt(3) / 2, -0.5, 0)
                print("GESTURE ", gesture)
            elif angle == 330 or angle == -30:
                glTranslatef(-0.5, -math.sqrt(3) / 2, 0)
                print("GESTURE ", gesture)
            else:
                glTranslatef(0, -1, 0)
                print("GESTURE ", gesture)

        elif gesture == "left":
            if angle == 30 or angle == -330:
                glTranslate(-math.sqrt(3) / 2, -0.5, 0)
                print("GESTURE ", gesture)
            elif angle == 60 or angle == -300:
                glTranslate(-0.5, -math.sqrt(3) / 2, 0)
                print("GESTURE ", gesture)
            elif angle == 90 or angle == -270:
                glTranslate(0, -1, 0)
                print("GESTURE ", gesture)
            elif angle == 120 or angle == -240:
                glTranslatef(0.5, -math.sqrt(3) / 2, 0)
                print("GESTURE ", gesture)
            elif angle == 150 or angle == -210:
                glTranslatef(math.sqrt(3)/2, -0.5, 0)
                print("GESTURE ", gesture)
            elif angle == 180 or angle == -180:
                glTranslatef(1, 0, 0)
                print("GESTURE ", gesture)
            elif angle == 210 or angle == -150:
                glTranslatef(math.sqrt(3) / 2, 0.5, 0)
                print("GESTURE ", gesture)
            elif angle == 240 or angle == -120:
                glTranslatef(0.5, math.sqrt(3) / 2, 0)
                print("GESTURE ", gesture)
            elif angle == 270 or angle == -90:
                glTranslatef(0, 1, 0)
                print("GESTURE ", gesture)
            elif angle == 300 or angle == -60:
                glTranslatef(-0.5, math.sqrt(3) / 2, 0)
                print("GESTURE ", gesture)
            elif angle == 330 or angle == -30:
                glTranslatef(-math.sqrt(3)/2, 0.5, 0)
                print("GESTURE ", gesture)
            else:
                glTranslate(-1, 0, 0)
                print("GESTURE ", gesture)

        elif gesture == "right":
            if angle == 30 or angle == -330:
                glTranslate(math.sqrt(3)/2, 0.5, 0)
                print("GESTURE ", gesture)
            elif angle == 60 or angle == -300:
                glTranslate(0.5, math.sqrt(3)/2, 0)
                print("GESTURE ", gesture)
            elif angle == 90 or angle == -270:
                glTranslate(0, 1, 0)
                print("GESTURE ", gesture)
            elif angle == 120 or angle == -240:
                glTranslatef(-0.5, math.sqrt(3)/2, 0)
                print("GESTURE ", gesture)
            elif angle == 150 or angle == -210:
                glTranslatef(-math.sqrt(3)/2, 0.5, 0)
                print("GESTURE ", gesture)
            elif angle == 180 or angle == -180:
                glTranslatef(-1, 0, 0)
                print("GESTURE ", gesture)
            elif angle == 210 or angle == -150:
                glTranslatef(-math.sqrt(3)/2, -0.5, 0)
                print("GESTURE ", gesture)
            elif angle == 240 or angle == -120:
                glTranslatef(-0.5, -math.sqrt(3)/2, 0)
                print("GESTURE ", gesture)
            elif angle == 270 or angle == -90:
                glTranslatef(0, -1, 0)
                print("GESTURE ", gesture)
            elif angle == 300 or angle == -60:
                glTranslatef(0.5, -math.sqrt(3)/2, 0)
                print("GESTURE ", gesture)
            elif angle == 330 or angle == -30:
                glTranslatef(math.sqrt(3)/2, -0.5, 0)
                print("GESTURE ", gesture)
            else:
                glTranslate(1, 0, 0)
                print("GESTURE ", gesture)

        elif gesture == "clock":
            angle += 30
            glRotatef(30, 0, 0, -1)  # only x
            print("GESTURE ", gesture)
        elif gesture == "counter":
            angle -= 30
            glRotatef(30, 0, 0, 1)  # only x
            print("GESTURE ", gesture)

        if angle == 360 or angle == -360:
            angle = 0

        # FOR WHEN WE HAVE ALL GESTURES
        elif gesture == "snap":
            changeCount = changeCount + 1
            print("GESTURE ", gesture)
        # elif gesture == "pinch_in":
        #     glTranslatef(0, 0, 1)
        #     print("GESTURE ", gesture)
        # elif gesture == "pinch_out":
        #     glTranslatef(0, 0, -1)
        #     print("GESTURE ", gesture)
        elif gesture == "ignore":
            print("GESTURE ", gesture)
        gesture = ""

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glClearColor(1, 1, 1, 1)  # white -> POSSIBILITY

        glClear(GL_COLOR_BUFFER_BIT)

        # Changing Shapes
        if changeCount % 2 != 0:
            Triangle()
            currentShape = 'Triangle'
        elif changeCount % 2 == 0:
            Cube()
            currentShape = 'Cube'

        pygame.display.flip()  # an alternative could be display.update()
        pygame.time.wait(10)  # in ms