import glob
import os
import sys
import random
import time
import numpy as np
import cv2
import math
import time

try:
    sys.path.append(glob.glob('../../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        5,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla



def draw_points(drawing_material,map,seconds,color_array = [0,255,0],option=1):
    if(option == 1):
        for idx, w in enumerate(drawing_material):
            #about the point different , the location not like the waypoints
            world.debug.draw_string(w.location, '0 {}'.format(idx), draw_shadow=False,color=carla.Color(r=color_array[0], g=color_array[1], b=color_array[2]),life_time=seconds,persistent_lines=True)
    else:
        world.debug.draw_string(drawing_material.location, 'O start point', draw_shadow=False,color=carla.Color(r=color_array[0], g=color_array[1], b=color_array[2]),life_time=seconds,persistent_lines=True)


if __name__ == "__main__":

    #--------------for set client , map , world , waypoints and the map-------------------
    # client = carla.Client('localhost',2000)
    client = carla.Client('10.119.184.95',2000)
    
    client.set_timeout(5)
    client.load_world('Town07')

    world = client.get_world()

    # settings = world.get_settings()
    # settings.fixed_delta_seconds = 0.05
    # world.apply_settings(settings)

    map = world.get_map()

    #-----------------------set the spectator and draw the points----------------------
    #for draw the spawn_points
    spawn_points = world.get_map().get_spawn_points()

    #for setting the spectator position and the find the actors in the world
    # actor_list = world.get_actors()

    # draw_points(spawn_points,map,900,[255,0,0],1)
    draw_points(spawn_points[32],map,900,[255,0,0],0)

    while True:
        #-----------------------create a car for obstacle----------------------
        vehicle_type = "vehicle.volkswagen.t2"
        vehicle_bp = world.get_blueprint_library().find(vehicle_type)

        actor = world.spawn_actor(vehicle_bp, spawn_points[32])
        actor.apply_control(carla.VehicleControl(brake=1.0))
        time.sleep(1800)
        actor.destroy()