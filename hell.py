import json
from os import path
name = "Mark"
users = [
    {
        "username": name,
        "phone": 143
    }
]
flag = 0

print(users[0]['username'])
my_path = 'task.json'
if path.exists(my_path):
    with open(my_path , 'r') as file:
        previous_json = json.load(file)
        print(len(previous_json))
        for i in range(len(previous_json)):
        	print(previous_json[i]['username'])
        	if previous_json[i]["username"] == users[0]['username']:
        		flag = 1
        		print("name already exists")
        		break
        if flag == 0:
        	users = previous_json + users
if flag == 1:
	pass
else:
	with open(my_path , 'w') as file:
		json.dump(users, file, indent=4)