import time
from random import randint

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By


class Duolingo:
    def __init__(self, url) -> None:
        """
        Инициализация
        """
        self.url = url
        self.f = Faker(locale="ru_RU")
        self.account_password = self.f.password()
        self.account_email = self.f.free_email()
        self.account_name = self.f.name()
        self.account_age = self.f.random_int(14, 90)
        self.browser = webdriver.Remote("http://selenium:4444")
        cookies = {
            "name": "lang",
            "value": "ru",
            "domain": ".duolingo.com",
            "path": "/",
        }
        self.browser.implicitly_wait(10)
        self.browser.get(self.url)
        self.browser.add_cookie(cookies)
        self.browser.get(self.url)
        time.sleep(5)

    def __enter__(self) -> None:
        """
        Вход в контекстный менеджер
        """
        self.select_language()
        self.select_how_did_find()
        self.select_motivation()
        self.select_daily_goal()
        self.select_help_with_socialnet()
        self.select_direction()
        self.close_first_lesson()
        self.open_create_profile()
        self.set_age()
        self.set_name()
        self.set_email()
        self.set_password()
        self.submit_create_profile()
        # self.find_owner()

    def __exit__(self, type, value, traceback) -> None:
        """
        Выход из контекстного менеджера
        """
        self.browser.quit()

    def select_language(self) -> None:
        """
        Выбор языка для изучения
        """
        try:
            xpath = '//*[@id="root"]/div/div/span/div/div/div/ul/button[1]'
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.click()
            time.sleep(5)
        except Exception:
            self.browser.quit()

    def select_how_did_find(self):
        """
        Отвеачем на вопрос как узнали о Duolingo
        """
        try:
            num = randint(1, 8)
            xpath = f'//*[@id="root"]/div/div/div/div[2]/div/div/div/ul/div[{num}]'
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.click()
            # click submit button
            xpath = '//*[@id="root"]/div/div/div/div[2]/div/div/button'
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.click()
            time.sleep(5)
        except Exception:
            self.browser.quit()

    def select_motivation(self):
        """
        Отвеачем на вопрос о мотивации
        """
        try:
            num = randint(1, 7)
            xpath = f'//*[@id="root"]/div/div/div/div[2]/div/div/div/ul/div[{num}]'
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.click()
            # click submit button
            xpath = '//*[@id="root"]/div/div/div/div[2]/div/div/button'
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.click()
            time.sleep(5)
        except Exception:
            self.browser.quit()

    def select_daily_goal(self):
        """
        Выбираем цель дня
        """
        try:
            num = randint(1, 4)
            xpath = f'//*[@id="root"]/div/div/div/div[2]/div/div/div/label[{num}]'
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.click()
            # click submit button
            xpath = '//*[@id="root"]/div/div/div/div[2]/div/div/button'
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.click()
            time.sleep(5)
        except Exception:
            self.browser.quit()

    def select_help_with_socialnet(self):
        """
        Отключаем помощь уведомлениями в соц сетях
        """
        try:
            xpath = '//*[@id="root"]/div/div/div/div[2]/div/div/ul/li[3]/button'
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.click()
            time.sleep(5)
        except Exception:
            self.browser.quit()

    def select_direction(self):
        """
        Выбираем направление
        """
        try:
            xpath = '//*[@id="root"]/div/div/div/div[2]/div/div/div/button[1]'
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.click()
            time.sleep(5)
        except Exception:
            self.browser.quit()

    def close_first_lesson(self):
        """
        Закрываем первый урок
        """
        try:
            xpath = '//*[@id="root"]/div/div/div/div/div[1]/div/div/button'
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.click()
            time.sleep(5)
        except Exception:
            self.browser.quit()

    def open_create_profile(self) -> None:
        """
        Открыть форму создания профиля
        """
        try:
            self.browser.get("https://www.duolingo.com")
            xpath = '//*[@id="root"]/div/div[5]/div/div/div[1]/div/div[2]/button[1]'
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.click()
            time.sleep(5)
        except Exception:
            self.browser.quit()

    def set_age(self) -> None:
        """
        Указать возраст
        """
        try:
            xpath = '//*[@id="overlays"]/div[4]/div/div/form/div[1]/div[1]/div[1]/label/div/input'
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.send_keys(self.account_age)
        except Exception:
            self.browser.quit()

    def set_name(self) -> None:
        """
        Указать имя
        """
        try:
            xpath = "//*[@id='overlays']/div[4]/div/div/form/div[1]/div[1]/div[2]/label/div/input"
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.send_keys(self.account_name)
        except Exception:
            self.browser.quit()

    def set_email(self) -> None:
        """
        Указать почту
        """
        try:
            xpath = "//*[@id='overlays']/div[4]/div/div/form/div[1]/div[1]/div[3]/label/div/input"
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.send_keys(self.account_email)
        except Exception:
            self.browser.quit()

    def set_password(self) -> None:
        """
        Указать пароль
        """
        try:
            xpath = "//*[@id='overlays']/div[4]/div/div/form/div[1]/div[1]/div[4]/label/div/input"
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.send_keys(self.account_password)
        except Exception:
            self.browser.quit()

    def submit_create_profile(self) -> None:
        """
        Подтвердить указанные данные
        """
        try:
            xpath = "//*[@id='overlays']/div[4]/div/div/form/div[1]/button"
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.click()
            print(
                f"{self.account_name} {self.account_age} y.o {self.account_email}: {self.account_password}"
            )
            time.sleep(10)
        except Exception:
            self.browser.quit()

    def find_owner(self):
        """
        Находим собственный аккаунт
        """
        owner = "r4hx"
        try:
            # find search button
            xpath = (
                '//*[@id="root"]/div/div[5]/div/div/div[1]/div[4]/div[2]/button[2]/div'
            )
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.click()
            # find input
            xpath = '//*[@id="root"]/div/div[5]/div/div/div[1]/div[4]/div[3]/div/input'
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.send_keys(owner)
            # find submit
            xpath = '//*[@id="root"]/div/div[5]/div/div/div[1]/div[4]/div[3]/div/button'
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.click()
            time.sleep(5)
            # follow button
            xpath = '//*[@id="root"]/div/div[5]/div/div/div[1]/div[4]/div[3]/ul/li/div[2]/button'
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.click()
            # verify email overlay
            xpath = '//*[@id="overlays"]/div[4]/div/div/div/button'
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.click()
        except Exception:
            self.browser.quit()
