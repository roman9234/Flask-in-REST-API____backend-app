from flask import Flask, request
from marshmallow import ValidationError

from eshop.businsess_logic.order_usecases import order_create, order_get_many, order_get_by_id
from eshop.view.order_schemas import OrderCreateDtoSchema, OrderSchema, OrderGetManyParams

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


def run_server():
    app.run()
