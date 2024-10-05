
Если использовать терминал windows, возникнут особенности с ковычками. Нужно будет писать \n для всех ковычек внутки JSON

Запрос к
@app.post("/api/v1/order")
id продуктов 1 и 2
curl http://127.0.0.1:5000/api/v1/order -X POST -H "Content-Type: application/json" -d {\"product_ids\":[\"1\",\"2\"]}


Запрос к @app.get("/api/v1/order")
curl -L "http://127.0.0.1:5000/api/v1/order?limit=20&page=0" -X GET



Запрос к @app.get("/api/v1/order/<id>")

Вставляем id ранее созданного заказа

curl -L "http://127.0.0.1:5000/api/v1/order/8c6efb08-a07f-44dd-831f-079745e6cde2" -X GET
















