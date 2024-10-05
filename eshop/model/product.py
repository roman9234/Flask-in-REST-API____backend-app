from dataclasses import dataclass

# Продукт - имеет id имя и цену
@dataclass()
class Product:
    id: str
    name: str
    price: float