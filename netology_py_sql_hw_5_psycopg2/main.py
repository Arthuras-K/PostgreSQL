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

        db = sql.db_client(conn)

        # Создать две таблицы
        print(db.create_table('client'))
        print(db.create_table('phone_num')) 

        # Добавить новую запись. Обязательно имя, фамилию, емейл и по желанию номер телефона
        print(db.add_client(first_name = 'кaкa',last_name = 'енего', email = 'paip@yandex.ru', number = +7999557777))        

        # Добавить номер телефон к существующему клиенту по его id или емейлу
        print(db.add_phone_num(number = +79975487, id = 3, email = None))         

        # Изменить данные клиента по его id или емейлу
        data = {
        'id': 3, 'email': 'paip@yandex.ru', 'first_name': None, 'last_name': None, 'numb': None   
        }
        print(db.change_client(**data))       

    conn.close()
