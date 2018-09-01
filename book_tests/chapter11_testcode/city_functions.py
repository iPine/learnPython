
# coding: utf-8

# In[ ]:



def city_country_population(cityname,countryname,population=''):
    if population:
        message = cityname.title() + ',' + countryname.title() + ' - population ' + str(population)
    else:
        message = cityname.title() + ',' + countryname.title()
    return message