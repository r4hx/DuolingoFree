import time

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
        self.browser.implicitly_wait(10)
        self.browser.get(self.url)
        time.sleep(5)

    def __enter__(self) -> None:
        """
        Вход в контекстный менеджер
        """
        self.select_language()
        self.close_test()
        self.open_create_profile()
        self.set_age()
        self.set_name()
        self.set_email()
        self.set_password()
        self.submit_create_profile()

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
            xpath = "//*[@id='root']/div/div/span/div/div/div/ul/button[8]"
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.click()
            time.sleep(5)
        except Exception:
            self.browser.quit()

    def close_test(self) -> None:
        """
        Пропуск теста на знание языка
        """
        try:
            xpath = "//*[@id='root']/div/div/div/div[1]/div/button"
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
            xpath = "//*[@id='root']/div/div[4]/div/div/div[1]/div[2]/button[1]"
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
            xpath = "//*[@id='overlays']/div[5]/div/div/form/div[1]/div[1]/div[1]/label/div/input"
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.send_keys(self.account_age)
        except Exception:
            self.browser.quit()

    def set_name(self) -> None:
        """
        Указать имя
        """
        try:
            xpath = "//*[@id='overlays']/div[5]/div/div/form/div[1]/div[1]/div[2]/label/div/input"
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.send_keys(self.account_name)
        except Exception:
            self.browser.quit()

    def set_email(self) -> None:
        """
        Указать почту
        """
        try:
            xpath = "//*[@id='overlays']/div[5]/div/div/form/div[1]/div[1]/div[3]/label/div/input"
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.send_keys(self.account_email)
        except Exception:
            self.browser.quit()

    def set_password(self) -> None:
        """
        Указать пароль
        """
        try:
            xpath = "//*[@id='overlays']/div[5]/div/div/form/div[1]/div[1]/div[4]/label/div/input"
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.send_keys(self.account_password)
        except Exception:
            self.browser.quit()

    def submit_create_profile(self) -> None:
        """
        Подтвердить указанные данные
        """
        try:
            xpath = "//*[@id='overlays']/div[5]/div/div/form/div[1]/button"
            elem = self.browser.find_element(By.XPATH, xpath)
            elem.click()
            print(
                f"{self.account_name} {self.account_age} y.o {self.account_email}: {self.account_password}"
            )
            time.sleep(10)
        except Exception:
            self.browser.quit()
