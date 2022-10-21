from copy import copy
from datetime import date
from decimal import Decimal
from unittest import TestCase

from sport_arbitrage.helpers import converted_odds, implied_probability, normalize_value, \
    find_grouped_three_way_book_order_odds, group_three_way_book_orders
from sport_arbitrage.models import ThreeWayBookOrder


class Test(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.base_three_way_book_order = ThreeWayBookOrder(
            'TEST',
            'TEST',
            'TEST',
            'TEST',
            'TEST',
            'TEST',
            date(2022, 10, 21),
            normalize_value(0),
            normalize_value(0),
            normalize_value(0)
        )

    def test_converted_odds(self):
        if round(converted_odds(Decimal('1.4')), 4) != Decimal('0.7143'):
            self.fail()
        pass

    def test_implied_probability(self):
        values = normalize_value(['0.71','0.105','0.147'])
        if implied_probability(values) != normalize_value('0.962'):
            self.fail()
        pass

    def test_find_grouped_three_way_book_order_odds(self):
        first_order = copy(self.base_three_way_book_order)
        first_order.first_team_odds = normalize_value('1.4')
        first_order.second_team_odds = normalize_value('8.8')
        first_order.tie_odds = normalize_value('5.8')
        second_order = copy(self.base_three_way_book_order)
        second_order.first_team_odds = normalize_value('1.2')
        second_order.second_team_odds = normalize_value('9.5')
        second_order.tie_odds = normalize_value('6.0')
        third_order = copy(self.base_three_way_book_order)
        third_order.first_team_odds = normalize_value('1.2')
        third_order.second_team_odds = normalize_value('9.1')
        third_order.tie_odds = normalize_value('6.8')
        max_implied_probability = find_grouped_three_way_book_order_odds([first_order,second_order,third_order])
        if round(max_implied_probability, 4) != normalize_value('0.9666'):
            self.fail()
        pass

    def test_group_three_way_book_orders(self):
        first_order = copy(self.base_three_way_book_order)
        first_order.league = "LEAGUE 1"
        second_order = copy(self.base_three_way_book_order)
        second_order.league = "LEAGUE 2"
        third_order = copy(self.base_three_way_book_order)
        third_order.league = "LEAGUE 1"
        grouped_orders = group_three_way_book_orders([first_order,second_order,third_order])
        for orders in grouped_orders:
            order_hash = hash(orders[0])
            for order in orders:
                if hash(order) != order_hash:
                    self.fail()
        pass

