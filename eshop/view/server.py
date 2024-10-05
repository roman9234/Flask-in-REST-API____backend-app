from flask import Flask, request
from marshmallow import ValidationError

from eshop.businsess_logic.order_usecases import order_create, order_get_many, order_get_by_id
from eshop.businsess_logic.product_usecases import product_create, product_get_by_id, product_get_many, \
    product_delete_by_id
from eshop.view.order_schemas import OrderCreateDtoSchema, OrderSchema, OrderGetManyParams
from eshop.view.product_schemas import ProductCreateDtoSchema, ProductSchema, ProductGetManyParams

app = Flask(__name__)

# Создаёт Order из JSON данных по схеме
# Выводит в ответе данные созданного order
@app.post("/api/v1/order")
def order_create_endpoint():
    try:
        # load загружает данные из JSON в схему
        order_create_dto = OrderCreateDtoSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    try:
        order = order_create(
            product_ids=order_create_dto['product_ids']
        )
    except Exception as e:
        return {
            "error": str(e)
        }

    # dump переводит схему в JSON формат
    return OrderSchema().dump(order)

# Возвращает страницу page из списка Order поделённого  на отрезки limit
@app.get("/api/v1/order")
def order_get_many_endpoint():
    try:
        order_get_many_params = OrderGetManyParams().load(request.args)
    except ValidationError as err:
        return err.messages, 400


    order = order_get_many(
        page=order_get_many_params['page'],
        limit=order_get_many_params['limit'],
    )

    return OrderSchema(many=True).dump(order)

# Возвращает Order с указанным id если он есть
# Иначе возвращает JSON с описанием ощибки
@app.get("/api/v1/order/<id>")
def order_get_by_id_endpoint(id):
    order = order_get_by_id(id)

    if order is None:
        return {
            "error": 'Not found'
        }, 404

    return OrderSchema().dump(order)


# Создание нового продукта
@app.post("/api/v1/product")
def product_create_endpoint():
    print(request)
    try:
        # load загружает данные из JSON в схему
        product_create_dto = ProductCreateDtoSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    try:
        product = product_create(
            name=product_create_dto['name'],
            price=product_create_dto['price']
        )
    except Exception as e:
        return {
            "error": str(e)
        }

    # dump переводит схему в JSON формат
    return ProductSchema().dump(product)


@app.get("/api/v1/product")
def product_get_many_endpoint():
    try:
        product_get_many_params = ProductGetManyParams().load(request.args)
    except ValidationError as err:
        return err.messages, 400


    order = product_get_many(
        page=product_get_many_params['page'],
        limit=product_get_many_params['limit'],
    )

    return ProductSchema(many=True).dump(order)

# Возвращает Product с указанным id если он есть
# Иначе возвращает JSON с описанием ощибки
@app.get("/api/v1/product/<id>")
def product_get_by_id_endpoint(id):
    product = product_get_by_id(id)

    if product is None:
        return {
            "error": 'Not found'
        }, 404

    return ProductSchema().dump(product)


@app.delete("/api/v1/product/<id>")
def product_delete_by_id_endpoint(id):
    product_delete_by_id(id)
    return {
        "result": 'Resource deleted successfully'
    }, 204


def run_server():
    app.run()
