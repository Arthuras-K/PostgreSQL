# Импорт модуля Psycopg2 для взаимодействовия с базой postgres
import psycopg2
import class_sql as sql
import yaml



if __name__ == '__main__':  
    with open('config.yaml') as f:
        config = yaml.safe_load(f)
        PASSWORD_SQL = config['password_sql'] # Токен от ВК с доступом к фото


    # Создается подключение к БД с помощью метода connect(). database - имя БД, user - имя при регистрации в postgress, password - пароль от user
    with psycopg2.connect(database = "db_hw5", user = "postgres", password = PASSWORD_SQL) as conn:

        db = sql.db_client(conn)

        # Создать две таблицы
        print(db.create_table('client'))
        print(db.create_table('phone_num')) 

        # Добавить новую запись. Обязательно имя, фамилию, емейл и по желанию номер телефона
        print(db.add_client('кaкa', 'енего', 'ooop@yandex.ru', +7901237))        

        # Добавить номер телефон к существующему клиенту по его id или емейлу
        print(db.add_phone_num(number = +79557, id = 3, email = 'pap@yandex.ru'))         

  


    conn.close()










