# -*- coding: utf-8 -*-
# @File  : 数据处理.py
# @Author: YiF Lu
# @Date  : 2019/5/17
# @Software: PyCharm

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image
from wordcloud import WordCloud
plt.style.use('ggplot'); #使用'ggplot'风格美化显示的图表
font = {'family':'SimHei'}; #设置使用的字体（需要显示中文的时候使用）
matplotlib.rc('font',**font); #设置显示中文，与字体配合使用

df = pd.read_csv('top250_movie.csv',sep='#',encoding='utf8');
#df.head();
# 查看数据基本信息
#df.info();
# 重复值检查
#count=df.duplicated().value_counts();
#print(count);
country =df['movie_country'].str.split(' ').apply(pd.Series);
#print(country);
all_country = country.apply(pd.value_counts).fillna('0');
all_country.columns = ['area1','area2','area3','area4','area5','area6'];
all_country['area1'] = all_country['area1'].astype(int);
all_country['area2'] = all_country['area2'].astype(int);
all_country['area3'] = all_country['area3'].astype(int);
all_country['area4'] = all_country['area4'].astype(int);
all_country['area5'] = all_country['area5'].astype(int);
all_country['area6'] = all_country['area6'].astype(int);
#print(all_country);
# 得到一个国家或地区参与制作电影数的排名情况
all_country['all_counts'] = all_country['area1']+all_country['area2']+all_country['area3']+all_country['area4']+all_country['area5'];
#降序
all_country=all_country.sort_values(['all_counts'],ascending=False);

#counts=all_country.head();
#print(counts);
# country_rank = pd.DataFrame({'counts':all_country['all_counts']});
#  地区排序 并显示
# show_conuntry=country_rank.sort_values(by='counts',ascending=False)
# 画柱形图 显示前十
all_country['all_counts'].plot(kind='bar');
plt.title('电影产出国',fontsize=20)
plt.show();

# 关于电影类型的字段分析
all_type = df['movie_type'].str.split(' ').apply(pd.Series);
#把缺失值填充0
#print(all_type)
all_type = all_type.apply(pd.value_counts).fillna('0');
#print(all_type)
all_type.columns = ['tpye1','type2','type3','type4','type5'];
all_type['tpye1'] = all_type['tpye1'].astype(int);
all_type['type2'] = all_type['type2'].astype(int);
all_type['type3'] = all_type['type3'].astype(int);
all_type['type4'] = all_type['type4'].astype(int);
all_type['type5'] = all_type['type5'].astype(int);
# 计算总数
all_type['all_counts'] = all_type['tpye1']+all_type['type2']+all_type['type3']+all_type['type4']+all_type['type5'];
all_type = all_type.sort_values(['all_counts'],ascending=False);
top5=all_type.head(5);
#print(top5['all_counts'].astype(int),top5.index.astype(str));
#饼图 前五种类型的电影
plt.axes(aspect=1)
#plt.pie(x=top5['all_counts'],labels=top5.index,autopct='%3.1f %%');
plt.pie(x=all_type['all_counts'],labels=all_type.index,autopct='%3.1f %%');
plt.title('电影类型占比',fontsize=20)
plt.show();
#词云
pic=np.array(Image.open('beij.png'));
wordcloud = WordCloud(max_words=120,font_path='msyh.ttf',mask=pic,background_color='white',scale=2).generate(df['movie_intro'].to_string());
plt.imshow(wordcloud);
plt.axis('off');
plt.show();