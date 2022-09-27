from decimal import Decimal
from datetime import datetime
from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

from sport_arbitrage.models import ThreeWayBookOrder

BOOK_MAKER = "BET365"
SPORT= "SOCCER"
LEAGUE="BRASILEIRAO"
SERIES="SERIE B"

if __name__ == '__main__':
    odds_query = f"//div[contains(@class, 'gl-Participant_General')]/span[@class='sgl-ParticipantOddsOnly80_Odds']"
    names_query = f"//div[contains(@class,'rcl-ParticipantFixtureDetailsTeam_TeamName')]"
    driver = uc.Chrome()
    driver.get('https://www.bet365.com/#/AC/B1/C1/D1002/E73179377/G40/H^1/')
    while driver.find_elements(By.XPATH,"//div[contains(@class,'bl-Preloader')]"):
        driver.refresh()
        sleep(2)
    odds = [Decimal(odds.text) for odds in driver.find_elements(By.XPATH, odds_query)]
    names= [name.text for name in driver.find_elements(By.XPATH,names_query)]
    total_bet_quantity = len(odds) / 3 
    sanity_check = True if total_bet_quantity != len(names) / 2 else False
    if sanity_check:
        raise ValueError("Odds doesn't have corresponding names")
    
    twbos = []
    for index in range(1,total_bet_quantity+1):
        twbo = ThreeWayBookOrder(
            book_maker_name=BOOK_MAKER,
            sport=SPORT,
            league=LEAGUE,
            first_team_name=names[index*2],
            second_team_name=names[index*2+1],
            reference_datetime=datetime.now(),
            first_team_odds=odds[index*3],
            draw_odds=odds[index*3+1],
            second_team_odds=odds[index*3+2]
        )
        twbos.append(twbo)
    driver.quit()