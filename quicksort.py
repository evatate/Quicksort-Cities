# Filename: quicksort.py
# Author: Eva Tate
# Course: CS1
# Date: November 1, 2023
# Purpose: To create a quicksort algorithm that sorts a list in order

from city import City

# Function swaps chosen value into its place in list and returns its index
def partition(the_list, p, r, compare_func):
    pivot = the_list[r]  # chosen item to place
    i = p - 1  # goes up until items less than or equal to the pivot
    j = p  # goes to the end of the list with items greater than the pivot

    # compares each item to pivot and swaps those less than the pivot to before the pivot
    for k in range(p, r):
        if compare_func(the_list[j], pivot):
            i += 1
            temp = the_list[i]
            the_list[i] = the_list[j]
            the_list[j] = temp
        j += 1

    # swaps the pivot into the index found by the loop
    temp = the_list[i + 1]
    the_list[i + 1] = the_list[r]
    the_list[r] = temp

    return i + 1


def compare_alpha(city1, city2):
    return city1.name.lower() <= city2.name.lower()


def compare_population(city1, city2):
    return city2.population <= city1.population


def compare_latitude(city1, city2):
    return city1.latitude <= city2.latitude


def quicksort(the_list, p, r, compare_func):

    # base case: ends call when sublist has fewer than two items
    if len(the_list[p : r + 1]) < 2:
        return

    # partitions sublist, stores index in q, and calls quicksort for both halves of list
    else:
        q = partition(the_list, p, r, compare_func)
        quicksort(the_list, p, q - 1, compare_func)
        quicksort(the_list, q + 1, r, compare_func)


# sorts list by calling quicksort
def sort(the_list, compare_func):
    quicksort(the_list, 0, len(the_list) - 1, compare_func)