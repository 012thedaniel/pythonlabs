import pymysql
from sql_config import host, port, user, password, database


def select_info_from_database(request, value):
    try:
        connection = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
        with connection.cursor() as cursor:
            cursor.execute(request, value)
            data = cursor.fetchall()
        connection.close()
        return data
    except Exception as e:
        print(f'oooops... {e}')


def insert_delete_update_info_in_database(request, value):
    try:
        connection = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
        with connection.cursor() as cursor:
            cursor.execute(request, value)
        connection.commit()
        connection.close()
    except Exception as e:
        print(f'oooops... {e}')
