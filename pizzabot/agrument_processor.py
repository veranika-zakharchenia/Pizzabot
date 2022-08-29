class ArgumentProcessor:
    def __init__(self, arguments: str):
        self.arguments = arguments

    def _process_grid(self):
        pass

    def _process_coordinates(self):
        pass

    def _create_points(self):
        pass

    def get_points(self):
        self._process_grid()
        self._process_coordinates()
        self._create_points()

