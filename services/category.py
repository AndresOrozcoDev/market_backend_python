from models.schema import Category as CategoryModel
from utils.interfaces import Category as CategoryInterface

class CategoryService():
    
    def __init__(self, db) -> None:
        self.db = db


    def get_categories(self):
        result = self.db.query(CategoryModel).all()
        return result
    

    def get_category_by_id(self, id: int):
        result = self.db.query(CategoryModel).filter(CategoryModel.id == id).first()
        return result
    

    def get_category_by_name(self, name: str):
        result = self.db.query(CategoryModel).filter(CategoryModel.name == name).first()
        return result
    

    def create_category(self, name: str):
        new = CategoryModel(**{"name": name})
        self.db.add(new)
        self.db.commit()
        return 
    

    def update_category(self, id: int, name: str):
        exists = self.get_category_by_id(id)
        if not exists:
            return False
        else:
            supermarket = self.db.query(CategoryModel).filter(CategoryModel.id == id).first()
            supermarket.name = name
            self.db.commit()
            return True
    

    def delete_category(self, id: int):
        exists = self.get_category_by_id(id)
        if not exists:
            return False
        else:
            self.db.query(CategoryModel).filter(CategoryModel.id == id).delete()
            self.db.commit()
            return True
            
    