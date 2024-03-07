from os.path import dirname, join, abspath

import numpy as np
from pynput import keyboard
from pyrep import PyRep
from pyrep.robots.arms.jaco import Jaco
from pyrep.robots.end_effectors.jaco_gripper import JacoGripper
from pyrep.objects.dummy import Dummy
from pyrep.objects.shape import Shape

SCENE_FILE = join(dirname(abspath(__file__)), 'simTest2.ttt')
pr = PyRep()

pr.launch(SCENE_FILE, headless=False)
pr.start()

jaco = Jaco()
gipper = JacoGripper(0)
target = Shape('Cuboid')
current_pos = jaco.get_position()

# target = np.array([0.25, 0.25, 0.25]
# path = jaco.get_path(position=target.get_position(), quaternion=jaco.get_quaternion())
# path = agent.get_linear_path(position=pos, angle=0)
increment = 0.01


def move(key):
    if key == keyboard.Key.up:
        current_pos[1] += increment  # Move in positive Y direction
    elif key == keyboard.Key.down:
        current_pos[1] -= increment  # Move in negative Y direction
    elif key == keyboard.Key.left:
        current_pos[0] -= increment  # Move in negative X direction
    elif key == keyboard.Key.right:
        current_pos[0] += increment  # Move in positive X direction
    elif key == keyboard.KeyCode.from_char('w'):
        current_pos[2] += increment  # Move up in Z direction
    elif key == keyboard.KeyCode.from_char('s'):
        current_pos[2] -= increment  # Move down in Z direction


while True:


    path.visualize()
    path = jaco.get_path(position=current_pos, quaternion=jaco.get_quaternion())
    done = False
    while not done:
        done = path.step()
        pr.step()

    path.clear_visualization()

print('Done ...')
input('Press enter to finish ...')
pr.stop()
pr.shutdown()
