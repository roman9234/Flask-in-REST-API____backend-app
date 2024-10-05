import uuid
from typing import Optional, List

from eshop.model.product import Product
from eshop.data_access.product_repo import save, delete_by_id, get_by_id, get_many, get_new_id


def product_create(name : str, price : float) -> Product:
    product = Product(
        id=get_new_id(),
        name=name,
        price=price
    )
    save(product)
    return product

# Возвращает Product,если он есть в БД, инаце возвращает None
def product_get_by_id(id: str) -> Optional[Product]:
    return get_by_id(id)


def product_get_many(page: int, limit: int) -> List[Product]:
    return get_many(page=page, limit=limit)

def product_delete_by_id(id : str):
    delete_by_id(id)