import sys, json, admin, os

total_user_count = 0
class user:
    def __init__(self,username=None, pwd=None, uid=0):
        self.username = username
        self.pwd = pwd
        self.uid = uid
    def add(self, data):
        data[self.uid] = {
            "username": self.username,
            "pwd": self.pwd,
            "tasks": {}
        }

owner = admin.get()
data = {}
data[owner.uid] = {
    "username": owner.username,
    "pwd": owner.pwd,
    "tasks": owner.tasks
}

file_path = admin.file_path()
def dump(file_path):
    with open(file_path, 'w') as file: 
        json.dump(data, file)

def read(file_path):
    with open(file_path, 'r') as file: 
        return json.load(file)
    
data = read(file_path)
def checkCredentials(user, pwd):
    for id in data:
        if user == data[id]['username'] and user[id]['pwd'] == pwd:
            return 1
    return 0

def sout():
    return str(read())