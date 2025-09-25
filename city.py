# Filename: city.py
# Author: Eve Tate
# Course: CS1
# Date: October 30, 2023
# Purpose: Creates City class which returns a string if printed and draws a circle
# on a map image representing the city

from cs1lib import *
from random import randint

RAD = 4  # sets radius of circle representing the city

class City:
    def __init__(self, country_code, name, region, population, latitude, longitude):

        # information about the city
        self.country_code = country_code
        self.name = name
        self.region = region
        self.population = population
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return str(self.name) + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude)

    def draw(self, cx, cy):
        # scales latitude and longitude to the size of the image
        px = cx + self.longitude * 2
        py = cy - self.latitude * 2

        # draws circle representing city on the map image
        disable_stroke()
        set_fill_color(randint(0, 1), randint(0, 1), randint(0, 1))  # random color
        draw_circle(px, py, RAD)