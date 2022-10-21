from collections import defaultdict
from decimal import Decimal
from typing import List, Union

from sport_arbitrage.models import ThreeWayBookOrder


def normalize_value(value: Union[str, float, int, List[str], List[float],List[int]]):
    if isinstance(value,list):
        return [Decimal(item) for item in value]
    return Decimal(value)

def converted_odds(odds: Decimal) -> Decimal:
    return Decimal(1/odds)


def implied_probability(values : List[Decimal]) -> Decimal:
    return sum(values)


def can_arbitrage(imp_prob: Decimal) -> Decimal:
    return imp_prob < 0.98


def find_grouped_three_way_book_order_odds(twb_orders: List[ThreeWayBookOrder]) -> Decimal:
    max_first_odds = 0
    max_second_odds = 0
    max_tie_odds = 0
    for twd_order in twb_orders:
        max_first_odds = max(max_first_odds,twd_order.first_team_odds)
        max_second_odds = max(max_second_odds, twd_order.second_team_odds)
        max_tie_odds = max(max_tie_odds, twd_order.tie_odds)
    max_first_odds = converted_odds(max_first_odds)
    max_second_odds = converted_odds(max_second_odds)
    max_tie_odds = converted_odds(max_tie_odds)
    return implied_probability([
        max_first_odds,
        max_second_odds,
        max_tie_odds
    ])


def group_three_way_book_orders(twb_orders: List[ThreeWayBookOrder]) -> List[List[ThreeWayBookOrder]]:
    grouped_twb_orders = defaultdict(list)
    for twb_order in twb_orders:
        grouped_twb_orders[hash(twb_order)].append(twb_order)
    return list(grouped_twb_orders.values())







