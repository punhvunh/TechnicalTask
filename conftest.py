import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def sends_request_to_fixture_and_quit_driver(driver, request):
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()
    yield from sends_request_to_fixture_and_quit_driver(driver, request)
