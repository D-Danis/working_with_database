from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from sqlalchemy_utils import create_database, database_exists


class Base(DeclarativeBase):
    pass


# def get_engine(user=None, password=None, host=None, port=None, db=None, dialect='postgresql'):
#     """

#     """
#     if dialect == 'postgresql':
#         # Формируем URL для PostgreSQL
#         url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
#         # Проверяем существование БД и создаём при необходимости
#         if not database_exists(url):
#             create_database(url)
#         engine = create_engine(url, pool_pre_ping=True)
#     elif dialect == 'sqlite':
#         # Для SQLite: db интерпретируется как путь к файлу
#         if not db:
#             db = 'database.sqlite'
#         if db == ':memory:':
#             url = 'sqlite:///:memory:'
#         else:
#             # Абсолютный путь для избежания проблем с рабочим каталогом
#             db_path = os.path.abspath(db)
#             db_dir = os.path.dirname(db_path)
#             if db_dir and not os.path.exists(db_dir):
#                 os.makedirs(db_dir)
#             url = f'sqlite:///{db_path}'
#         # Для SQLite не нужны проверка существования и pool_pre_ping
#         engine = create_engine(url, echo=False)
#     else:
#         raise ValueError(f"Unsupported dialect: {dialect}. Use 'postgresql' or 'sqlite'.")

#     return engine


def get_engine(user, password, host, port, db):
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)

    eng = create_engine(url, pool_pre_ping=True)
    return eng


engine = get_engine(DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)
# engine = get_engine(db='mydatabase.sqlite', dialect='sqlite')
Session = sessionmaker(bind=engine)
