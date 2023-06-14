from models.schema import Product as ProductModel
from utils.interfaces import Product as ProductInterface

class ProductService():
    
    def __init__(self, db) -> None:
        self.db = db


    def get_products(self):
        result = self.db.query(ProductModel).all()
        return result