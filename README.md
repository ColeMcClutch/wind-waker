Wind Waker - 3D Scene Renderer:

Overview
========


This project is a 3D scene renderer that simulates a water environment with a boat and dynamic camera controls. The program uses OpenGL for rendering and GLFW for handling user input and window management. It allows users to interact with the scene using mouse and keyboard inputs, and includes features like camera zoom, rotation, and the movement of water waves.

The renderer makes use of shaders, meshes, and transformations to display the scene. A camera system is implemented to allow the user to move and rotate the view around the scene interactively.

Features:
=========

- 3D Camera Controls: Users can zoom in and out and rotate the camera to view the scene from different angles.
- Water and Boat Meshes: The scene includes dynamic water with ripples and a boat that can be rendered in the environment.
- Lighting: Directional light is applied to the scene to simulate realistic shading.
- Interactive Input: Arrow keys and mouse controls are used to modify the camera position and orientation.
- Multisampling: The renderer uses 4x multisampling to enhance the quality of the rendered image.

Requirements:
=============

- Python 3.x
- OpenGL
- GLFW
- PyGLM
- Custom modules (helpers.py, water.py, camera.py, boat.py)