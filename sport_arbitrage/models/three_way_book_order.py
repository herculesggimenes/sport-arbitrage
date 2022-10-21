
from dataclasses import dataclass

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Optional


@dataclass
class ThreeWayBookOrder:
    book_maker_name:str
    sport:str
    league:str
    series:str
    first_team_name: str
    second_team_name: str
    reference_date:Optional[date]
    first_team_odds:Decimal
    second_team_odds:Decimal
    tie_odds:Decimal

    def __hash__(self):
        return hash(
                self.book_maker_name + self.sport + self.league
                + self.series + self.first_team_name + self.second_team_name + self.reference_date.isoformat())