# Импорт модуля Psycopg2 для взаимодействовия с базой postgres
import psycopg2
import class_sql as sql
import yaml


if __name__ == '__main__':  
    with open('config.yaml') as f:
        config = yaml.safe_load(f)
        PASSWORD_SQL = config['password_sql'] 


    # Создается подключение к БД с помощью метода connect(). database - имя БД, user - имя при регистрации в postgress, password - пароль от user
    with psycopg2.connect(database = "db_hw5", user = "postgres", password = PASSWORD_SQL) as conn:
        # Создаем db экземпляр класса db_client
        db = sql.db_client(conn)

        # Создать две таблицы
        name_table = 'client'
        print(db.create_table(name_table))
        name_table = 'phone_num'
        print(db.create_table(name_table)) 


        # Добавить новую запись.
        # Обязательные поля для заполнения: (имя, фамилию, емейл)
        new_first_name = 'Eva'
        new_last_name = 'Romanova'
        new_email = 'er@mail.ru'
        # Не обязательные данные: (номер телефона)
        new_numbers = +7123456
        print(db.add_client(new_first_name, new_last_name, new_email, new_numbers))        


        # Добавить номер телефон к существующему клиенту по его id или емейлу
        target_id = None
        target_email = 'er@mail.ru'
        add_num = +792100
        print(db.add_phone_num(add_num, target_id, target_email))         


        # Изменить данные клиента по его id
        data = {
            'id': 1, 
            'email': None, 
            'first_name': None, 
            'last_name': 'Pulsova', 
            'number': None   
            }
        print(db.change_client(**data))    


        # Удалить номер телефона из базы
        add_num = +792100
        print(db.del_phone_num(add_num))         


        # Удалить данные о клиенте из базы
        del_id = 1
        del_email = None
        print(db.del_client(del_id, del_email))      


        # Находит данные о клиенте
        data = {
            'id': 1, 
            'email': None, 
            'first_name': None, 
            'last_name': None, 
            'number': None   
            }
        print(db.find_client(**data))  

    conn.close()
