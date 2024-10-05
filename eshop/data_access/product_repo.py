from typing import List, Optional

from eshop.model.product import Product

_products: List[Product] = [
    Product(
        id='1',
        name='Телевизор',
        price=15,
    ),
    Product(
        id='2',
        name='Кофемашина',
        price=10,
    ),
    Product(
        id='3',
        name='Ноутбук',
        price=12,
    )
]

# Сохраняет недавно добавленный Product
# Если id нового Product равен id уже существующего в списке _product, новый Product заменяет собой старый
def save(product: Product):
    for i in range(len(_products)):
        existed_product = _products[i]
        if existed_product.id == product.id:
            _products[i] = product
            break
    else:
        _products.append(product)

# удаляет product с указанным ID
def delete_by_id(id: str):
    global _products
    _products = [p for p in _products if p.id != id]


# возвращает Product с указанным ID
def get_by_id(id: str) -> Optional[Product]:
    return next((p for p in _products if p.id == id), None)

# делит _product на промежутки равные limit и возвращает из них промежуток под номером page
def get_many(page: int = 0, limit: int = 10):
    start = page * limit
    end = start + limit
    return _products[start:end]
