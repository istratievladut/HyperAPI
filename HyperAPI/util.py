import random
import sys
import csv
import posixpath
from HyperAPI.utils.exceptions import ApiException


class Helper:
    @staticmethod
    def try_catch(func):
        def try_catched(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ApiException:
                raise
            except Exception as e:
                print("Error during a {}'s action: {}".format(str(args[0].__class__.__name__), str(e)))
        try_catched.__doc__ = func.__doc__
        return try_catched


"""
Utils functions
"""


def safePathJoin(first_part, *other_parts):
    """Safely join paths on any platform"""

    return posixpath.join(first_part, *other_parts)


def find_csv_delimiter(filename):

    with open(filename, 'r', encoding="utf-8") as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.readline(), ',;:|\t')

    return dialect.delimiter


# Define tag colors
tag_colors_list = [
    '#003380', '#005C31', '#0075DC', '#0080FF', '#00998F', '#1AB39F', '#1B587C', '#2BCE48', '#31B6FD', '#339966',
    '#410082', '#426600',
    '#4C005C', '#4E5B6F', '#5EF1F2', '#604878', '#6187E3', '#740AFF', '#7E6BC9', '#7FD13B', '#808080', '#8F7C00',
    '#94FFB5', '#990000',
    '#993F00', '#9DCC00', '#9F2936', '#B26B02', '#C20088', '#D2DA7A', '#E0FF66', '#EA157A', '#F07F09', '#F0A3FF',
    '#F5C040', '#FADA7A',
    '#FF0010', '#FF5005', '#FF6600', '#FFA405', '#FFA8BB', '#FFCC99', '#FFE100', '#FFFF80',
]


def get_random_color():
    return random.choice(tag_colors_list)


shuffle_indices = list(range(len(tag_colors_list)))
random.shuffle(shuffle_indices)
tag_colors = [tag_colors_list[k] for k in shuffle_indices]
