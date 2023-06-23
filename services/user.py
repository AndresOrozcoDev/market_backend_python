from utils.functions import send_email, generate_password


class UserService():
    
    def __init__(self, db) -> None:
        self.db = db

    async def post_forgetPassword(self, email: str):
        new_password = await generate_password()
        subject = 'New Password'
        message = 'Your new password is: '
        result = await send_email(email, subject, message, new_password)
        return result