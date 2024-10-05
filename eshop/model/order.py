from dataclasses import dataclass
from typing import List

# Заказ - имеет id, список id продуктов в заказе и total равный сумме цен всех товаров
@dataclass
class Order:
    id: str
    product_ids: List[str]
    total: int
