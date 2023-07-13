

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

    # def get_slider_price_left(self):
    #     return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.slider_price_left)))
    # выбирает левый ползунок цены

    def get_product_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))
    # выбирает product 1



    # Actions
    def click_product_1(self):
        self.get_product_1().click()
        print("click product 1")
        # кликает product 1

    # def change_price_slider(self):
    #     price = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.slider_price_left)))
    #     self.get_slider_price_left().click_and_hold().move_by_offset(10, 0).release()
    #     print("move slider")
    #     # кликает поле ввода поиска

    # def input_name_product(self, input_name_product):
    #     self.get_input_text().send_keys(input_name_product)
    #     print("input name product")
    #     # вводит текст  для поиска
    #
    # def click_button_find(self):
    #     self.get_button_find().click()
    #     print("click button find")
    #     # кликает поле кнопку поиск


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

