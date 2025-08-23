Requerimientos para el proyecto:
*Python 3.10+
*PostgresSQL 14+
*Redis

PostgresSQL Informacion:
Usuario: Postgres
Contraseña: "Contraseña"
Host: localhost
Puerto: 5432
Schema: Pets_store

Iniciar Postgress con PgAdmin 4 y crear la conexion con el siguiente linea:
engine = create_engine('postgresql://postgres:TU_PASSWORD@localhost:5432/postgres')

Para ejecutar el servidor:
python pets_api.py

Utilizar postman para testear los endpoints.

Principales Endpoints, Metodos que acepta y principal funcion:

*Auth

POST /register – Crear usuario y obtener token

POST /login – Iniciar sesión y obtener token

GET /me – Ver información del usuario autenticado

*Products

GET /products/list

POST /products/new_product (admin)

POST /products/modification (admin)

DELETE /products/delete (admin)

*Cart

POST /cart/add

DELETE /cart/remove/product

POST /cart/modify/amount

GET /cart

*Invoices

POST /complete/purchase

GET /me/invoices

GET /me/invoices/detail

POST /invoices/modification (admin)

DELETE /invoices/delete (admin)
