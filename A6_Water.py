#Include statements
from OpenGL.GL import *
import glfw
import glm
from helpers import *
from water import Water
from camera import Camera
from boat import Boat


# Initialize glfw
glfw.init() 
glfw.window_hint(glfw.SAMPLES, 4)  # Enable 4x multisampling

# Set context version required for shaders and VAOs
glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)  # For MacOS
glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

# Open a window and create its OpenGL context
screen_width = 1000 #screen width
screen_height = 800 #screen height


#Create window with title 'Wind Waker'
window = glfw.create_window(screen_width, screen_height, "Wind Waker", None, None)
glfw.make_context_current(window)

# Create mesh objects
water = Water(-10.0, 10.0, 1.0)
boat = Boat()

# Define matrices
#Define the perspective
P = glm.perspectiveFov(glm.radians(45.0), screen_width, screen_height, 0.001, 1000.0)
#Define M
M = glm.mat4(1.0)  

# Initialize camera
center = glm.vec3(5.0, 5.0, 5.0)   # Camera position
eye = glm.vec3(0.0, 0.0, 0.0)      # Camera look direction
up = glm.vec3(0.0, 1.0, 0.0)       # Direction of up

camera = Camera(center, eye, up)


# Define direction of light source
light_direction = glm.vec3(5.0, 30.0, 5.0)


# Ensure we can capture the escape key being pressed
glfw.set_input_mode(window, glfw.STICKY_KEYS, GL_TRUE)

# Ensure depth is determined correctly
glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LESS)


# Initialize variables
time = 0        # Used to make the waves ripple
x_press = None  # Location mouse was first clicked
y_press = None
dx = 0          # Distance mouse was dragged in each direction
dy = 0
dr = 0          # Proportional to time arrow key is held. Sign indicates direction


# Render loop, runs until esc is clicked
while (glfw.get_key(window, glfw.KEY_ESCAPE) != glfw.PRESS and not glfw.window_should_close(window)):  
    # Clear buffers and set background color
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.2, 0.2, 0.3, 0.0)  # Dark blue
    

    # Increment time
    time += 0.01

    #Poll for events
    glfw.poll_events()  

    # Process up and down arrow key presses
    #UP Key Zoom In
    if (glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS):  
        dr -= 0.01  
    #Zoom out when holding down key
    elif (glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS):  
        dr += 0.01  
    #Hold still if no key is clicked
    else:  
        dr = 0   

    # Process mouse click and drag
    mouse_left_state = glfw.get_mouse_button(window, glfw.MOUSE_BUTTON_LEFT)
    if (mouse_left_state == glfw.PRESS):  # Detect if left mouse button is clicked

        # Get location clicked
        x_cursor, y_cursor = glfw.get_cursor_pos(window)

        if x_press is None:  # On the first frame mouse is clicked
            x_press = x_cursor  # Save location where mouse was first clicked
            y_press = y_cursor

        # Calculate distance between initial location clicked and position dragged to
        dx = x_cursor - x_press
        dy = y_cursor - y_press

        # Save the dragged cursor positon so it can be calculated in the next frame
        x_press = x_cursor
        y_press = y_cursor

    elif (mouse_left_state == glfw.RELEASE):  # Detect if Left mouse button is released
        x_press = None    # Reset the clicked location
        y_press = None
        dx = 0            
        dy = 0


    # Adjust camera position
    camera.zoomRadius(dr)            # Modify radius based on arrow press
    camera.rotateTheta(0.005 * dx)   # Modify theta based on horizontal drag motion
    camera.rotatePhi(-0.005 * dy)    # Modify phi based on vertical drag motion

    # Set view matrix to use new camera position
    V = glm.lookAt(camera.getCenter(), camera.getEye(), camera.getUp())

    # Calculate model view projection matrix (MVP)
    MVP = P * V * M

    # Render each mesh
    water.draw(MVP, V, M, time, light_direction) #Draw the water
    boat.draw(MVP, time) #Draw the boat

    # Swap buffers
    glfw.swap_buffers(window)
    glfw.poll_events()


# Close OpenGL window and terminate GLFW
glfw.terminate()
