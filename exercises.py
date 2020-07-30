import sys
import collections

def is_anagram(s1, s2):
    """
    Write an algorithm that returns whether s1 and s2 are anagrams of each other, i.e.
    if s1 and s2 contain the same letters in a possibly different order.
    E.g.: "abc" and "cab" are anagrams, "aab" and "bba" are not.
    :param s1: string
    :param s2: string
    :return: True or False
    """

    try:
        # check s1 and s2 length
        if len(s1) == len(s2):
            # create a lists for s1 and s2
            list_s1 = sorted(s1)
            list_s2 = sorted(s2)
            # compare list_string_one and list_string_two
            return True if list_s1 == list_s2 else False
        else:
            return False
    except TypeError as e:
        print("Program stopped. {}: Values aren't both str -> {}.".format(type(e), e))
        sys.exit(1)


def check_parenthesis_consistency(string):
    """
    Write an algorithm that determines if the parenthesis (round brackets "()") in a string are properly balanced.
    An expression is said to be properly parenthesised if it has the form "(p)" or "pq", where p and q are
    properly parenthesised expressions. Any string (including an empty string) that does not contain any parenthesis
    is properly parenthesised.
    E.g.: "()()" is properly parenthesised, "(()" is not.
    :param string: the string to analyse.
    :return: True if the parentheses are balanced, False if not.
    """

    try:
        start_char = '('
        end_char = ')'
        # compare number of chars '(' and ')' in string
        if string.count(start_char) == string.count(end_char):
            counter = 0
            for char in string:
                if char == start_char:
                    counter += 1
                if char == end_char:
                    counter -= 1
                if counter < 0:
                    return False
             return True if counter == 0 else False
         else:
             return False
    except TypeError as e:
        print("Program stopped. {}: Value isn't str -> {} is {}.".format(type(e), e, type(string)))
        sys.exit(1)


def shortest_path(start, end, maze):
    """
    Write an algorithm that finds the shortest path in a maze from start to end
    The maze is represented by a list of lists containing 0s and 1s:
    0s are walls, paths cannot go through them
    The only movements allowed are UP/DOWN/LEFT/RIGHT
    :param start: tuple (x_start, y_start) - the starting point
    :param end: tuple (x_end, y_end) - the ending point
    :param maze: list of lists - the maze
    :return: list of positions [(x1, y1), (x2, y2), ...] representing the shortest path in the maze
    """

    # define row and column size
    x_size = len(maze)
    y_size = len(maze[0])
    # define a list-like container starting with list of start tuple
    queue = collections.deque([[start]])
    # define a set of data starting with start tuple
    seen = set([start])
    # create a list including all found path
    path_list = list()
    while queue:
        # for first iteration -> init path with list containing start tuple
        # then replace it by list of path tuples
        path = queue.popleft()
        path_list.append(path)
        if path == end:
            return path_list
        # get the last tuple in path
        x, y = path[-1]
        # scan and assign x and y with possible values
        for x_coord, y_coord in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            # avoid IndexError
            if 0 <= x_coord < x_size and 0 <= y_coord < y_size:
                # avoid walls and already met tuples
                if maze[x_coord][y_coord] != 0 and (x_coord, y_coord) not in seen:
                    queue.append(path + [(x_coord, y_coord)])
                    seen.add((x_coord, y_coord))
    pass
