#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "tamekiaNelson"

import timeit
import cProfile
import pstats
import functools


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    @functools.wraps(func)
    def status(*args, **kwargs):
        pro_file = cProfile.Profile()
        pro_file.enable()
        result = func(*args, **kwargs)
        pro_file.disable()
        pro_file_status = pstats.Stats(pro_file).sort_stats('cumulative')
        pro_file_status.print_stats()
        return result
    return status


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """returns True if title is within movies list"""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False

# def find_duplicate_movies(src):
#     """Returns a list of duplicate movies from a src list"""
#     movies = read_movies(src)
#     duplicates = []
#     while movies:
#         movie = movies.pop()
#         if is_duplicate(movie, movies):
#             duplicates.append(movie)
#     return duplicates


@profile
def find_duplicate_movies_improved(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicated_movie = []
    movie_dict = {}
    for movie in movies:
        if movie in movie_dict:
            duplicated_movie.append(movie)
        else:
            movie_dict[movie] = None
    return duplicated_movie


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    # YOUR CODE GOES HERE
    t = timeit.Timer(stmt='find_duplicate_movies("movies.txt")',
                     setup='from __main__ import find_duplicate_movies',)
    number_repeats = 7
    num = 3
    result = t.repeat(repeat=number_repeats, number=num)
    timer_measurement = 'Best time across {} repeats of {} runs per repeat: {} sec'.format(
        number_repeats, num, min(result)/num)
    # print(timer_measurement)
    return timer_measurement


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies_improved('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
