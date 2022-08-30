from re import I
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables 
from models import Publisher, Book, Stock, Shop, Sale 


if __name__ == '__main__':  
    
    DSN = 'postgresql://postgres:sql8114@localhost:5432/db_hw6' # Cтрока подключения к postgres "postgresql://логин:пароль@localhost:стандартынй_порт/имя_БД"

    engine = sqlalchemy.create_engine(DSN) # Обьект который может подключиться к БД

    create_tables(engine) # Создаются таблицы (или вначале все удаляются при drop_all, а потом создаются)


    Session = sessionmaker(bind=engine) # Создаем класс который может создавать сессии подключения
    # Начало сессии
    session = Session()

    pub1 = Publisher(name="Эксмо")
    pub2 = Publisher(name="Росмэн")

    session.add_all([pub1, pub2]) # Создаем список обьектов для отправки в БД
    session.commit() # Фиксация ранее подготовленных обьектов в БД 

    book1 = Book(title="Серия книг S.T.A.L.K.E.R", publisher=pub1)

    session.add(book1) # Создаем обьект для отправки в БД
    session.commit()

    book2 = Book(title="Generation «П»", publisher=pub1)
    book3 = Book(title="Облачный атлас", publisher=pub1)
    book4 = Book(title="Гарри Поттер и философский камень", publisher=pub2)
    book5 = Book(title="Таня Гроттер и Золотая Пиявка", publisher=pub2)

    shop1 = Shop(name="Буквоед")
    shop2 = Shop(name="Читай-город")
    shop3 = Shop(name="Лабиринт")

    session.add_all([book2, book3, book4, book5, shop1, shop2, shop3])
    session.commit()

    stock1 = Stock(book=book1, shop=shop2, count=45)
    stock2 = Stock(book=book2, shop=shop1, count=29)
    stock3 = Stock(book=book2, shop=shop2, count=21)
    stock4 = Stock(book=book3, shop=shop1, count=10)
    stock5 = Stock(book=book4, shop=shop3, count=102)
    stock6 = Stock(book=book4, shop=shop2, count=56)
    stock7 = Stock(book=book5, shop=shop3, count=15)
    stock8 = Stock(book=book5, shop=shop2, count=9)
    
    session.add_all([stock1, stock2, stock3, stock4, stock5, stock6, stock7, stock8])
    session.commit()

    sale1 = Sale(price=620, date_sale=9052020, stock=stock1, count=5)
    sale2 = Sale(price=680, date_sale=10052020, stock=stock2, count=2)
    sale3 = Sale(price=210, date_sale=1052020, stock=stock3, count=8)
    sale4 = Sale(price=421, date_sale=16052020, stock=stock4, count=2)    
    sale5 = Sale(price=6700, date_sale=12052020, stock=stock5, count=23)
    sale6 = Sale(price=660, date_sale=110052020, stock=stock6, count=2)
    sale7 = Sale(price=10, date_sale=19052020, stock=stock7, count=1)
    sale8 = Sale(price=1112, date_sale=18052020, stock=stock2, count=9)
    sale9 = Sale(price=1812, date_sale=28052020, stock=stock3, count=7)
    sale10 = Sale(price=1992, date_sale=26052020, stock=stock5, count=4)
    sale11 = Sale(price=1552, date_sale=28052020, stock=stock7, count=6)
    sale12 = Sale(price=1202, date_sale=29052020, stock=stock7, count=4)

    session.add_all([sale1, sale2, sale3, sale4, sale5, sale6, sale7, sale8, sale9, sale10, sale11, sale12])
    session.commit()


    for i in session.query(Book).all(): # Извлечение всех элементов из табл
        print(i)
    for i in session.query(Book).filter(Book.title.like('%оттер%')).all(): # Извлечение всех элементов из табл с фильтрацией
        print('Книга в название есть "оттер" - ', i)
    for i in session.query(Book).join(Stock.book).filter(Stock.count > 20).all(): # Извлечение всех элементов из табл с обьединением join с другой таблицей и с фильтрацией 
        print('Книга в кол-ве больше 20 - ', i)


    session.query(Book).filter(Book.title == "Серия книг S.T.A.L.K.E.R").update({"title": "Пикник на обочине S.T.A.L.K.E.R"}) # Обновление данных в таблице
    session.commit()

            

    print('------ Задание 2 -----')

    print('Поиск через имя:')  
    name_input = "Росмэн"

    for i in session.query(Shop).join(Stock.shop).join(Book, Book.id_book == Stock.id_book).join(Publisher, Publisher.id_publisher == Book.id_publisher).filter(Publisher.name == name_input): #  Обьдинение 4 таблиц и поиск через имя
        print(i)    


    print('Поиск через id и подзапрос:')  
    id_input = 2

    subq = session.query(Book).join(Publisher, Publisher.id_publisher == Book.id_publisher).filter(Publisher.id_publisher == id_input).subquery() # Создание подзапроса и посик через id
    q = session.query(Shop).join(Stock.shop).join(subq, Stock.id_book == subq.c.id_book)

    for i in q:
        print(i)    


    session.close
