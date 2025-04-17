import psycopg2
from flask import request, jsonify
from psycopg2 import sql,errors
class PgManager:
    def __init__(self,dbname,user,password,host,port=54321):
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname
        self.port = port

        self.connection = self.create_connection(dbname, user, password, host, port)
        if self.connection:
            self.cursor = self.connection.cursor()
            print("Connection created succesfully")

    
    def create_connection(self,dbname, user, password, host, port):
        try:
            connection = psycopg2.connect(
            host='localhost',
            port=5432,
            user='postgres',
            password='!23J0$ue',
            dbname='postgres'
            )
            return connection
        except Exception as error:
            print("Error connecting to the database:", error)
            return None
    
    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Connection closed")
    
    def execute_query(self, query, *args):
        self.cursor.execute(query,*args)
        if self.cursor.rowcount == 0:
            raise errors.lookup('02000')('User selected not found!')
        self.connection.commit()
        if self.cursor.description:
            results = self.cursor.fetchall()
            return results


class DatabaseComands():
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def create_user(self, name,email,username,password,date_of_birth,account_status):

        self.db_manager.execute_query(
            f"INSERT INTO lyfter_car_rental.users (name, email, username, password, date_of_birth, account_status) VALUES  (%s, %s, %s,%s, %s, %s);", (name, email, username, password, date_of_birth, account_status)
        )
        print("Query executed")
        

    def create_car(self, maker, model, year_of_manufacture, car_status):
        self.db_manager.execute_query( f'INSERT INTO lyfter_car_rental.cars (maker, model, year_of_manufacture, car_status) VALUES (%s, %s, %s,%s);', (maker, model, year_of_manufacture, car_status))
        


    def modify_user_status(self, username, account_status):
        try:
            self.db_manager.execute_query(f'UPDATE lyfter_car_rental.users SET account_status =%s WHERE username =%s;',(account_status,username))
            return True
        except:
            return ('Something when wrong!')
    
    def modify_car_status(self,model,year_of_manufacture, car_status):
        try:
            self.db_manager.execute_query(f'UPDATE lyfter_car_rental.cars SET car_status =%s WHERE model =%s AND year_of_manufacture=%s ;',(model,year_of_manufacture, car_status))
            return True
            
        except:
            return ('Something when wrong!')
        
    def create_new_rent(self, user_id,cars_id,rental_status):
        self.db_manager.execute_query(
            f'INSERT INTO lyfter_car_rental.rentals (user_id,cars_id,rental_status) VALUES (%s, %s, %s);', (user_id,cars_id,rental_status)
        )
       

    def return_rent(self,user_id,cars_id):
        self.db_manager.execute_query(
            (f'UPDATE lyfter_car_rental.cars SET car_status = \'Available\' WHERE id =%s ;',(cars_id,))
        )
        self.db_manager.execute_query(
            (f'UPDATE lyfter_car_rental.rentals SET rental_status = \'Complete\' WHERE user_id =%s AND cars_id=%s ;',(user_id, cars_id))
        )
    
    def change_rent_status(self,rent_id,rental_status):
        self.db_manager.execute_query(f'UPDATE lyfter_car_rental.rentals SET rental_status = %s WHERE rental_status = %s;',(rental_status, rent_id))

    def change_status_unavailable(self,cars_id):
        self.db_manager.execute_query(
            (f'UPDATE lyfter_car_rental.cars SET car_status = \'Unavailable\' WHERE id =%s ;',(cars_id,))
        )

    def shows_available_cars(self):
        self.db_manager.execute_query(
            (f'SELECT * FROM lyfter_car_rental.cars WHERE car_status = \'Available\' ;')
        )
    def shows_current_rent_cars(self):
        self.db_manager.execute_query(
        (f'SELECT * FROM lyfter_car_rental.cars WHERE car_status = \'Rent\' ;')
        )
        

        print("Connection changes committed")
    
    def show_all_values(self,table):
        result = self.db_manager.execute_query(
            (f'SELECT * FROM lyfter_car_rental.{table} ;')
        )
        return result
    

    def show_filter_tables_queries(self,table, column, table_filter):
        result = self.db_manager.execute_query(
            f'SELECT * FROM lyfter_car_rental.{table} WHERE {column} = %s ;', (table_filter, )
        )
        return result

def check_valid_values(*args):
        for  values in args:
            if values not in request.json:
                return jsonify(f'Request without {values} '),400