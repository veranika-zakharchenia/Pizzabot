from pizzabot.delivery import Delivery
from pizzabot.point import Point


class TestDelivery:
    def test_get_route__successful(self):
        expected_result = "ENNNDEEEND"

        delivery = Delivery([Point(1, 3), Point(4, 4)])
        actual_result = delivery.get_instructions()

        assert actual_result == expected_result

    def test_get_route__negative_coordinate(self):
        expected_result = "ENNNDWWND"

        delivery = Delivery([Point(1, 3), Point(-1, 4)])
        actual_result = delivery.get_instructions()

        assert actual_result == expected_result

    def test_get_route__start_point(self):
        expected_result = "DD"

        delivery = Delivery([Point(0, 0), Point(0, 0)])
        actual_result = delivery.get_instructions()

        assert actual_result == expected_result
