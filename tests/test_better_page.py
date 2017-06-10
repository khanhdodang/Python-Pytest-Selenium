import pytest


@pytest.mark.usefixtures('driver')
class TestBetterPage(object):

  def test_main_page(self, driver):
    """
    Verify 'Buying a home?' text and click on 'Get pre-approved' button
    :return: None
    """
    driver.get('https://staging.better.com')
    driver.implicitly_wait(30)
    get_msg = driver.find_element_by_xpath("//h3[@class='ProductPageAction-heading']").text
    assert get_msg == "Buying a home?"
    driver.find_element_by_xpath("//button[contains(text(), 'Get pre-approved')]").click()