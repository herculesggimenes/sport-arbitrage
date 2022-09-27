from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By


if __name__ == '__main__':
    selector = f"//div[contains(@class, 'gl-Participant_General')][1]/span[@class='sgl-ParticipantOddsOnly80_Odds']"
    driver = uc.Chrome()
    driver.get('https://www.bet365.com/#/AC/B1/C1/D1002/E73179377/G40/H^1/')
    while driver.find_elements(By.XPATH,"//div[contains(@class,'bl-Preloader')]"):
        driver.refresh()
        sleep(2)
    elements = driver.find_elements(By.XPATH, selector)
    driver.quit()
    driver.get('https://www.leovegas.com/pt-br/aposta?btag=669799_4F3F0F5EFBF44262B148EE042083EE3E&pid=3702651&bid=15794#filter/football,brazil,brasileirao_serie_a')

    