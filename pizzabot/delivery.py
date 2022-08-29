from typing import List

from pizzabot.point import Point

STARTING_POINT = Point(0, 0)
COMMAND_DROP = 'D'
COMMAND_EAST = 'E'
COMMAND_WEST = 'W'
COMMAND_SOUTH = 'S'
COMMAND_NORTH = 'N'


class Delivery:
    def __init__(self, points: List[Point]):
        self.points = points

    def _move_horizontally(self, starting_coordinate: int, finish_coordinate: int):
        horizontal_movement = ''

        diff_x = starting_coordinate - finish_coordinate
        if diff_x > 0:
            direction_x = COMMAND_WEST
        else:
            direction_x = COMMAND_EAST

        for i in range(0, abs(diff_x)):
            horizontal_movement += direction_x

        return horizontal_movement

    def _move_vertically(self, starting_coordinate: int, finish_coordinate: int):
        vertical_movement = ''

        diff_y = starting_coordinate - finish_coordinate
        if diff_y > 0:
            direction_y = COMMAND_SOUTH
        else:
            direction_y = COMMAND_NORTH

        for i in range(0, abs(diff_y)):
            vertical_movement += direction_y

        return vertical_movement

    def _get_intermediate_instructions(self, starting_point: Point, finishing_point: Point) -> str:
        intermediate_instructions = ''

        intermediate_instructions += self._move_horizontally(starting_point.x, finishing_point.x)
        intermediate_instructions += self._move_vertically(starting_point.y, finishing_point.y)
        intermediate_instructions += COMMAND_DROP

        return intermediate_instructions

    def get_instructions(self) -> str:
        instructions = ''
        prev_point = STARTING_POINT

        for current_point in self.points:
            instructions += self._get_intermediate_instructions(prev_point, current_point)
            prev_point = current_point

        return instructions
