
# coding: utf-8

# In[ ]:


from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """根据指定的国家，返回Pygal使用的两个字母的国别码"""
    
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        elif name == 'East Asia & Pacific (all income levels)':
            return 'ai'
        elif name == 'East Asia & Pacific (developing only)':
            return 'ad'
        elif name == 'Europe & Central Asia (all income levels)':
            return 'el'
        elif name == 'Europe & Central Asia (developing only)':
            return 'ed'
        elif name == 'Heavily indebted poor countries (HIPC)':
            return 'hp'
        elif name == 'Latin America & Caribbean (all income levels)':
            return 'll'
        elif name == 'Latin America & Caribbean (developing only)':
            return 'ld'
        elif name == 'Least developed countries: UN classification':
            return 'lu'
        elif name == 'Middle East & North Africa (all income levels)':
            return 'ml'
        elif name == 'Middle East & North Africa (developing only)':
            return 'md'
        elif name == 'Sub-Saharan Africa (all income levels)':
            return 'sl'
        elif name == 'Sub-Saharan Africa (developing only)':
            return 'sd'
    #如果没有找到指定的国家，就返回None
    return None

