import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_dOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "your chromedriver path"
TWITTER_EMAIL = "your twitter mail"
TWITTER_PASS = "your twitter password"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = Chrome(driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(2)
        go_to = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_to.send_keys(Keys.ENTER)

        time.sleep(2)
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)

        twitter_username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        twitter_username.send_keys(TWITTER_EMAIL)
        twitter_username.send_keys(Keys.ENTER)

        time.sleep(5)
        twitter_password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        twitter_password.send_keys(TWITTER_PASS)
        twitter_password.send_keys(Keys.ENTER)

        tweet_compose = self.driver.find_element(By.CSS_SELECTOR,'.DraftEditor-editorContainer div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_dOWN}down/{PROMISED_UP}up?"

        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div['
            '1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div')
        tweet_button.click()

        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()