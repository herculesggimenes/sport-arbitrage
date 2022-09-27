
from dataclasses import dataclass

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

@dataclass
class ThreeWayBookOrder:
    book_maker_name:str
    sport:str
    league:str
    series:str
    first_team_name: str
    second_team_name: str
    reference_datetime:datetime
    first_team_odds:Decimal
    second_team_odds:Decimal
    draw_odds:Decimal