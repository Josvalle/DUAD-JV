from flask import Flask, request, jsonify
from class_database import PgManager, DatabaseComands, check_valid_values

app = Flask(__name__)

db_manager = PgManager(
    dbname="postgres",
    user="postgres",
    password="!23J0$ue",
    host="localhost"
)

user_commands = DatabaseComands(db_manager)

@app.route("/users", methods=["POST"])
def create_new_user():
    try:
        error = check_valid_values('name', 'email','username', 'date_of_birth', 'account_status')
        if error:
            return error
        name = request.json['name']
        email = request.json ['email']
        username = request.json ['username']
        password = request.json ['password']
        date_of_birth = request.json ['date_of_birth']
        account_status = request.json ['account_status']
        user_commands.create_user(name,email,username,password, date_of_birth, account_status)
        return jsonify('user create'), 200
    except:
        return jsonify('Something when wrong!')

@app.route("/cars", methods=["POST"])
def create_new_car():
    try:
        error = check_valid_values('maker','model','year_of_manufacture','car_status')
        if error:
            return error
        maker = request.json['maker']
        model = request.json['model']
        year_of_manufacture = request.json['year_of_manufacture']
        car_status = request.json['car_status']
        user_commands.create_car(maker, model, year_of_manufacture, car_status)
        return jsonify('car create'), 200
    except:
        return jsonify('Something when wrong!')
    

@app.route("/rentals", methods=["POST"])
def create_new_rent():
    try:
        error = check_valid_values('user_id','cars_id','rental_status')
        if error:
            return error
        user_id = request.json['user_id']
        cars_id = request.json['cars_id']
        rental_status = request.json['rental_status']
        user_commands.create_new_rent(user_id,cars_id,rental_status)
        return jsonify('rental create'), 200
    except:
        return jsonify('Something when wrong!')

@app.route("/cars/status", methods=["PUT"])
def change_status_of_car():
    
    try:
        error = check_valid_values('model','year_of_manufacture','car_status')
        if error:
            return error
        model = request.json['model']
        year_of_manufacture = request.json['year_of_manufacture']
        car_status = request.json['car_status']
        user_commands.modify_car_status(model,year_of_manufacture, car_status)
        return jsonify(f'Car status have been change to {car_status}'), 201
    except:
        return jsonify('Something when wrong!')

@app.route("/users/status", methods=["PUT"])
def change_status_of_user():
    try:
        error = check_valid_values('username','account_status')
        if error:
            return error
        username = request.json['username']
        account_status = request.json['account_status']
        user_commands.modify_user_status(username, account_status)
        return jsonify(f'Account  status for username {username} have been change to {account_status}'), 201
    except:
        return jsonify('Something when wrong!')

@app.route("/rent/status/complete", methods=["PUT"])
def complete_rent():
    try:
        error = check_valid_values('user_id','cars_id')
        if error:
            return error
        user_id = request.json['user_id']
        cars_id = request.json['cars_id']
        user_commands.return_rent(user_id,cars_id)
        return jsonify('Rent has been complete'), 201
        
    except:
        return jsonify('Something when wrong!')

@app.route("/rent/status", methods=["PUT"])
def change_rental_status():
    try:
        error = check_valid_values('rent_id','rental_status')
        if error:
            return error
        rent_id = request.json['rent_id']
        rental_status = request.json['rental_status']
        user_commands.change_rent_status(rent_id,rental_status)
        return jsonify(f'Rental status has been change to {rental_status}'), 201
    except:
        return jsonify('Something when wrong!')

@app.route("/users/status/overdue", methods=["PUT"])
def change_status_of_user_overdue():
    try:
        error = check_valid_values('username',)
        if error:
            return error
        username = request.json['username']
        account_status = 'Overdue'
        user_commands.modify_user_status(username, account_status)
        return jsonify(f'user: {username} has been flagged as Overdue'), 201
    except:
        return jsonify('Something when wrong!')
    

@app.route("/cars")
def show_cars_information():
    try:
        if request.args:
            table_column = request.args.get('column')
            table_filter = request.args.get('table_filter')
            result = user_commands.show_filter_tables_queries('cars',table_column,table_filter)
            return result
        else: 
            result = user_commands.show_all_values_cars()
            return result
    except:
        return jsonify('Something when wrong!')

@app.route("/users")
def show_users_information():
    try:
        if request.args:
            table_column = request.args.get('column')
            table_filter = request.args.get('table_filter')
            result = user_commands.show_filter_tables_queries('users',table_column,table_filter)
            return result
        else: 
            result = user_commands.show_all_values_users()
            return result
    except:
        return jsonify('Something when wrong!')

@app.route("/rentals")
def show_rentals_information():
    try:
        if request.args:
            table_column = request.args.get('column')
            table_filter = request.args.get('table_filter')
            result = user_commands.show_filter_tables_queries('rentals',table_column,table_filter)
            return result
        else: 
            result = user_commands.show_all_values_rentals()
            return result
    except:
        return jsonify('Something when wrong!')
if __name__ == "__main__":
    
    app.run(host='localhost', debug=True)