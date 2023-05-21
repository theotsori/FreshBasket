class BaseModel:
    def __init__(self, **kwargs):
        self.populate_fields(**kwargs)

    def populate_fields(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class User(BaseModel):
    def __init__(self, user_id, name, email, password, phone):
        super().__init__(user_id=user_id, name=name, email=email, password=password, phone=phone)


class Product(BaseModel):
    def __init__(self, product_id, name, description, price, image, category):
        super().__init__(product_id=product_id, name=name, description=description,
                         price=price, image=image, category=category)


class Cart(BaseModel):
    def __init__(self, cart_id, user_id):
        super().__init__(cart_id=cart_id, user_id=user_id)
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)


class Order(BaseModel):
    def __init__(self, order_id, user_id, status, total):
        super().__init__(order_id=order_id, user_id=user_id, status=status, total=total)
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)
