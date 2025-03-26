import time
from selenium.webdriver.common.by import By

def test_add_to_cart_button_is_present(browser):
    # Ochiq sahifa
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Qo‘lda vizual tekshiruv uchun
    time.sleep(30)
    
    # Tugma mavjudligini assert qilish
    add_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_button.is_displayed(), "Add to basket button is not visible"
