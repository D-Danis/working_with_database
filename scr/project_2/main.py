import os
import requests
import threading
import datetime as dt
from concurrent.futures import ThreadPoolExecutor

from parser import ParserLink
from orm import create_tables, data_pull_to_db
from spimex_pdf_parser import extract_spimex_bulletin_data

from logger import logger


START_URL = "https://spimex.com/markets/oil_products/trades/results/"
START_FROM = dt.datetime(2023, 1, 1).date()

thread_local = threading.local()


def get_session_for_thread():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def delete_temporary_file(file) -> None:
    os.remove(file)


def download_file(url):
    """Загрузите PDF-файл с URL-адреса на сервер."""
    requests_session = get_session_for_thread()
    with requests_session.get(url, stream=True) as response:
        response.raise_for_status()
        date = ParserLink.get_file_date(url)
        name = f"pdf/{date}.pdf"

        with open(name, mode="wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        return name, date


def file_processing(url):
    """Загрузка, обработка и вставка данных с обработкой ошибок."""
    try:
        name, date = download_file(url)
        if name is None:
            return
        logger.info(f"Файл {name} сохранён")
        data_to_store = extract_spimex_bulletin_data(name, date)
        logger.info(f"Данные из {name} получены")
        delete_temporary_file(name)
        logger.info(f"Временный файл {name} удалён")
        data_pull_to_db(data_to_store)
        logger.info(f"Данные за {date} успешно сохранены в БД")
    except Exception as e:
        logger.exception(f"Ошибка при обработке {url}: {e}")


def main():
    os.makedirs("pdf", exist_ok=True)

    create_tables()

    logger.info("Начало получения данных для обработки")
    link_builder = ParserLink(START_FROM, START_URL)
    links = link_builder.grab_links()
    links.reverse()
    link_builder.close()
    logger.info(f"Получено {len(links)} ссылок для обработки")

    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(file_processing, links)


if __name__ == "__main__":
    main()
