from selenium import webdriver

from screenshorts import get_file_content, get_chromedriver_object


def test_user_receives_a_list_for_reading_file_content():
    filename = "urls.txt"
    return_value = get_file_content(filename)
    assert isinstance(return_value, list)


def test_returns_a_non_empty_list_for_a_correct_filename():
    filename = "urls.txt"
    return_value = get_file_content(filename)
    assert isinstance(return_value, list)
    assert bool(return_value) == True


def test_returns_an_empty_list_for_an_incorrect_filename():
    filename = "crymeariver.csv"
    return_value = get_file_content(filename)
    assert isinstance(return_value, list)
    assert bool(return_value) == False


def test_creates_a_chromedriver_instance():
    driver = get_chromedriver_object()
    assert isinstance(driver, webdriver.Chrome)
