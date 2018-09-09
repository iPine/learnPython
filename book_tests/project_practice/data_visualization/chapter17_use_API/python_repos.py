
# coding: utf-8

# In[7]:


import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#执行API调用并存储响应
url =  'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
#使用 requests来执行调用
r = requests.get(url)
print('Status code:',r.status_code)


response_dict = r.json()
print("Total repositories:",response_dict['total_count'])

#探索有关仓库的信息
repo_dicts = response_dict['items']


names,plot_dicts = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    #stars.append(repo_dict['stargazers_count'])  
    if repo_dict['description']:
        plot_dict = {
            'value':repo_dict['stargazers_count'],
            'label':repo_dict['description'],
            'xlink':repo_dict['html_url']
        }
    else:
        plot_dict = {
            'value':repo_dict['stargazers_count'],
            'label':'No description!',
            'xlink':repo_dict['html_url']
        }
    plot_dicts.append(plot_dict)

#可视化
my_style = LS('#663333',base_style=LCS)

#通过修改 my_config的属性，可定制图表的外观
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config,style=my_style)

chart.title = 'Most-Starred JavaScript Projects on GitHub'
chart.x_labels = names

# chart.add('',stars)
chart.add('',plot_dicts)
chart.render_to_file('javascript_repos.svg')


