

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Base.base_class import Base


class Product_1_page(Base):

    # Locators
    name_product_1 = "//h1[@class='mb-6 text-body-2 md:order-first md:mb-2 md:text-title-3 md:font-bold']"


    # Getters
    def get_name_product_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.name_product_1)))
    # выбирает поле ввода поиска

    def get_button_find(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_find)))
    # выбирает кнопку поиск


    # Methods
    def assert_product_1(self):
        self.assert_word(self.get_name_product_1(), "Спальный мешок пуховый Сплав Mission Light серый")
    # сравнивает надпись с заданной







