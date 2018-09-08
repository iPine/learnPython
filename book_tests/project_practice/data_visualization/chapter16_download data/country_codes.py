
# coding: utf-8

# In[ ]:


from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """根据指定的国家，返回Pygal使用的两个字母的国别码"""
    
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        elif country_name == 'East Asia & Pacific (all income levels)':
            return 'al'
        elif country_name == 'East Asia & Pacific (developing only)':
            return 'ad'
        elif country_name == 'Europe & Central Asia (all income levels)':
            return 'el'
        elif country_name == 'Europe & Central Asia (developing only)':
            return 'ed'
        elif country_name == 'Heavily indebted poor countries (HIPC)':
            return 'hp'
        elif country_name == 'Latin America & Caribbean (all income levels)':
            return 'll'
        elif country_name == 'Latin America & Caribbean (developing only)':
            return 'ld'
        elif country_name == 'Least developed countries: UN classification':
            return 'lu'
        elif country_name == 'Middle East & North Africa (all income levels)':
            return 'ml'
        elif country_name == 'Middle East & North Africa (developing only)':
            return 'md'
        elif country_name == 'Sub-Saharan Africa (all income levels)':
            return 'sl'
        elif country_name == 'Sub-Saharan Africa (developing only)':
            return 'sd'
    #如果没有找到指定的国家，就返回None
    return None

