import logging
import time

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


class Duolingo:

    time_to_wait_element = 20
    poll_frequency = 0.5

    def __init__(self, url: str) -> None:
        """
        Инициализация
        """
        logging.info("Инициализируем сессию Selenium")
        self.url = url
        self.f = Faker(locale="ru_RU")
        self.task_result = ""
        self.account_password = self.f.password()
        self.account_email = self.f.free_email()
        self.account_name = self.f.name()
        self.account_age = self.f.random_int(14, 90)
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-plugins-discovery")
        # options.add_argument("--start-maximized")
        self.browser = webdriver.Remote(
            "http://selenium:4444/wd/hub",
            options=options,
        )
        cookies = {
            "name": "lang",
            "value": "ru",
            "domain": ".duolingo.com",
            "path": "/",
        }
        logging.info("Загружаем главную страницу Duolingo")
        self.browser.get(self.url)
        logging.info("Устанавливает русские cookies")
        self.browser.add_cookie(cookies)
        self.browser.get(self.url)

    def __enter__(self) -> str:
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
        except Exception as e:
            logging.info(f"Exception: {e}", exc_info=True)
            logging.info("Задача аварийно остановилась")
            self.browser.quit()
        return self.task_result

    def __exit__(self, type, value, traceback) -> None:
        """
        Выход из контекстного менеджера
        """
        logging.info("Задача выполнена успешно")
        self.browser.quit()

    def select_language(self) -> None:
        """
        Выбор языка для изучения
        """
        time.sleep(1)
        logging.info("Выбираем язык для изучения")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = '//*[@id="root"]/div/div/div[2]/div/div/ul/button[1]'
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except Exception as e:
            logging.info(f"Exception: {e}", exc_info=True)
            logging.info("Возникла ошибка при выборе языка для изучения")
            self.browser.quit()

    def select_how_did_find(self) -> None:
        """
        Отвеачем на вопрос как узнали о Duolingo
        """
        time.sleep(1)
        logging.info("Отвечаем на вопрос как узнали о Duolingo")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = f'//*[@id="root"]/div[1]/div/div[2]/div/div/div/ul/div[{self.f.random_int(1, 9)}]'
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
            xpath = '//*[@id="root"]/div[1]/div/div[2]/div/div/button'
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except Exception as e:
            logging.info(f"Exception: {e}", exc_info=True)
            logging.info(
                "Возникла ошибка во время ответа на вопрос как узнали о Duolingo"
            )
            self.browser.quit()

    def select_motivation(self) -> None:
        """
        Отвеачем на вопрос о мотивации
        """
        time.sleep(1)
        logging.info("Отвечаем на вопрос о мотивации")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = f'//*[@id="root"]/div[1]/div/div[2]/div/div/div/ul/div[{self.f.random_int(1, 7)}]'
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
            xpath = '//*[@id="root"]/div[1]/div/div[2]/div/div/button'
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except Exception as e:
            logging.info(f"Exception: {e}", exc_info=True)
            logging.info("Возникла ошибка при ответе на вопрос о мотивации")
            self.browser.quit()

    def select_daily_goal(self) -> None:
        """
        Выбираем цель дня
        """
        time.sleep(1)
        logging.info("Выбираем цель дня")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = f'//*[@id="root"]/div[1]/div/div[2]/div/div/div/label[{self.f.random_int(1, 4)}]'
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
            xpath = '//*[@id="root"]/div[1]/div/div[2]/div/div/button'
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except Exception as e:
            logging.info(f"Exception: {e}", exc_info=True)
            logging.info("Возникла ошибка при выборе цели дня")
            self.browser.quit()

    def select_help_with_socialnet(self) -> None:
        """
        Отключаем помощь уведомлениями в соц сетях
        """
        time.sleep(1)
        logging.info("Отказываемся от уведомления в социальных сетях")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = '//*[@id="root"]/div[1]/div/div[2]/div/div/ul/li[3]/button'
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except Exception as e:
            logging.info(f"Exception: {e}", exc_info=True)
            logging.info("Возникла ошибка при отказе уведомлений в социальных сетях")
            self.browser.quit()

    def select_direction(self) -> None:
        """
        Выбираем направление
        """
        time.sleep(1)
        logging.info("Выбираем направление")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = '//*[@id="root"]/div[1]/div/div[2]/div/div/div/button[1]'
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except Exception as e:
            logging.info(f"Exception: {e}", exc_info=True)
            logging.info("Возникла ошибка при выборе направления")
            self.browser.quit()

    def close_first_lesson(self) -> None:
        """
        Закрываем первый урок
        """
        time.sleep(1)
        logging.info("Закрываем первый урок")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = '//*[@id="root"]/div/div/div/div/div[1]/div/div/button'
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except Exception as e:
            logging.info(f"Exception: {e}", exc_info=True)
            logging.info("Возникла ошибка при закрытие первого урока")
            self.browser.quit()

    def open_create_profile(self) -> None:
        """
        Открыть форму создания профиля
        """
        time.sleep(1)
        logging.info("Открываем форму создание пользователя")
        try:
            self.browser.get("https://www.duolingo.com/shop")
            time.sleep(5)
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            try:
                xpath = (
                    '//*[@id="root"]/div[4]/div/div[2]/div/div[1]/div/div[2]/button[1]'
                )
                browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
            except Exception:
                logging.info("Кнопка не найдена, пробуем еще раз.")
                self.browser.get("https://www.duolingo.com/shop")
                time.sleep(5)
                browser = WebDriverWait(
                    driver=self.browser,
                    timeout=self.time_to_wait_element,
                    poll_frequency=self.poll_frequency,
                )
                try:
                    xpath = '//*[@id="root"]/div[4]/div/div[2]/div/div[1]/div/div[2]/button[1]'
                    browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
                except Exception:
                    logging.info("Кнопка не найдена и во второй раз.")
        except Exception as e:
            logging.info(f"Exception: {e}", exc_info=True)
            logging.info("Возникла ошибка при открытие формы создания пользователя")
            self.browser.quit()

    def set_age(self) -> None:
        """
        Указать возраст
        """
        logging.info("Указываем возраст")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = '//*[@id="overlays"]/div[2]/div/div/form/div[1]/div[1]/div[1]/label/div/input'
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).send_keys(
                self.account_age
            )
        except Exception as e:
            logging.info(f"Exception: {e}", exc_info=True)
            logging.info("Возникла ошибка при указание возраста")
            self.browser.quit()

    def set_name(self) -> None:
        """
        Указать имя
        """
        logging.info("Указываем имя")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = '//*[@id="overlays"]/div[2]/div/div/form/div[1]/div[1]/div[2]/label/div/input'
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).send_keys(
                self.account_name
            )
        except Exception as e:
            logging.info(f"Exception: {e}", exc_info=True)
            logging.info("Возникла ошибка при указании имени")
            self.browser.quit()

    def set_email(self) -> None:
        """
        Указать почту
        """
        logging.info("Указываем почту")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = '//*[@id="overlays"]/div[2]/div/div/form/div[1]/div[1]/div[3]/label/div/input'
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).send_keys(
                self.account_email
            )
        except Exception as e:
            logging.info(f"Exception: {e}", exc_info=True)
            logging.info("Возникла ошибка при указании почты")
            self.browser.quit()

    def set_password(self) -> None:
        """
        Указать пароль
        """
        logging.info("Указываем пароль")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = '//*[@id="overlays"]/div[2]/div/div/form/div[1]/div[1]/div[4]/label/div/input'
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).send_keys(
                self.account_password
            )
        except Exception as e:
            logging.info(f"Exception: {e}", exc_info=True)
            logging.info("Возникла ошибка при укаании пароля")
            self.browser.quit()

    def submit_create_profile(self) -> None:
        """
        Подтвердить указанные данные
        """
        logging.info("Подтверждаем создание пользователя")
        try:
            browser = WebDriverWait(
                driver=self.browser,
                timeout=self.time_to_wait_element,
                poll_frequency=self.poll_frequency,
            )
            xpath = '//*[@id="overlays"]/div[2]/div/div/form/div[1]/button'
            browser.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
            logging.info(
                f"Создан пользователь: {self.account_name} {self.account_age}y.o {self.account_email}:{self.account_password}"
            )
            self.task_result = (
                f"{self.account_name} {self.account_email}:{self.account_password}"
            )
        except Exception as e:
            logging.info(f"Exception: {e}", exc_info=True)
            logging.info("Возникла ошибка при подтверждении создания пользователя")
            self.browser.quit()
