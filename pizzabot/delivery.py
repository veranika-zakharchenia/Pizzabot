STARTING_POINT = (0, 0)
COMMAND_DROP = 'D'
COMMAND_EAST = 'E'
COMMAND_WEST = 'W'
COMMAND_SOUTH = 'S'
COMMAND_NORTH = 'N'

class Delivery:
    def __init__(self, points):
        self.points = points

    def _move_horizontally(self):
        pass

    def _move_vertically(self):
        pass

    def _get_intermediate_instructions(self, prev_point, current_point):
        pass

    def get_instructions(self) -> str:
        instructions = ''
        prev_point = STARTING_POINT

        for current_point in self.points:
            instructions += self._get_intermediate_instructions(prev_point, current_point)
            prev_point = current_point

        return instructions