— как запустить сервер;
1. Создать виртуальное окружение virtualenv venv
2. Активировать окружение и установить зависимости из requirements.txt

3. Для запуска можно выполнить команду:
.\venv\Scripts\python.exe .\main.py

Или запустить файл используя среду разработки



— как создать продукт;
Можно использовать curl
Так как в windows терминале двойные кавычки обозначают строку, которую мы используем как параметр,
Перед каждыми двойными кавычками внутри JSON должен стоять обратный слеш \

curl http://127.0.0.1:5000/api/v1/product -X POST -H "Content-Type: application/json" -d "{\"name\":\"Refrigerator\",\"price\":\"30.0\"}"
curl http://127.0.0.1:5000/api/v1/product -X POST -H "Content-Type: application/json" -d "{\"name\":\"Washing Machine\",\"price\":\"25.0\"}"

— как получить все продукты;
Сделаем limit 100 и page 0 чтобы получить первые 100 результатов

curl -L "http://127.0.0.1:5000/api/v1/product?limit=100&page=0" -X GET


— как получить продукт по id.

curl -L "http://127.0.0.1:5000/api/v1/product/1" -X GET
curl -L "http://127.0.0.1:5000/api/v1/product/2" -X GET
curl -L "http://127.0.0.1:5000/api/v1/product/3" -X GET
curl -L "http://127.0.0.1:5000/api/v1/product/4" -X GET
curl -L "http://127.0.0.1:5000/api/v1/product/5" -X GET

- удаление продукта по id.

curl -L "http://127.0.0.1:5000/api/v1/product/4" -X DELETE
curl -L "http://127.0.0.1:5000/api/v1/product/5" -X DELETE










Подробно про функции

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
















