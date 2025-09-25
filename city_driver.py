# Filename: city_driver.py
# Author: Eve Tate
# Course: CS1
# Date: October 30, 2023
# Purpose: Creates a list of each city in the file "world_cities.txt" and sorts the list
# in different ways, writing the output files "cities_alpha.txt", "cities_population.txt"
# and "cities_latitude.txt" and then creates animation drawing most populous 100 cities on a map

from cs1lib import *
from city import City
from quicksort import *

IMAGE_WIDTH = 720
IMAGE_HEIGHT = 360

# finds center of image
CX = IMAGE_WIDTH // 2
CY = IMAGE_HEIGHT // 2

city_list = []

# opens the file and reads it
file = open('world_cities.txt', 'r')
for line in file:

    # creates list of items separated by commas in each line of file
    city_info = line.strip().split(',')

    # breaks apart list of city information
    country_code = city_info[0]
    name = city_info[1]
    region = city_info[2]
    population = city_info[3]
    latitude = city_info[4]
    longitude = city_info[5]

    # converts string values
    population = int(population)
    latitude = float(latitude)
    longitude = float(longitude)

    # creates City object and appends it into list of cities
    city = City(country_code, name, region, population, latitude, longitude)
    city_list.append(city)

# sorts list by alphabetical city names and writes list in empty file
sort(city_list, compare_alpha)
output_file = open('cities_alpha.txt', 'w')
for city in city_list:
    output_file.write(str(city) + '\n')

# sorts list by latitude and writes list in empty file
sort(city_list, compare_latitude)
output_file = open('cities_latitude.txt', 'w')
for city in city_list:
    output_file.write(str(city) + '\n')

# sorts list by population and writes list in empty file
sort(city_list, compare_population)
output_file = open('cities_population.txt', 'w')
for city in city_list:
    output_file.write(str(city) + '\n')

img = load_image('world.png')  # loads image of the map
curr_city_index = 0  # index of city being animated

def main_draw():
    global curr_city_index

    # clears screen and sets map image as background
    if curr_city_index == 0:
        clear()
        draw_image(img, 0, 0)

    # draws most populous 100 cities in city list on map
    if curr_city_index < 100:
        city = city_list[curr_city_index]
        city.draw(CX, CY)
        curr_city_index += 1


start_graphics(main_draw, width=IMAGE_WIDTH, height=IMAGE_HEIGHT, framerate=5)