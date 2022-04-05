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
    # GHAITH COLOURS -> OLD CUBE
    # (1, 1, 0),  # yellow
    # (0, 1, 0),  # green
    # (0.75, 0.38, 0),  # Orange
    # (1, 1, 1),  # white
    # (0.9, 0, 0),  # Red
    # (0, 0, 1)  # Blue
    ########

    # DIFFERENT COLOURS ON EACH PHASE
    # (1, 0, 1),
    # (1, 1, 0),
    # (0, 1, 1),
    # (1, 0, 0),
    # (0, 0, 1),
    # (0, 1, 0),
    # (1, 1, 1),
    # (1, 0, 0), # red
    # (1, 0, 0), # red
    (0.714, 0.839, 0.89),  # b6d6e3 -> pretty blue
    (0.612, 0.925, 0.357),  # 9CEC5B
    (0.843, 0.992, 0.925),  # D7FDEC
    (0.663, 0.984, 0.843),  # A9FBD7
    (0.698, 0.894, 0.859),  # B2E4DB
    (0.690, 0.776, 0.808),  # B0C6CE
    (0, 0, 1),  # blue
    # (0.576, 0.545, 0.631),   # 938BA1

)


# making our cube
def Cube():
    glBegin(GL_QUADS)

    # FRONT
    # glColor3f(0.843, 0.992, 0.925) # D7FDEC
    #glColor3f(0.729, 0.843, 0.949)  # BAD7F2 -> BEAU BLUE
    #glColor3f(0.898, 0.596, 0.608)  # E5989B -> PASTEL PINK
    # glColor3f(0.537, 0.631, 0.937)  #89A1EF -> CORNFLOWER BLUE
    #glColor3f(0.969, 0.133, 0.082)  #red mexican fiesta
    glColor3f(0.808, 0.259, 0.341)  # CE4247 CHERRY RED
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    # TOP
    # glColor3f(0.714, 0.839, 0.89) #b6d6e3
    #glColor3f(0.949, 0.729, 0.788)  # F2BAC9 ->ORCHID PINK
    #glColor3f(0.71, 0.514, 0.553)  #B5838D ->ENGLISH LAVENDER
    # glColor3f(0.937, 0.612, 0.855) #EF9CDA -> ORCHID CRAYOLA
    #glColor3f(0.11, 0.69, 0.831)  # blue mexican fiesta
    glColor3f(1.0, 0.498, 0.318)  # FF7F51 REDISH ORANGE
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)

    # LEFT SIDE
    # glColor3f(0.698, 0.894, 0.859),  # B2E4DB -> MIDDLE BLUE GREEN
    #glColor3f(0.729, 0.949, 0.914)  # BAF2E9  -> CELESTE
    #glColor3f(0.427, 0.408, 0.459)  # 6D6875 -> OLD LAVENDER
    # glColor3f(0.0, 0.647, 0.878)  #00A5E0 -> CAROLINA BLUE
    #glColor3f(0.627, 0.769, 0.035)  # green mexican fiesta
    glColor3f(0.447, 0.0, 0.149)  # 720026 BURGUNDY
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)

    # RIGHT SIDE
    # glColor3f(0.690, 0.776, 0.808),  # B0C6CE
    #glColor3f(0.949, 0.886, 0.729)  # F2E2BA -> DUTCH WHITE
    #glColor3f(1.0, 0.706, 0.635)  # FFB4A2 -> MELON
    # glColor3f(0.996, 0.808, 0.945)  #FECEF1 -> PINK LACE
    #glColor3f(1.0, 0.831, 0.224)  # yellow mexican fiesta
    glColor3f(0.31, 0.0, 0.043)  # 4F000B DARK RED
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)

    # BOTTOM
    # glColor3f(0.612, 0.925, 0.357)  # 9CEC5B
    # glColor3f(0.69, 0.949, 0.706)  # B0F2B4-> GRANNY SMITH APPLE
    #glColor3f(1.0, 0.804, 0.698) #FFCDB2 -> APRICOT
    # glColor3f(0.196, 0.796, 1.0)  #32CBFF -> VIVID SKY BLUE
    #glColor3f(0.98, 0.643, 0.02)  # orange mexican fiesta
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

    #BOTTOM
    #glColor3f(0.714, 0.839, 0.89)  # b6d6e3
    #glColor3f(1.0, 0.867, 0.29) #FFD4A YELLOW
    glColor3f(0.38, 0.518, 0.847)  #6184D8
    glVertex3f(-1.0, 0.0, 1.0)
    glVertex3f(-1.0, 0.0, -1.0)
    glVertex3f(1.0, 0.0, 0.0)

    #LEFT
    #glColor3f(0.612, 0.925, 0.357)  # 9CEC5B
    #glColor3f(0.996, 0.565, 0.0) #FE900 ORANGE
    glColor3f(0.612, 0.925, 0.357)  #9CEC5B
    glVertex3f(-1.0, 0.0, 1.0)
    glVertex3f(-1.0, 0.0, -1.0)
    glVertex3f(0.0, 3.0, 0.0)

    #FRONT
    #glColor3f(0.843, 0.992, 0.925)  # D7FDEC
    #glColor3f(0.353, 0.859, 1.0) #5ADBFF BLUE
    glColor3f(0.314, 0.773, 0.718)  #50CB7
    glVertex3f(-1.0, 0.0, 1.0)
    glVertex3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 3.0, 0.0)

    #RIGHT
    #glColor3f(0.663, 0.984, 0.843),  # A9FBD7
    glColor3f(0.235, 0.412, 0.592) #3C6997 GREY BLUE
    glVertex3f(-1.0, 0.0, -1.0)
    glVertex3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 3.0, 0.0)

    glEnd()


# def main():
if __name__ == "__main__":
    global changeCount
    global currentShape
    global currentMatrix

    # variable for clockwise
    global clockX
    clockX = 0

    # variable for counter
    global counterClockX
    counterClockX = 0


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
                    counterClockX = 0
                    clockX = 0

        if gesture == "up":
            if clockX == 0 & counterClockX == 0:
                glTranslatef(0, 1, 0)
                print("GESTURE ", gesture)

                # If it was Clockwise
            elif clockX != 0 & clockX % 30 == 0:
                print("------------------------TEST CLOCK--------------------------")
                glRotatef(clockX, 0, 0, 1)  # turns it counter
                glTranslatef(0, 1, 0)  # up
                glRotatef(clockX, 0, 0, -1)  # turns it back to clockwise
                print("GESTURE ", gesture)

           # elif counterX == 30 | counterX == 60 | counterX == 90 | counterX == 120:
            # If it was Counter
            elif counterClockX != 0 & counterClockX % 30 == 0:
                print("------------------------TEST COUNTER--------------------------")
                glRotatef(counterClockX, 0, 0, -1)   # turns it clockwise
                glTranslatef(0, 1, 0)   # up
                glRotatef(counterClockX, 0, 0, +1)    # turns it back to counter
                print("GESTURE ", gesture)




        elif gesture == "down":
            if clockX == 0 & counterClockX == 0:
                glTranslatef(0, -1, 0)
                print("GESTURE ", gesture)

                # elif counterX == 30 | counterX == 60 | counterX == 90 | counterX == 120:
            elif counterClockX != 0 & counterClockX % 30 == 0:
                glRotatef(counterClockX, 0, 0, -1)  # turns it clockwise
                glTranslatef(0, -1, 0)  # Down
                glRotatef(counterClockX, 0, 0, 1)  # turns it back to counter
                print("GESTURE ", gesture)

                # elif clockX == 30:
            elif clockX != 0 & clockX % 30 == 0:
                glRotatef(clockX, 0, 0, 1)  # turns it counter
                glTranslatef(0, -1, 0)  # Down
                glRotatef(clockX, 0, 0, -1)  # turns it back to clockwise
                print("GESTURE ", gesture)


        elif gesture == "left":
            if clockX == 0 & counterClockX == 0:
                glTranslatef(-1, 0, 0)
                print("GESTURE ", gesture)

                # elif counterX == 30 | counterX == 60 | counterX == 90 | counterX == 120:
            elif counterClockX != 0 & counterClockX % 30 == 0:
                glRotatef(counterClockX, 0, 0, -1)  # turns it clockwise
                glTranslatef(-1, 0, 0)  # Left
                glRotatef(counterClockX, 0, 0, 1)  # turns it back to counter
                print("GESTURE ", gesture)

                # elif clockX == 30:
            elif clockX != 0 & clockX % 30 == 0:
                glRotatef(clockX, 0, 0, 1)  # turns it counter
                glTranslatef(-1, 0, 0)  # Left
                glRotatef(clockX, 0, 0, -1)  # turns it back to clockwise
                print("GESTURE ", gesture)


        elif gesture == "right":
            if clockX == 0 & counterClockX == 0:
                glTranslatef(1, 0, 0)
                print("GESTURE ", gesture)

            elif counterClockX != 0 & counterClockX % 30 == 0:
                glRotatef(counterX, 0, 0, -1)  # turns it clockwise
                glTranslatef(1, 0, 0)  # Right
                glRotatef(counterX, 0, 0, 1)  # turns it back to counter
                print("GESTURE ", gesture)

                # elif clockX == 30:
            elif clockX != 0 & clockX % 30 == 0:
                glRotatef(clockX, 0, 0, 1)  # turns it counter
                glTranslatef(1, 0, 0)  # Right
                glRotatef(clockX, 0, 0, -1)  # turns it back to clockwise
                print("GESTURE ", gesture)


        elif gesture == "clock":
            clockX += 30
            if counterClockX > 0:
                #counterClockX -= 30
                counterClockX = 0
            # glRotatef(25, -1, -1, -1) #all axis
            # glRotatef(30, 0, -1, 0)  # only y
            glRotatef(30, 0, 0, -1)  # only x
            # glRotatef(30, 0, -1, 0)  # only y
            print("GESTURE ", gesture)

        elif gesture == "counter":
            counterClockX += 30
            if clockX > 0:
                #clockX -= 30
                clockX = 0
            # glRotatef(25, 1, 1, 1) #all axis
            glRotatef(30, 0, 0, 1)  # only x
            # glRotatef(30, 0, 1, 0)  # only y
            print("GESTURE ", gesture)

        elif gesture == "reset":
            resetShape()
            counterClockX = 0
            clockX = 0
            print("GESTURE ", gesture)

        # FOR WHEN WE HAVE ALL GESTURES
        elif gesture == "snap":
            changeCount = changeCount + 1
            print("GESTURE ", gesture)
        elif gesture == "pinch_in":
            glTranslatef(0, 1.0, 1.0)
            print("GESTURE ", gesture)
        elif gesture == "pinch_out":
            glTranslatef(0, 0, -1.0)
            print("GESTURE ", gesture)
        gesture = ""

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # BACKGROUND COLOUR
        # glClearColor(0.7, 0.8, 0.88, 1)  # (red, green, blue, alpha)
        # glClearColor(0, 0, 0, 1) # black
        glClearColor(1, 1, 1, 1)  # white -> POSSIBILITY
        # glClearColor(0.576, 0.545, 0.631,0)  # 938BA1
        # glClearColor(0.502, 0.502, 0.502, 1) #808080 grey
        # glClearColor(0.792, 0.808, 0.812, 1) #cacecf light grey
        # glClearColor(0.753, 0.753, 0.753, 0) #C0C0C0 silver
        # glClearColor(0.753, 0.824, 0.851, 1) # c0d2d9 -> light blue: POSSIBILITY
        # glClearColor(0.953, 1, 1, 1) # f3ffff -> twilight : POSSIBILITY

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

# if __name__ == "__main__":
#     main()
