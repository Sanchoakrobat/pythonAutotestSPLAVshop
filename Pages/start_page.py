

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Base.base_class import Base


class Start_page(Base):
    url = 'https://www.splav.ru/'




    # Locators
    input_text = "//input[@type='text']"
    button_find = "//div[@class='relative hidden lg:block']"


    # Getters
    def get_input_text(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.input_text)))
    # выбирает поле ввода поиска

    def get_button_find(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_find)))
    # выбирает кнопку поиск


    # Actions
    def click_input_text(self):
        self.get_input_text().click()
        print("click input text")
        # кликает поле ввода поиска

    def input_name_product(self, input_name_product):
        self.get_input_text().send_keys(input_name_product)
        print("input name product")
        # вводит текст  для поиска

    def click_button_find(self):
        self.get_button_find().click()
        print("click button find")
        # кликает поле кнопку поиск


    # Methods
    def start(self):

        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()

    def input_and_find(self):
        self.get_input_text()
        self.click_input_text()
        self.input_name_product("спальный мешок")
        self.get_button_find()
        self.click_button_find()







