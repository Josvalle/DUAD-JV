from  sqlalchemy import MetaData, create_engine, select, inspect, Table, Column, Integer, String, ForeignKey, insert,update,delete


db_URI = 'postgresql://postgres:!23J0$ue@localhost:5432/postgres'

engine = create_engine(db_URI) #echo=True)
metadata_obj = MetaData()

def check_if_table_exist():
    tables = ['users', 'user_address', 'cars']
    
    for table_name in tables:
        exist_of_table = inspect(engine).has_table(table_name, schema='lyfter_table_orms')
        try: 
            if exist_of_table == True:
                continue
            elif exist_of_table == False:
                if table_name == 'users':
                    user_table = Table(
                    'users',
                    metadata_obj,
                    Column('id', Integer, primary_key=True, autoincrement=True),
                    Column('first_name', String(25),nullable=False),
                    Column('last_name', String(25),nullable=False),
                    Column('user_email', String(40),nullable=False)

                    )
                elif table_name == 'user_address':
                    user_adress_table = Table(
                    'user_address',
                    metadata_obj,
                    Column('id', Integer, primary_key=True, autoincrement=True),
                    Column('user_id', ForeignKey('users.id'), nullable=False),
                    Column('address', String(150), nullable=False)
                    )
                elif table_name == 'cars':
                    cars_table = Table(
                    'cars',
                    metadata_obj,
                    Column('id', Integer, primary_key=True, autoincrement=True),
                    Column('user_id', ForeignKey('users.id')),
                    Column('plate', String(6), nullable=False)
                    )
                else:
                    return('Something when wrong')
                metadata_obj.create_all(engine)
        except: 
            return('Something when wrong')

class User():
    def __init__(self):
        self.users_table = Table('users', metadata_obj, autoload_with=engine, schema='lyfter_table_orms')
    
    
    def create_new_user(self, first_name_value, last_name_value, user_email_value):
        try:
            new_user = insert(self.users_table).values(first_name = first_name_value, last_name = last_name_value, user_email = user_email_value)
            with engine.connect() as conn:
                result = conn.execute(new_user)
                conn.commit()
        except:
            print('Something when wrong')
    def modify_user(self, column,user_email, new_value ):
        valid_columns = ['first_name', 'last_name', 'user_email']
        try:
            if column in valid_columns:
                modification = (update(self.users_table).where(self.users_table.c.user_email == user_email).values(column=new_value))
                with engine.connect() as conn:
                    result = conn.execute(modification)
                    conn.commit()
            else:
                print('not valid column selected it ')
        except:
            return('Something when wrong!')
        
    def delete_user(self, user_email):
        try:
            delete_user = delete(self.users_table).where(self.users_table.c.user_email == user_email)
            with engine.connect() as conn:
                    result = conn.execute(delete_user)
                    conn.commit()
        except Exception as ex:
            print(ex)
    
    def show_all_user(self):
        try:
            user_info = select(self.users_table)
            with engine.connect() as conn:
                for row in conn.execute(user_info ):          
                    print(row)
        except Exception as ex:
            print(ex)



class Cars():
    def __init__(self):
        self.cars_table = Table('cars', metadata_obj, autoload_with=engine, schema='lyfter_table_orms')
    def create_new_car(self,plate_value, user_id_value = None):
        try:
            if user_id_value:
                new_car = insert(self.cars_table).values(user_id = user_id_value, plate = plate_value)
            else:
                new_car = insert(self.cars_table).values(plate = plate_value,user_id = None)
            with engine.connect() as conn:
                result = conn.execute(new_car)
                conn.commit()
        except Exception as ex:
            print(ex)

    def modify_car(self, column,plate, new_value ):
        valid_columns = ['user_id', 'plate']
        try:
            if column in valid_columns:
                modification = (update(self.cars_table).where(self.cars_table.c.plate == plate).values(column=new_value))
                with engine.connect() as conn:
                    result = conn.execute(modification)
                    conn.commit()
            else:
                print('not valid column selected it ')
        except:
            return('Something when wrong!')
        
    def delete_car(self, plate):
        try:
            delete_car = delete(self.cars_table).where(self.cars_table.c.plate == plate)
            with engine.connect() as conn:
                    result = conn.execute(delete_car)
                    conn.commit()
        except Exception as ex:
            print(ex)
    

    def add_user_to_car(self, plate, user_id_value):
        try:
            add_user_car = (update(self.cars_table).where(self.cars_table.c.plate == plate).values(user_id = user_id_value))
            with engine.connect() as conn:
                    result = conn.execute(add_user_car)
                    conn.commit()
        except Exception as ex:
            print(ex)

    def show_all_cars(self):
        try:
            cars_info = select(self.cars_table)
            with engine.connect() as conn:
                for row in conn.execute(cars_info ):          
                    print(row)
        except Exception as ex:
            print(ex)


class UserAddress():
    def __init__(self):
        self.user_address_table = Table('user_address', metadata_obj, autoload_with=engine, schema='lyfter_table_orms')
    def create_new_address(self,user_id_value, address_value):
        try:
            
            new_address = insert(self.user_address_table).values(user_id = user_id_value, address = address_value)
           
            with engine.connect() as conn:
                result = conn.execute(new_address)
                conn.commit()
        except Exception as ex:
            print(ex)

    def modify_address(self, column,user_id, new_value ):
        valid_columns = ['user_id', 'address']
        try:
            if column in valid_columns:
                modification = (update(self.cars_table).where(self.user_address_table.c.user_id == user_id).values(column=new_value))
                with engine.connect() as conn:
                    result = conn.execute(modification)
                    conn.commit()
            else:
                print('not valid column selected it ')
        except:
            return('Something when wrong!')
        
    def delete_address(self, user_id):
        try:
            delete_car = delete(self.user_address_table).where(self.user_address_table.c.user_id == user_id)
            with engine.connect() as conn:
                    result = conn.execute(delete_car)
                    conn.commit()
        except Exception as ex:
            print(ex)
    
    def show_all_user(self):
        try:
            address_info = select(self.user_address_table)
            with engine.connect() as conn:
                for row in conn.execute(address_info ):          
                    print(row)
        except Exception as ex:
            print(ex)


        

