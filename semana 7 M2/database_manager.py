from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, literal_column
from sqlalchemy import insert, select, update,delete
from authenticator import JWT_Manager 

# class DBManger():
#     def __init__(self):
#         self.engine = create_engine('postgresql://postgres:!23J0$ue@localhost:5432/postgres')
#         self.metadata_obj = MetaData()
# jwt_manager = JWT_Manager ()
engine = create_engine('postgresql://postgres:!23J0$ue@localhost:5432/postgres')
metadata_obj = MetaData()

class User():
    def __init__(self):
        self.users_table = Table('users', metadata_obj, autoload_with=engine, schema='fruits_store')
    
    
    def insert_user(self, username, password, ):
        stmt = insert(self.users_table).returning(self.users_table.c.id).values(username=username, password=password, role = 'user')
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.all()[0]

    def get_user(self, username, password):
        stmt = select(self.users_table).where(self.users_table.c.username == username).where(self.users_table.c.password == password)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            users = result.all()

            if(len(users)==0):
                return None
            else:
                return users[0]

    def get_user_by_id(self, id):
        stmt = select(self.users_table).where(self.users_table.c.id == id)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            users = result.all()
            if(len(users)==0):
                return None
            else:
                return users[0]
    
    def get_user_role(self,id):
        stmt = select(self.users_table.c.role).where(self.users_table.c.id == id)
        with engine.connect() as conn:
            result = conn.execute(stmt).scalar()
            if result.strip().lower() == 'admin':
                print('true')
                return True
            elif result.strip().lower() == 'user':
                print('false')
                return False
    
    def modify_user(self, id, column, new_value ):
         
         try:
            column_modification = literal_column(column)
            modification = (update(self.users_table).where(self.users_table.c.id == id).values({column_modification: new_value}))
            with engine.begin() as conn:
                    result = conn.execute(modification)
                    
         except:
            return('Something when wrong!')
    

    def delete_user(self, id):
        try:
            delete_user = delete(self.users_table).where(self.users_table.c.id == id)
            with engine.begin() as conn:
                    result = conn.execute(delete_user)
                    return(print('user delete'))
                    
        except Exception as ex:
            print(ex)

class Products():
    def __init__(self):
        self.products_table = Table('products', metadata_obj, autoload_with=engine, schema='fruits_store')
    
    def insert_new_product(self, name, price, entry_date, quantity):
        stmt = insert(self.products_table).values(name=name, price=price, entry_date = entry_date, quantity = quantity)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
    
    def show_products(self, product = None):
        if product != None:
            stmt = select(self.products_table).where(self.products_table.c.name == product)
            with engine.connect() as conn:
                result = conn.execute(stmt)
                conn.commit()
            return result
        else:    
            stmt = select(self.products_table)
            with engine.connect() as conn:
                result = conn.execute(stmt)
                conn.commit()
            return result
    
    def verify_available_stock(self, product):
        stock = select(self.products_table.c.quantity).where(self.products_table.c.name == product)
        with engine.connect() as conn:
                result = conn.execute(stock).scalar()
                conn.commit()
        return result
    
    def obtain_id_product(self, product):
        id = select(self.products_table.c.id).where(self.products_table.c.name == product)
        with engine.connect() as conn:
                result = conn.execute(id).scalar()
                print(result)
                conn.commit()
        return int(result)

    def obtain_price_product(self, product_id, quantity_of_product):
        price = select(self.products_table.c.price).where(self.products_table.c.id == product_id)
        with engine.connect() as conn:
                result = conn.execute(price).scalar()
                conn.commit()
        
        total = result*quantity_of_product
        return int(total)
    
    def modify_product(self, id, column, new_value):
        try:
            column_modification = literal_column(column)
            modification = (update(self.products_table).where(self.products_table.c.id == id).values( {column_modification: new_value}))
            with engine.begin() as conn:
                    result = conn.execute(modification)
        except:
            return('Something when wrong!')
    
    def update_product_quantity(self, id, new_value): 
         modification = (update(self.products_table).where(self.products_table.c.id == id).values(quantity=new_value))
         with engine.begin() as conn:
              result = conn.execute(modification)
            

    def delete_product(self, id):
        try:
            delete_user = delete(self.products_table).where(self.products_table == id)
            with engine.begin() as conn:
                    result = conn.execute(delete_user)
                    
        except Exception as ex:
            print(ex)






class Invoices():
    def __init__(self):
        self.invoice_table = Table('invoices', metadata_obj, autoload_with=engine, schema='fruits_store')
        self.products_table = Products()
    
    def insert_new_invoice(self, user_id, product,quantity_of_product):
        print('start function')
        product_id = self.products_table.obtain_id_product(product)
        available_product = self.products_table.verify_available_stock(product)
        
        if available_product > quantity_of_product:
             new_quantity = available_product - quantity_of_product
             total = self.products_table.obtain_price_product(product_id, quantity_of_product)
             stmt = insert(self.invoice_table).values(user_id=user_id, products_id=product_id, total_amount = total)
             update_product = self.products_table.update_product_quantity(product_id,new_quantity)
             with engine.begin() as conn:
                result = conn.execute(stmt)
                
                
        else:
            return('Available product is lower that quantity need it ')
    
    def show_invoices_per_client(self, client):
            stmt = select(self.invoice_table).where(self.invoice_table.c.user_id == client)
            with engine.connect() as conn:
                result = conn.execute(stmt)
                conn.commit()
            return result
    
    def modify_invoice(self, id, new_value, column):
        try:
            column_modification = literal_column(column)
            modification = (update(self.invoice_table).where(self.invoice_table.c.id == id).values( {column_modification: new_value}))
            with engine.begin() as conn:
                result = conn.execute(modification)
                    
        except:
            return('Something when wrong!')
    

    def delete_invoice(self, id):
        try:
            delete_invoice = delete(self.invoice_table).where(self.invoice_table == id)
            with engine.begin() as conn:
                    result = conn.execute(delete_invoice)
                    
        except Exception as ex:
            print(ex)


# def id_getter(token):
#     token = token.replace("Bearer ","")
#     decoded = jwt_manager.decode(token)
#     user_id = decoded['id']
#     return user_id
