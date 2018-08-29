
# coding: utf-8

# In[ ]:


class User:
    def __init__(self,first_name,last_name,location):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
#         for key,value in user_info.items():
#             self[key] = value
        self.login_attempts = 0
        
    def describe_user(self):
        print('Your information include:')
        print('First name: '+ self.first_name.title())
        print('Last name: '+ self.last_name.title())
        print('Location: ' + self.location.title())
#         print('Other info: '+self[key].title())
    
    def greet_user(self):
        print('Hello, ' + self.first_name.title() + ' ' + self.last_name.title()+'\n')
        
    def increment_login_attempts(self,increment=1):
        #increment设置成默认参数可行，设置成可选参数也行increment=""
        #if increment:
            self.login_attempts += increment
        #else:
        #    self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0

#提取独立类
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

