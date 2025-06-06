from flask import Flask,request,Response,jsonify
from database_manager import User, Products,Invoices
from authenticator import JWT_Manager 

app = Flask(__name__)

user = User()
invoices = Invoices()
products = Products()
jwt_manager = JWT_Manager()

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()  # data is empty
    if(data.get('username') == None or data.get('password') == None):
        return Response(status=400)
    else:
        result = user.insert_user(data.get('username'), data.get('password'))
        user_id = result[0]

        token = jwt_manager.encode({'id':user_id})
        
        return jsonify(token=token)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # data is empty
    if(data.get('username') == None or data.get('password') == None):
        return Response(status=400)
    else:
        result = user.get_user(data.get('username'), data.get('password'))

        if(result == None):
            return Response(status=403)
        else:
            user_id = result[0]
            token = jwt_manager.encode({'id':user_id})
        
            return jsonify(token=token)

@app.route('/me')
def me():
    try:
        token = request.headers.get('Authorization')
        if(token is not None):
            token = token.replace("Bearer ","")
            decoded = jwt_manager.decode(token)
            user_id = decoded['id']
            user_value = user.get_user_by_id(user_id)
            return jsonify(id=user_id, username=user_value[1])
        else:
            return Response(status=403)
    except Exception as e:
        return Response(status=500)

@app.route('/purchase',methods=['POST'])
def new_purchase():
    try:
        token = request.headers.get('Authorization')
        data = request.get_json()
        if(token is not None):
            token = token.replace("Bearer ","")
            decoded = jwt_manager.decode(token)
            user_id = decoded['id']
            product = data.get('product')
            quantity_of_product = data.get('quantity_of_product')
            invoices.insert_new_invoice(user_id,product,quantity_of_product)
            return jsonify('Purchase succesfully create', 200)
        else:
            return Response(status=403)
    except Exception as e:
        return Response(status=500)

@app.route('/me/invoices')
def my_invoices():
    try:
        token = request.headers.get('Authorization')
        if(token is not None):
            token = token.replace("Bearer ","")
            decoded = jwt_manager.decode(token)
            user_id = decoded['id']
            invoices = Invoices.show_invoices_per_client(user_id)
            return jsonify(invoices, 200)
        else:
            return Response(status=403)
    except Exception as e:
        return Response(status=500)

@app.route('/user/modification', methods=['POST'])
def modify_user():
    try:
        data = request.get_json() 
        token = request.headers.get('Authorization')
        if(token is not None):
            print('token exist')
            token = token.replace("Bearer ","")
            decoded = jwt_manager.decode(token)
            user_id = decoded['id']
            permition = user.get_user_role(user_id)
            print(f'it is True:? {permition}')
            if permition == True:
                print('Modifying users...')
                user.modify_user(int(data.get('user_id')),data.get('column'),data.get('new_value'))
                return jsonify('User modify', 200)
            else:
                return Response(status=403)
        else:
            return Response(status=403)
    except Exception as e:
        return Response(status=500)

@app.route('/user/delete', methods=['DELETE'])
def delete_users():
    print('function enter')
    try:
        data = request.get_json() 
        token = request.headers.get('Authorization')
        if(token is not None):
            token = token.replace("Bearer ","")
            decoded = jwt_manager.decode(token)
            user_id = decoded['id']
            permition = user.get_user_role(user_id)
            if permition == True:
                user.delete_user(data.get('user_id'))
                return jsonify('user delete', 200)
            else:
                return Response(status=403)
        else:
            return Response(status=403)
    except Exception as e:
        return Response(status=500)

@app.route('/products/new_product', methods =['POST'])
def add_new_product():
    try:
        data = request.get_json() 
        token = request.headers.get('Authorization')
        if(token is not None):
            token = token.replace("Bearer ","")
            decoded = jwt_manager.decode(token)
            user_id = decoded['id']
            permition = user.get_user_role(user_id)
            if permition == True:
                products.insert_new_product(data.get('name'),data.get('price'),data.get('entry_date'), data.get('quantity'))
                return jsonify(f'product: {data.get('name')} add', 200)
            else:
                return Response(status=403)
        else:
            return Response(status=403)
    except Exception as e:
        return Response(status=500)


@app.route('/products/modification', methods=['POST'])
def modify_product():
    try:
        data = request.get_json() 
        token = request.headers.get('Authorization')
        if(token is not None):
            token = token.replace("Bearer ","")
            decoded = jwt_manager.decode(token)
            user_id = decoded['id']
            permition = user.get_user_role(user_id)
            if permition == True:
                products.modify_product (data.get('product_id'),data.get('column'),data.get('new_value'))
                return jsonify(f'Products has been modified', 200)
            else:
                return Response(status=403)
        else:
            return Response(status=403)
    except Exception as e:
        return Response(status=500)

@app.route('/products/delete', methods=['DELETE'])
def delete_products():
    try:
        data = request.get_json() 
        token = request.headers.get('Authorization')
        if(token is not None):
            token = token.replace("Bearer ","")
            decoded = jwt_manager.decode(token)
            user_id = decoded['id']
            permition = user.get_user_role(user_id)
            if permition == True:
                products.delete_product (data.get('product_id'))
                return jsonify(f'Product with ID: {data.get('product_id')} has been delete')
            else:
                return Response(status=403)
        else:
            return Response(status=403)
    except Exception as e:
        return Response(status=500)

@app.route('/invoices/modification', methods=['POST'])
def modify_invoice():
    try:
        data = request.get_json() 
        token = request.headers.get('Authorization')
        if(token is not None):
            token = token.replace("Bearer ","")
            decoded = jwt_manager.decode(token)
            user_id = decoded['id']
            permition = user.get_user_role(user_id)
            if permition == True:
                invoices.modify_invoice (data.get('invoice_id'),data.get('column'),data.get('new_value'))
                return jsonify(f'The invoice with id {data.get('invoice_id')} has been modified ', 200)
            else:
                return Response(status=403)
        else:
            return Response(status=403)
    except Exception as e:
        return Response(status=500)

@app.route('/invoices/delete', methods=['DELETE'])
def delete_invoice():
    try:
        data = request.get_json() 
        token = request.headers.get('Authorization')
        if(token is not None):
            token = token.replace("Bearer ","")
            decoded = jwt_manager.decode(token)
            user_id = decoded['id']
            permition = user.get_user_role(user_id)
            if permition == True:
                invoices.delete_invoice (data.get('invoice_id'))
            else:
                return Response(status=403)
        else:
            return Response(status=403)
    except Exception as e:
        return Response(status=500)

if __name__ == "__main__":
    
    app.run(host='localhost', debug=True)