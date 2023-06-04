import pytest
from task_number_three.pages.shop_phone_page import ShopPhonePage
from utilities.utilities import Utilities


def opens_domain(driver, url):
    main_page = ShopPhonePage(driver, f'https://{url}')
    main_page.open()
    return main_page


@pytest.mark.usefixtures("driver")
class TestShopPhonePage:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utilities()

    def test_random_choose_of_smartphone(self):
        a1_data = self.ut.gets_data_from_json_file('a1_data.json')
        for data in a1_data['a1_data']:
            url = data['url']
            shop_phone_page = opens_domain(self.driver, url)
            shop_phone_page.clicks_on_button_log_in_and_buy()

