import random

from selenium.webdriver.common.by import By


class ShopPhonePageElementsLocators:

    JUMP_TO_PURCHASE_BUTTON_XPATH = \
        f'(//div[contains(@class,"product-listing-box ")]//div[contains(@class,"product-listing-item-btn")]' \
        f'//a[contains(@class,"button")])[{random.randint(1, 12)}]'

    SELECT_6_MONTH_XPATH = '//span[contains(@class,"select2-results")]//li[contains(@class,"select2-results__option")]//div[contains(@class,"value")][contains(.,"6 мес по")]'

    LOG_IN_AND_BYE_BUTTON_XPATH = '//div[contains(@class,"live-filter-content-item active")]//div[contains(@class,"price-block-button")]//button//span[contains(@class,"button-label")][text()="Войти и купить"]'

    SELECTION_ARROW = \
        (By.XPATH, '//span[contains(@class,"selection")]//span[contains(@class,"select2-selection__arrow")]')

    PHONE_NAME_AND_COLOUR_HEADER = (By.XPATH, '//span[contains(@itemprop,"name")]//h1[contains(@class,"h")]')

    SELECT_6_MONTH = (By.XPATH, SELECT_6_MONTH_XPATH)

    LOG_IN_AND_BYE_BUTTON = (By.XPATH, LOG_IN_AND_BYE_BUTTON_XPATH)
