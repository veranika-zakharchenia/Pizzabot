class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = int(x)
        self.y = int(y)

    def __iter__(self):
        yield self.x, self.y

