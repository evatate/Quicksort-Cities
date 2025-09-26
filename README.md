# Quicksort of Cities

This repository contains an implementation of the **quicksort algorithm** to sort a dataset of world cities by different criteria:  
- **Alphabetical name**  
- **Latitude**  
- **Population**  

The project also includes a visualization that draws the **100 most populous cities** on a world map using the CS1 graphics library.

---

## Materials Provided

- **cs1lib.py** – graphics library used for drawing cities on the map  
- **world_cities.txt** – dataset of cities (country code, name, region, population, latitude, longitude)  
- **cities_alpha.txt** – output file sorted alphabetically by city name  
- **cities_latitude.txt** – output file sorted by latitude  
- **cities_population.txt** – output file sorted by population  

---

## Core Components

### City

`city.py` defines a `City` class to store city attributes and draw them on a map.  

city = City(country_code, name, region, population, latitude, longitude)
print(city)   # -> "New York,8175133,40.7128,-74.0060"
city.draw(CX, CY)  # draws city on map

`quicksort.py` implements the **quicksort algorithm** with custom comparators.

#### Comparison Functions

* `compare_alpha(city1, city2)` – alphabetical by name  
* `compare_population(city1, city2)` – descending by population  
* `compare_latitude(city1, city2)` – ascending by latitude

#### Sort Function

`from quicksort import sort, compare_alpha`

`sort(city_list, compare_alpha)`

---

### City Driver

`city_driver.py` loads data from `world_cities.txt`, builds `City` objects, sorts them with quicksort, writes results to output files, and animates the 100 most populous cities on a world map.

#### Usage

`python3 city_driver.py`

---

## Files

* **city.py** – defines the `City` class  
* **quicksort.py** – quicksort implementation with comparators  
* **city\_driver.py** – main program: loads data, sorts, outputs files, and animates map  
* **world\_cities.txt** – input dataset  
* **cities\_alpha.txt** – output sorted alphabetically  
* **cities\_latitude.txt** – output sorted by latitude  
* **cities\_population.txt** – output sorted by population  
* **world.png** – background world map image

---

## Implementation Details

* Quicksort uses the **last element as pivot** and recursively partitions sublists.  
* Sorting is done **in-place** for efficiency.  
* Comparator functions allow sorting by different criteria without modifying the algorithm.  
* Visualization uses **CS1 graphics library** to draw circles for cities, with random colors.

---

## Limitations

* Quicksort worst-case performance is O(n²) when data is already sorted, though average case is O(n log n).  
* Visualization only draws the **100 most populous cities** to avoid clutter.  
* City positions on the map are approximated by scaling latitude and longitude.
