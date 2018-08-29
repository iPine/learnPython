
# coding: utf-8

# In[ ]:



#导入依赖的父模块
from user import User

#提取的独立类
class Privileges():
    def __init__(self,privileges=[ "can add post","can delete post","can ban user"]):
        self.privileges = privileges
    
    def show_privileges(self):
        print('Admin has the following privileges: ')
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self,first_name,last_name,location):
        super().__init__(first_name,last_name,location)
#         self.privileges = [ "can add post","can delete post","can ban user"]
        self.privileges = Privileges()

