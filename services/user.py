from models.schema import User as UserModel
from utils.functions import send_email, generate_password


class UserService():
    
    def __init__(self, db) -> None:
        self.db = db


    def get_users(self):
        result = self.db.query(UserModel).all()
        return result
    

    def get_user_by_id(self, id: int):
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        return result


    def get_user_login(self, email: str, password: str):
        result = self.db.query(UserModel).filter(UserModel.email == email and UserModel.password == password).first()
        return result
    

    def create_user(self, email: str, password: str):
        new = UserModel(**{"email": email, "password": password})
        self.db.add(new)
        self.db.commit()
        return 
    

    def update_user(self, id: int, password: str):
        exists = self.get_user_by_id(id)
        if not exists:
            return False
        else:
            user = self.db.query(UserModel).filter(UserModel.id == id).first()
            user.password = password
            self.db.commit()
            return True
    

    def delete_user(self, id: int):
        exists = self.get_user_by_id(id)
        if not exists:
            return False
        else:
            self.db.query(UserModel).filter(UserModel.id == id).delete()
            self.db.commit()
            return True
        

    def post_forgetPassword(self, email: str):
        new_password = generate_password()
        subject = 'New Password'
        message = 'Your new password is: '
        result = send_email(email, subject, message, new_password)
        return result