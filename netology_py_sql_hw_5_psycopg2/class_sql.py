# Импорт модуля Psycopg2 для взаимодействовия с базой postgres
from pickle import NONE
import psycopg2


class db_client:

    """Класс для создания и работы с таблицами 
    для СУБД PostgresSQL
    """
    def __init__(self, conn):
        # conn - необходимое подключение для работы с БД
        self.connect = conn 


    def check_absence(self, id:int = None, email: str = None, number: int = None) -> bool:
        'Метод возвращет True если в базе нету id, номера телефона или емейла и Folse если есть'
        with self.connect.cursor() as cur: 
            cur.execute("""
            SELECT client.id, email, number 
              FROM client
              FULL JOIN phone_num 
                ON client.id = phone_num.client_id
             WHERE client.id = %s OR email = %s OR number = %s;
            """, (id, email, number))
            return not bool(cur.fetchall())



    # Форматирование значений допустимо через оператор %s, а вот форматирование имен таблиц, столбцов возможно только через конструкцию format(Identifier('_'))
    def create_table(self, name: str) -> str:
        'Этот метод создает таблицы из заготовок с именем "client" или "phone_num"'
        with self.connect.cursor() as cur:
            if name == 'client':   
                # cur.execute - метод для написания запросов с помощью cur(курсор)                            
                cur.execute("""
                CREATE TABLE IF NOT EXISTS client(
                            id SERIAL       PRIMARY KEY,
                    first_name VARCHAR(60)  NOT NULL,   
                     last_name VARCHAR(60)  NOT NULL,
                         email VARCHAR(200) NOT NULL UNIQUE
                    );                 
                """)
                self.connect.commit()  # только после commit или fetch(one,many,all) происходит отправка запроса в БД
                return f'Создана таблица {name} с полями id, first_name, last_name и email'

            elif name == 'phone_num':    
                cur.execute("""
                CREATE TABLE IF NOT EXISTS phone_num(
                           id SERIAL      PRIMARY KEY,
                       number NUMERIC(12) UNIQUE,
                    client_id INTEGER     NOT NULL REFERENCES client(id)
                    );                 
                """)
                self.connect.commit()
                return f'Создана таблица {name} с полями id, number, client_id'
            
            else:
                return 'Ошибка! Таблица не создана, нет заготовки с таким именем. Возможные имена "client", "phone_num"'


    def add_client(self, first_name: str, last_name: str, email: str, number: int = None)-> str:
        'Добавляет нового клиента'        
        with self.connect.cursor() as cur: 

            flag = self.check_absence(email = email, number = number)

            if flag:
                # Форматирование запросов через оператор % и кортеж (f - строки не подходят, возможен вредоносный код)                             
                cur.execute("""
                INSERT INTO client(first_name, last_name, email) 
                VALUES(%s, %s, %s) 
                RETURNING id;                     
                """, (first_name.capitalize(), last_name.capitalize(), email))

                if number != None:
                    # Возвращает RETURNING id и фиксирует изменения 
                    client_id = cur.fetchone()
                    cur.execute("""
                    INSERT INTO phone_num(number, client_id) 
                    VALUES(%s, %s);                     
                    """, (number, client_id))

                self.connect.commit()
                return f'Клиент {first_name.capitalize()} добавлен(a)'

            else:
                return 'Ошибка! Клиент c таким емейлом и/или номером телефона уже есть в базе'               


    def add_phone_num(self, number: int, id: int  = None, email: str = None)-> str:
        'Добавляет номер телефона к существующему клиенту'
        flag = self.check_absence(number = number)
      
        if flag:   
            with self.connect.cursor() as cur:
                flag_id = self.check_absence(id = id)
                flag_email = self.check_absence(email = email)

                if flag_id and flag_email:
                    return 'Ошибка! Такого id или емейла нет в базе'   

                elif email and id == None:                
                    cur.execute("""
                    SELECT id FROM client 
                    WHERE email = %s;                
                    """, (email, ))
                    id = cur.fetchone()

                cur.execute("""
                INSERT INTO phone_num(number, client_id) 
                VALUES (%s, %s);                
                """, (number, id))

                self.connect.commit()                 
                return 'Номер телефона добавлен'     
        else:
            return 'Ошибка! Этот номер уже есть в базе'   



    def change_client(self, id: int = None, email: str = None, 
                    first_name: str = None, last_name: str = None, 
                        number: int = None)-> str:
        'Меняет данные клиента'
        with self.connect.cursor() as cur:               

            flag_id = self.check_absence(id = id)
            flag_email = self.check_absence(email = email)

            if flag_id:
                return 'Ошибка! Такого id нет в базе'   

            elif not flag_email:
                return 'Ошибка! Нельзя заменить емэйл на уже существующий'   

            if email != None:
                cur.execute("""
                UPDATE client 
                   SET email=%s 
                 WHERE id=%s;
                """, (email, id))

            if first_name != None:
                cur.execute("""
                UPDATE client 
                   SET first_name=%s 
                 WHERE id=%s;
                """, (first_name, id))

            if last_name != None:
                cur.execute("""
                UPDATE client 
                   SET last_name=%s 
                 WHERE id=%s;
                """, (last_name, id))

            if number != None:
                cur.execute("""
                SELECT COUNT(*)
                  FROM phone_num
                 WHERE client_id=%s;
                """, (id, ))

                if cur.fetchall()[0][0] > 1:
                    return f'Невозможно изменить номер т.к. у клиенат несколько номеров'                       

                cur.execute("""
                UPDATE phone_num 
                   SET number=%s 
                 WHERE client_id=%s;
                """, (number, id))

            self.connect.commit()                 
            return f'Данные клиента id={id} изменены'     


    def del_phone_num(self, number: int)-> str:
        'Удаляет номер телефона у клиента'
        flag = self.check_absence(number = number)
        if not flag:   
            with self.connect.cursor() as cur:

                cur.execute("""
                DELETE FROM phone_num 
                 WHERE number=%s;
                """, (number, ))

                self.connect.commit()                 
                return 'Номер телефона удален'     
        else:
            return 'Ошибка! Такого номера нет в базе'  


    def del_client(self,  id: int = None, email: str = None)-> str:
        'Удаляет данные о клиенте из БД'
        with self.connect.cursor() as cur:

            flag_id = self.check_absence(id = id)
            flag_email = self.check_absence(email = email)

            if flag_id and flag_email:
                return 'Ошибка! Такого id или емейла нет в базе'   

            elif email and id == None:                
                cur.execute("""
                SELECT id 
                  FROM client 
                 WHERE email = %s;                
                """, (email, ))
                id = cur.fetchone()

            cur.execute("""
            DELETE FROM phone_num 
             WHERE client_id=%s;
            """, (id, ))

            cur.execute("""
            DELETE FROM client 
             WHERE id=%s;
            """, (id, ))

            self.connect.commit()                 
            return 'Данные о клиенте удалены'     
      

    def find_client(self, id: int = None, first_name: str = None, 
                   last_name: str = None, email: str = None, 
                      number: int = None) -> str:
        'Находит клиента по его данным'
        with self.connect.cursor() as cur: 
            cur.execute("""
            SELECT client.id, first_name, last_name, email, number 
              FROM client
              FULL JOIN phone_num 
                ON client.id = phone_num.client_id
             WHERE client.id = %s 
                OR first_name = %s 
                OR last_name = %s 
                OR email = %s 
                OR number = %s;
            """, (id, first_name, last_name, email, number))

            data = cur.fetchall()

            for i in range(len(data)):
                print({'id': data[i][0], 'first_name': data[i][1], 'last_name': data[i][2], 
                                        'email': data[i][3], 'number': data[i][4]})

            return 'Получены все совпадения'

   