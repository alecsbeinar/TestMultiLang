import time
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class TestMain:
    def test_btn_add_to_basket(self, browser):
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        try:
            button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-add-to-basket")
        except NoSuchElementException:
            assert False, "There isn't button 'Add to basket'"
        time.sleep(10)


if __name__ == "__main__":
    pytest.main()
