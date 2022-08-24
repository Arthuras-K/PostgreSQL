# Импорт модуля Psycopg2 для взаимодействовия с базой postgres
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
              JOIN phone_num 
                ON client.id = phone_num.client_id
             WHERE client.id = %s OR email = %s OR number = %s;
            """, (id, email, number))
            return not bool(cur.fetchall())



    # Форматирование значений допустимо через оператор %s, а вот форматирование имен таблиц, столбцов возможно только через конструкцию format(Identifier('_'))
    def create_table(self, name: str) -> str:
        'Метод create_table создает таблицы из заготовок с именем "client" или "phone_num"'
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

            return 'Ошибка! Таблица не создана, нет заготовки с таким именем. Возможные имена "client", "phone_num".'


    def add_client(self, first_name: str, last_name: str, email: str, number: int = None)-> str:
        'Метод add_client добавляет нового клиента'        
        with self.connect.cursor() as cur: 

            flag = self.check_absence(email = email, number = number)

            if flag:
                # Форматирование запросов через оператор % и кортеж (f - строки не подходят, возможен вредоносный код)                             
                cur.execute("""
                INSERT INTO client(first_name, last_name, email) 
                VALUES(%s, %s, %s) RETURNING id;                     
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
        'Метод add_phone_num добавляет номер телефона к существующему клиенту'
        flag = self.check_absence(number = number)
        if flag:   

            with self.connect.cursor() as cur:  

                flag_id = not self.check_absence(id = id)
                flag_email = not self.check_absence(email = email)

                if flag_id:
                    cur.execute("""
                    INSERT INTO phone_num(number, client_id) 
                    VALUES (%s, %s) RETURNING id;                
                    """, (number, id))

                    return f'Клиенту с id={id} успешно добавлен номер телефона' 

                elif flag_email:
                    return f'Клиенту с емейл={email} успешно добавлен номер телефона'                    

                else:
                    return 'Добавили по емейлу'                
        else:
            return 'Ошибка! Этот номер уже есть в базе'   


        


    # Изменить данные о клиенте
    def change_client(self ):
        with self.connect.cursor() as cur:                    
            cur.execute("""
            CREATE TABLE IF NOT EXISTS name=%s(
                id SERIAL PRIMARY KEY             
            """, (name,))
            conn.commit()


    # Удалить номер телефона
    def del_phone_num(self ):
        with self.connect.cursor() as cur:                    
            cur.execute("""
            CREATE TABLE IF NOT EXISTS name=%s(
                id SERIAL PRIMARY KEY             
            """, (name,))
            conn.commit()


    # Удалить клиента из БД
    def del_client(self ):
        with self.connect.cursor() as cur:                    
            cur.execute("""
            CREATE TABLE IF NOT EXISTS name=%s(
                id SERIAL PRIMARY KEY             
            """, (name,))
            conn.commit()            


    # Найти существующего клиента по его данным
    def find_client(self ):
        with self.connect.cursor() as cur:                    
            cur.execute("""
            CREATE TABLE IF NOT EXISTS name=%s(
                id SERIAL PRIMARY KEY             
            """, (name,))
            conn.commit()            



   