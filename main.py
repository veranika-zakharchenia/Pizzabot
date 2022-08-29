import sys

from pizzabot.agrument_processor import ArgumentProcessor
from pizzabot.delivery import Delivery

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            raise AttributeError('No arguments passed. Example: "5x5 (1, 3) (4, 4)"')

        argument_processor = ArgumentProcessor(sys.argv[1])
        points = argument_processor.get_points()
        delivery = Delivery(points)
        path = delivery.get_instructions()

        print(path)
    except AttributeError as error:
        print(f'Attribute error: {error}')
    except ValueError as error:
        print(f'Value error: {error}')
    except Exception as error:
        print(f'Unexpected error: {error}')