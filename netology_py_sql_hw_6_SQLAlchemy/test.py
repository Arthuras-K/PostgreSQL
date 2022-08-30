import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


DSN = 'postgresql://postgres:sql8114@localhost:5432/db_hw6' # Cтрока подключения к postgres "postgresql://логин:пароль@localhost:стандартынй_порт/имя_БД"

engine = sq.create_engine(DSN) # Обьект который может подключиться к БД


Base = declarative_base() # Cециальный класс регистрирует всех наследников и создает по ним таблицы


class Publisher(Base): # Модель - специальный класс, наследник от Base
    # Задается имя таблицы
    __tablename__ = 'publisher'

    # Создаются атрибуты таблицы
    id_publisher = sq.Column(sq.Integer, primary_key=True) # Колонка, типа int, ограничене - первичный ключ(уникальность, автоинкрем.)
    name = sq.Column(sq.String(length=40), unique=True) # Колонка, типа строка мах символов 40, ограниченa на уникальность

    def __str__(self):
         return f'Publisher {self.id_publisher}: {self.name}'


def create_tables(engine):  
    # Base.metadata.drop_all(engine) # Удаляет все существущие таблицы в БД           
    Base.metadata.create_all(engine) # Создает все таблицы в БД

print(Publisher)

create_tables(engine) # Создаются таблицы










Session = sessionmaker(bind=engine) # Создаем класс который может создавать сессии подключения
# Начало сессии
session = Session()


# перем =  табл(столб1="знач", столб2="знач")

# session.add(пере, пере2, пере3) # Создаем список обьектов для отправки в БД
# session.commit() # Фиксация ранее подготовленных обьектов в БД

# for i in session.query(табл).all(): # Извлечени всех элементов из табл
#     print(c)

session.close
