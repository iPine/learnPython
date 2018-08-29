
# coding: utf-8

# In[ ]:


class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        #传入一个默认参数，形参就不需要设置；置为0或者为空字符串或者其他默认值
        self.number_served = 0
    
    def describe_restaurant(self):
        print(self.restaurant_name.title() + "'s cuisine type is " + self.cuisine_type + '.')
    
    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is opening!')
    
    def set_number_served(self,number):
        self.number_served = number
        
    
    def increment_number_served(self,increment_number):
        self.number_served += increment_number
        

