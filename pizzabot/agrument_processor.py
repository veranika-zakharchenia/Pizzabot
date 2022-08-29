import re
from typing import List, Tuple

from pizzabot.point import Point


class ArgumentProcessor:
    def __init__(self, arguments: str):
        self.arguments = arguments

    def _process_grid(self) -> Tuple:
        """
        retrieve and validate grid value
        :return: grid size
        """
        grid = re.match(r'^(\d+)x(\d+)', self.arguments)

        if not grid:
            raise AttributeError('Grid size is not specified.')

        x, y = grid.groups()
        grid_size = (int(x), int(y))

        if grid_size == (0, 0):
            raise AttributeError('Grid size is not valid.')

        return grid_size

    def _process_coordinates(self, grid_size: Tuple) -> List[Tuple]:
        """
        retrieve and validate coordinates values
        :param grid_size: is needed to check if coordinate suits the grid
        :return: coordinates
        """
        coordinates = re.findall(r'(?:\((\d+),\s*(\d+)\))+?', self.arguments)

        if len(coordinates) == 0:
            raise AttributeError('No coordinates found.')

        for coordinate in coordinates:
            coordinate_tuple = tuple(int(item) for item in coordinate)
            if not all(grid_edge > coordinate for grid_edge, coordinate in zip(grid_size, coordinate_tuple)):
                raise AttributeError('Points are not suit the grid.')

        return coordinates

    def _create_points(self, coordinates: List[Tuple]) -> List[Point]:
        points = []

        for coordinate in coordinates:
            point = Point(*coordinate)
            points.append(point)

        return points

    def get_points(self) -> List[Point]:
        grid = self._process_grid()
        coordinates = self._process_coordinates(grid)
        points = self._create_points(coordinates)

        return points
