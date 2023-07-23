

from Base.base_class import Base
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Find_page(Base):


    # Locators
    # slider_price_left = "//div[@class='slider-touch-area']"
    # button_filter_menu = "//span[@class='font-semibold']"
    product_1 = "//a[@href='/products/spalnyj-meshok-puhovyj-splav-mission-light-seryj/']"


    # Getters
    def get_product_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))
    # выбирает product 1


    # Actions
    def click_product_1(self):
        self.get_product_1().click()
        print("click product 1")
        # кликает product 1


    # Methods
    def scroll_to_product_1(self):
        action = ActionChains(webdriver)
        product = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))
        action.move_to_element(product)
    # прокручивает страницу до элемента

    def product(self):
        self.get_product_1()
        self.click_product_1()
    # кликает на элемент

