import time

from dateutil import parser
from selenium import webdriver
from selenium.webdriver.common.by import By

from logger import logger


class ParserLink:
    def __init__(self, start_from, url):
        options = webdriver.ChromeOptions()
        # options.binary_location = '/snap/bin/chromium'  # можно убрать

        # Headless-режим
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--remote-debugging-port=9222")

        options.add_argument("--disable-logging")
        options.add_argument("--log-level=3")

        options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        self.driver = webdriver.Chrome(options=options)
        self.start_date = start_from
        self.url = url
        self.links = []
        self._next_css_sel = "li.bx-pag-next a"
        self._link_css_sel = "#comp_d609bce6ada86eff0b6f7e49e6bae904 div.accordeon-inner__wrap-item a"

    @staticmethod
    def get_file_date(file_url: str):
        """Извлечение даты из имени файла."""
        date = parser.parse(file_url.split("_")[-1][:8]).date()
        return date

    def _get_links(self):
        """Получение ссылки для скачивания на этой странице."""
        link_obj = self.driver.find_elements(By.CSS_SELECTOR, self._link_css_sel)
        return [
            t.get_attribute("href") for t in link_obj if self.get_file_date(t.get_attribute("href")) >= self.start_date
        ]

    def grab_links(self):
        """Собирайте ссылки из URL-адреса.l"""
        logger.debug("Начинаем сбор ссылок")
        self.driver.get(self.url)
        time.sleep(1)
        str_obj = self._get_links()
        if str_obj:
            self.links.extend(str_obj)
            next_page = self.driver.find_element(By.CSS_SELECTOR, self._next_css_sel)
            self.url = next_page.get_attribute("href")
            self.grab_links()
        return self.links

    def close(self):
        """Закрывает драйвер и освобождает ресурсы."""
        if self.driver:
            self.driver.quit()
