
# coding: utf-8

# In[7]:


import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#执行API调用并存储响应
# url =  'https://api.github.com/search/repositories?q=language:python&sort=stars'
url =  'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
#使用 requests来执行调用
r = requests.get(url)
#响应对象包含一个名为 status_code 的属性，它让我们知道请求是否成功了（状态码200表示请求成功）
print('Status code:',r.status_code)

#将API响应存储在一个变量中
#使用方法 json() 将这些信息转换为一个Python字典
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

#创建了一个Pygal类 Config 的实例
#通过修改 my_config的属性，可定制图表的外观
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
#标题字体大小
my_config.title_font_size = 24
#副标签字体大小
my_config.label_font_size = 14
#主标签字体大小
my_config.major_label_font_size = 18
#使用truncate_label 将较长的项目名缩短为15个字符
my_config.truncate_label = 15
#隐藏图表中的水平虚线
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config,style=my_style)
# chart.title = 'Most-Starred Python Projects on GitHub'
chart.title = 'Most-Starred JavaScript Projects on GitHub'
chart.x_labels = names

# chart.add('',stars)
chart.add('',plot_dicts)
# chart.render_to_file('python_repos.svg')
chart.render_to_file('javascript_repos.svg')


