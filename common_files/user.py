class User:
    def __init__(self,user_email,user_name,password,current_job_title):
        self.email = user_email
        self.name = user_name
        self.password =password
        self.current_job_title = current_job_title

    def change_password(self,password):
        self.password = password

    def change_job_title(self,new_job_title):
        self.current_job_title =  new_job_title

    def getUserInfo(self):
        print(f"user {self.name} cureently works as {self.current_job_title} and you can contact them at {self.email}")

