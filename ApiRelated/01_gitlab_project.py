import requests

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
#https://gitlab/api/v4/users/nanuchi/projects
#print(response.text)
#print(response.json())
#print(response.json()[1])
my_projects = response.json()

for project in my_projects:
    print(f"Project Name : {project['name']} Project URL : {project['web_url']}")

