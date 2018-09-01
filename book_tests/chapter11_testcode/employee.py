
# coding: utf-8

# In[ ]:



class Employee():
    """雇员信息"""
    
    def __init__(self,first_name,last_name,annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        
    def give_raise(self,increasment=5000):
        """限定年薪增加额度"""
        self.annual_salary += increasment
        return self.annual_salary

