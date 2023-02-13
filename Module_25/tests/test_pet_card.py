import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
   pytest_driver = webdriver.Chrome('D:\__Programming\_Python_My_Projects\WebDriver_Se\chromedriver_win32\chromedriver.exe')

   '''Открывем сайт в браузере Chrome'''
   pytest_driver.get('http://petfriends.skillfactory.ru/login')

   yield pytest_driver
   pytest_driver.quit()


def test_search_example(testing):

    driver = testing

    '''Вводим email'''
    driver.find_element(By.ID, 'email').send_keys('valid email')
    '''Вводим пароль'''
    driver.find_element(By.ID, 'pass').send_keys('valid pass')
    '''Нажимаем на кнопку входа в аккаунт'''
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    '''Переходим в папку Мои питомцы'''
    driver.find_element(By.XPATH, '//button[@type="button"]').click()
    driver.find_element(By.XPATH, '//a[text()="Мои питомцы"]').click()

    '''В личном кабинете формируем количество наших питомцев'''
    number_pets = driver.find_elements(By.TAG_NAME, 'tr')
    '''В личном кабинете формируем количество фото питомцев'''
    images = driver.find_elements(By.TAG_NAME, 'img')
    '''В личном кабинете формируем список имен питомцев'''
    names = driver.find_elements(By.TAG_NAME, 'td')

    assert len(number_pets) == len(images)
