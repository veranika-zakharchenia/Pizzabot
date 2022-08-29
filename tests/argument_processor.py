import pytest

from pizzabot.agrument_processor import ArgumentProcessor
from pizzabot.point import Point


class TestArgumentProcessor:
    def test_process_input__successful(self):
        argument_processor = ArgumentProcessor("5x5 (1, 3) (4, 4)")
        expected_result = [Point(1, 3), Point(4, 4)]

        actual_result = argument_processor.get_points()

        assert actual_result == expected_result

    def test_process_input__failed_out_of_grid(self):
        argument_processor = ArgumentProcessor("3x3 (1, 3) (4, 4)")

        with pytest.raises(AttributeError):
            argument_processor.get_points()

    def test_process_input__failed_not_valid_coordinate(self):
        argument_processor = ArgumentProcessor("3x3 (1, x)")

        with pytest.raises(AttributeError):
            argument_processor.get_points()

    def test_process_input__failed_not_valid_grid(self):
        argument_processor = ArgumentProcessor("3xx (1, 0)")

        with pytest.raises(AttributeError):
            argument_processor.get_points()

    def test_process_input__success_not_valid_coordinate(self):
        argument_processor = ArgumentProcessor("5x5 (1, x) (4, 4)")
        expected_result = [Point(4, 4)]

        actual_result = argument_processor.get_points()

        assert actual_result == expected_result

    def test_process_input__failed_no_coordinates(self):
        argument_processor = ArgumentProcessor("3x3 (x, y)")

        with pytest.raises(AttributeError):
            argument_processor.get_points()

    def test_process_input__failed_no_grid(self):
        argument_processor = ArgumentProcessor("(1, 0) (4, 3)")

        with pytest.raises(AttributeError):
            argument_processor.get_points()

    def test_process_input__failed_empty_input(self):
        argument_processor = ArgumentProcessor("")

        with pytest.raises(AttributeError):
            argument_processor.get_points()
