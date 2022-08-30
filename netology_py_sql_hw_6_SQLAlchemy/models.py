import sqlalchemy as sq
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base() # Cециальный класс регистрирует всех наследников и создает по ним таблицы

class Publisher(Base): # Модель - специальный класс, наследник от Base
    # Задается имя таблицы
    __tablename__ = 'publisher'

    # Создаются атрибуты таблицы
    id_publisher = sq.Column(sq.Integer, primary_key=True) # Колонка, типа int, ограничене - первичный ключ(уникальность, автоинкрем.)
    name = sq.Column(sq.String(length=40), unique=True) # Колонка, типа строка мах символов 40, ограниченa на уникальность

    # Метод для правильного отображения таблицы в print
    def __str__(self):
        return f'Publisher {self.id_publisher}: {self.name}'


class Book(Base):
    __tablename__ = 'book'

    id_book = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=60), nullable=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id_publisher"), nullable=False)

    publisher = relationship(Publisher, backref= 'book') # Для связывание с другой таблицей и автоматически создание в ней сво-ва которое будет смотреть на эту табл

    def __str__(self):
        return f'Book {self.id_book}: ({self.title}, {self.id_publisher})'


class Shop(Base):
    __tablename__ = 'shop'

    id_shop = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    def __str__(self):
        return f'Shop {self.id_shop}: {self.name}'


class Stock(Base):
    __tablename__ = 'stock'

    id_stock = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id_book'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id_shop'), nullable=False)
    count = sq.Column(sq.Integer,  nullable=False)

    book = relationship(Book, backref= 'stock')
    shop = relationship(Shop, backref= 'stock')

    def __str__(self):
        return f'Stock {self.id_stock}: ({self.id_book}, {self.id_book}, {self.count})'


class Sale(Base):
    __tablename__ = 'sale'

    id_sale = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer, nullable=False)    
    date_sale = sq.Column(sq.Integer, nullable=False)  
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id_stock"), nullable=False)
    count = sq.Column(sq.Integer,  nullable=False)

    stock = relationship(Stock, backref= 'sale')

    def __str__(self):
        return f'Sale {self.id_sale}: ({self.title}, {self.id_publisher}, {self.count})'


def create_tables(engine):  
    Base.metadata.drop_all(engine) # Удаляет все существущие таблицы в БД           
    Base.metadata.create_all(engine) # Создает все таблицы в БД
