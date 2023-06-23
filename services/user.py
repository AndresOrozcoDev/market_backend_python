from models.schema import User as UserModel
from utils.interfaces import User as UserInterface
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
    

    def get_user_by_email(self, email: int):
        result = self.db.query(UserModel).filter(UserModel.email == email).first()
        return result


    def post_login(self, user: UserInterface):
        result = self.db.query(UserModel).filter(UserModel.email == user.email and UserModel.password == user.password).first()
        return result
    

    def create_user(self, user: UserInterface):
        new = UserModel(**{"email": user.email, "password": user.password})
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
        exists = self.get_user_by_email(email)
        if not exists:
            return 'Not found user'
        else:
            try:
                new_password = generate_password()
                send_email(email, 'New Password', 'Your new password is: ', new_password)
            except Exception as e:
                return f"Error {e}" 
            finally:  
                exists.password = new_password
                self.db.commit()
                return f"Your new password {new_password} was send your email."