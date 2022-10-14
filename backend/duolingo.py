import time
from random import randint

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Duolingo:

    time_to_wait_element = 20
    poll_frequency = 0.1

    def __init__(self, url) -> None:
        """
        Инициализация
        """
        print("initialization")
        self.url = url
        self.f = Faker(locale="ru_RU")
        self.account_password = self.f.password()
        self.account_email = self.f.free_email()
        self.account_name = self.f.name()
        self.account_age = self.f.random_int(14, 90)
        options = webdriver.FirefoxOptions()
        options.add_argument("--ignore-ssl-errors=yes")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-dev-shm-usage")
        self.browser = webdriver.Remote(
            "http://selenium:4444/wd/hub",
            browser_profile=self.create_profile(),
            options=options,
        )
        cookies = {
            "name": "lang",
            "value": "ru",
            "domain": ".duolingo.com",
            "path": "/",
        }
        self.browser.get(self.url)
        self.browser.add_cookie(cookies)
        self.browser.get(self.url)

    def __enter__(self) -> None:
        """
        Вход в контекстный менеджер
        """
        try:
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
        except Exception:
            print("crashed")
            self.browser.quit()

    def __exit__(self, type, value, traceback) -> None:
        """
        Выход из контекстного менеджера
        """
        print("normal exit")
        self.browser.quit()

    def create_profile(self) -> webdriver.FirefoxProfile:
        """
        Создание профиля для браузера
        """
        profile = webdriver.FirefoxProfile()
        profile.set_preference("permissions.default.stylesheet", 2)
        profile.set_preference("permissions.default.image", 2)
        profile.set_preference("accessibility.force_disabled", 1)
        profile.set_preference(
            "places.history.expiration.transient_current_max_pages", 1
        )
        profile.set_preference("places.history.enabled", 0)
        profile.set_preference("browser.sessionstore.max_tabs_undo", 0)
        profile.set_preference("privacy.history.custom", 1)
        profile.set_preference("browser.cache.disk.enable", 0)
        profile.set_preference("browser.cache.memory.enable", 0)
        profile.set_preference("browser.cache.offline.enable", 0)
        profile.set_preference("network.http.use-cache", 0)
        profile.set_preference("browser.sessionhistory.max_total_viewers", 0)
        profile.set_preference("browser.sessionhistory.max_entries", 1)
        return profile

    def select_language(self) -> None:
        """
        Выбор языка для изучения
        """
        print("select language")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = '//*[@id="root"]/div/div/div[2]/div/div/ul/button[1]'
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except Exception:
            self.browser.quit()

    def select_how_did_find(self):
        """
        Отвеачем на вопрос как узнали о Duolingo
        """
        time.sleep(1)
        print("select how did find")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = (
                f'//*[@id="root"]/div[1]/div/div[2]/div/div/div/ul/div[{randint(1, 8)}]'
            )
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
            # click submit button
            xpath = '//*[@id="root"]/div[1]/div/div[2]/div/div/button'
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except Exception:
            self.browser.quit()

    def select_motivation(self):
        """
        Отвеачем на вопрос о мотивации
        """
        time.sleep(1)
        print("select motivation")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = (
                f'//*[@id="root"]/div[1]/div/div[2]/div/div/div/ul/div[{randint(1, 7)}]'
            )
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
            # click submit button
            xpath = '//*[@id="root"]/div[1]/div/div[2]/div/div/button'
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except Exception:
            self.browser.quit()

    def select_daily_goal(self):
        """
        Выбираем цель дня
        """
        time.sleep(1)
        print("select daily goal")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = (
                f'//*[@id="root"]/div[1]/div/div[2]/div/div/div/label[{randint(1, 4)}]'
            )
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
            # click submit button
            xpath = '//*[@id="root"]/div[1]/div/div[2]/div/div/button'
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except Exception:
            self.browser.quit()

    def select_help_with_socialnet(self):
        """
        Отключаем помощь уведомлениями в соц сетях
        """
        print("select help with socialnet")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = '//*[@id="root"]/div[1]/div/div[2]/div/div/ul/li[3]/button'
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except Exception:
            self.browser.quit()

    def select_direction(self):
        """
        Выбираем направление
        """
        print("select direction")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = '//*[@id="root"]/div[1]/div/div[2]/div/div/div/button[1]'
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except Exception:
            self.browser.quit()

    def close_first_lesson(self):
        """
        Закрываем первый урок
        """
        print("close first lesson")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = '//*[@id="root"]/div/div/div/div/div[1]/div/div/button'
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except Exception:
            self.browser.quit()

    def close_popup_window(self) -> None:
        print("close popup window")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = '//*[@id="root"]/div[1]/div/div/div[1]/div/div/button'
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except Exception:
            pass

    def open_create_profile(self) -> None:
        """
        Открыть форму создания профиля
        """
        print("open create profile")
        try:
            self.browser.get("https://www.duolingo.com/shop")
            print("click create account button")
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = (
                '//*[@id="root"]/div[5]/div/div[2]/div/div[1]/div/div[2]/button[1]/span'
            )
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except Exception:
            self.browser.quit()

    def set_age(self) -> None:
        """
        Указать возраст
        """
        print("set age")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = '//*[@id="overlays"]/div[2]/div/div/form/div[1]/div[1]/div[1]/label/div/input'
            # elem = self.browser.find_element(By.XPATH, xpath)
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).send_keys(
                self.account_age
            )
        except Exception:
            self.browser.quit()

    def set_name(self) -> None:
        """
        Указать имя
        """
        print("set name")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = '//*[@id="overlays"]/div[2]/div/div/form/div[1]/div[1]/div[2]/label/div/input'
            # elem = self.browser.find_element(By.XPATH, xpath)
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).send_keys(
                self.account_name
            )
        except Exception:
            self.browser.quit()

    def set_email(self) -> None:
        """
        Указать почту
        """
        print("set email")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = '//*[@id="overlays"]/div[2]/div/div/form/div[1]/div[1]/div[3]/label/div/input'
            # elem = self.browser.find_element(By.XPATH, xpath)
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).send_keys(
                self.account_email
            )
        except Exception:
            self.browser.quit()

    def set_password(self) -> None:
        """
        Указать пароль
        """
        print("set password")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = '//*[@id="overlays"]/div[2]/div/div/form/div[1]/div[1]/div[4]/label/div/input'
            # elem = self.browser.find_element(By.XPATH, xpath)
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).send_keys(
                self.account_password
            )
        except Exception:
            self.browser.quit()

    def submit_create_profile(self) -> None:
        """
        Подтвердить указанные данные
        """
        print("submit")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = '//*[@id="overlays"]/div[2]/div/div/form/div[1]/button'
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
            print(
                f"{self.account_name} {self.account_age} y.o {self.account_email}: {self.account_password}"
            )
        except Exception:
            self.browser.quit()
