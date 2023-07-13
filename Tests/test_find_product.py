import time
from selenium import webdriver
from Pages.start_page import Start_page
from Pages.find_page import Find_page
from Pages.product_1_page  import Product_1_page

def test_find_product():

    driver = webdriver.Chrome()
    print("start find product test")

    start = Start_page(driver)
    start.start()

    input_and_f = Start_page(driver)
    input_and_f.input_and_find()

    scrol = Find_page(driver)
    scrol.scroll_to_product_1()

    click = Find_page(driver)
    click.product()

    asse = Product_1_page(driver)
    asse.assert_product_1()

    time.sleep(10)

    print("Finish find product test")
    driver.quit()