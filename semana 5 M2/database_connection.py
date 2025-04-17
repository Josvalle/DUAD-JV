import psycopg2
from psycopg2 import sql,errors
# def format_user(user_record):
#     return {
#         "id": user_record[0],
#         "full_name": user_record[1],
#         "email": user_record[2],
#         "password": user_record[3],
#     }

connection = psycopg2.connect(
    host='localhost',
    port=5432,
    user='postgres',
    password='!23J0$ue',
    dbname='postgres'
)

cursor = connection.cursor()


def create_user(name,email,username,password,date_of_birth,account_status):

    cursor.execute(
        f"INSERT INTO lyfter_car_rental.users (name, email, username, password, date_of_birth, account_status) VALUES  (%s, %s, %s,%s, %s, %s,%s);", (name, email, username, password, date_of_birth, account_status)
    )
    print("Query executed")
    connection.commit()

def create_car(maker, model, year_of_manufacture, car_status):
    cursor.execute( f'INSERT INTO lyfter_car_rental.cars (maker, model, year_of_manufacture, car_status) VALUES (%s, %s, %s,%s);', (maker, model, year_of_manufacture, car_status))
    connection.commit()


def modify_user_status(username, account_status):
    try:
        cursor.execute(f'UPDATE lyfter_car_rental.users SET account_status =%s WHERE username =%s;',(account_status,username))
        
        if cursor.rowcount == 0:
            raise errors.lookup('02000')('User selected not found!')
        connection.commit()
    except:
        return ('Something when wrong!')
    
def modify_car_status(model,year_of_manufacture, car_status):
    try:
        cursor.execute(f'UPDATE lyfter_car_rental.cars SET car_status =%s WHERE model =%s AND year_of_manufacture=%s ;',(model,year_of_manufacture, car_status))
        
        if cursor.rowcount == 0:
            raise errors.lookup('02000')('Car selected not found!')
        connection.commit()
    except:
        return ('Something when wrong!')
    
def create_new_rent(user_id,cars_id,rental_status):
    cursor.execute(
        f'INSERT INTO lyfter_car_rental.rentals (user_id,cars_id,rental_status) VALUES (%s, %s, %s);', (user_id,cars_id,rental_status)
    )
    connection.commit()

def return_rent(user_id,cars_id):
    cursor.execute(
        (f'UPDATE lyfter_car_rental.cars SET car_status = "Available" WHERE id =%s ;',(cars_id))
    )
    cursor.execute(
        (f'UPDATE lyfter_car_rental.rentals SET rental_status = "Complete" WHERE user_id =%s AND cars_id=%s ;',(user_id, cars_id))
    )
    connection.commit()

def shows_available_cars():
    cursor.execute(
        (f'SELECT * FROM lyfter_car_rental.cars WHERE car_status = "Available" ;')
    )
def shows_current_rent_cars():
    cursor.execute(
        (f'SELECT * FROM lyfter_car_rental.cars WHERE car_status = "Rent" ;')
    )
        

print("Connection changes committed")
# results = cursor.fetchall()
# formatted_results = [format_user(result) for result in results]
# print(formatted_results)