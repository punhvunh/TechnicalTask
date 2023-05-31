from task_number_three.pages.base_page import BasePage
from task_number_three.locators.shop_phone_page_elements_locators import ShopPhonePageElementsLocators


class ShopPhonePage(BasePage):
    shop_phone_page_locator = ShopPhonePageElementsLocators()

    def clicks_on_button_log_in_bye(self):
        self.clicks_on_element(self.shop_phone_page_locator.JUMP_TO_PURCHASE_BUTTON_XPATH)
        phone_name_and_color = \
            self.element_is_visible(self.shop_phone_page_locator.PHONE_NAME_AND_COLOR_HEADER).get_attribute("innerText")
        self.element_is_visible(self.shop_phone_page_locator.SELECTION_ARROW).click()
        payment_option = self.element_is_present(self.shop_phone_page_locator.SELECT_6_MONTH).get_attribute("innerText")
        self.scroll_to_element(self.shop_phone_page_locator.SELECT_6_MONTH_XPATH)
        self.element_is_visible(self.shop_phone_page_locator.SELECT_6_MONTH).click()
        self.clicks_on_element(self.shop_phone_page_locator.LOG_IN_AND_BYE_BUTTON_XPATH)
        self.element_is_not_visible(self.shop_phone_page_locator.LOG_IN_AND_BYE_BUTTON)
        print(f"\nВыдан {phone_name_and_color}, вариант оплаты {payment_option}")

