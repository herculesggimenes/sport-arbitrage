from decimal import Decimal
from datetime import datetime, tzinfo
from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import pytz
from sport_arbitrage.models import ThreeWayBookOrder

BOOK_MAKER = "GALERABET"
SPORT= "SOCCER"
LEAGUE="BRASILEIRAO"
SERIES="SERIE B"
GALERABET_URL="https://sport.galera.bet/pre-jogo#/Soccer/Brazil/3104/20914001"
if __name__ == '__main__':
    odds_query = f"//div[contains(@class, 'gl-Participant_General')]/span[@class='sgl-ParticipantOddsOnly80_Odds']"
    names_query = f"//div[contains(@class,'rcl-ParticipantFixtureDetailsTeam_TeamName')]"
    dates_query = f"//div[@contains(@class,'rcl-MarketHeaderLabel-isdate')]/"
    driver = uc.Chrome()
    driver.get(GALERABET_URL)
    while driver.find_elements(By.XPATH,"//div[contains(@class,'bl-Preloader')]"):
        driver.refresh()
        sleep(2)
    odds = [Decimal(odds.text) for odds in driver.find_elements(By.XPATH, odds_query)]
    names= [name.text for name in driver.find_elements(By.XPATH,names_query)]
    total_bet_quantity = int(len(odds) / 3)
    sanity_check = True if total_bet_quantity != int(len(names) / 2) else False
    if sanity_check:
        raise ValueError("Odds doesn't have corresponding names")
    
    twbos = []
    for index in range(0,total_bet_quantity-1):
        twbo = ThreeWayBookOrder(
            book_maker_name=BOOK_MAKER,
            sport=SPORT,
            league=LEAGUE,
            series=SERIES,
            first_team_name=names[index*2],
            second_team_name=names[index*2+1],
            reference_datetime=datetime.now().astimezone(pytz.utc),
            first_team_odds=odds[index*3],
            tie_odds=odds[index*3+1],
            second_team_odds=odds[index*3+2]
        )
        twbos.append(twbo)
    driver.quit()