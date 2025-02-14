from user import User
from post import Post
app_user_one = User("rd@rd.com","raghavendra","password","devOpsEngineer")
app_user_one.getUserInfo()
app_user_one.change_job_title("DevOpsTrainer")
app_user_one.getUserInfo()
app_user_two = User("nana@rd.com","nana","password","devOpsEngineer")
app_user_two.getUserInfo()

new_post = Post("Some New Post",app_user_two.name)
new_post.get_post_info()