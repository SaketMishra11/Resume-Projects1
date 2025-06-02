import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px
from pytrends.request import TrendReq 
# pytrend ke libray h pyhton ki jo google ko easily access krti h uske andr ke trends pta krne ke liye fron its internal api

#setup of pytrend library and defing keyword
pytrends=TrendReq(hl='en-us',tz=360)
keyword='cloud computing'

pytrends.build_payload([keyword],cat=0,timeframe='today 12-m',geo='',gprop='',)
# yha pe google se request kr rhe h [keyword means jo hi keyword hme chahiye uska naam cat=category ki konsi category chahiye hmko sab category m chahiye esliye zero likha h,timrframe ka mtlv h kabtak ka data chahiye today 12-m ka mtlv h aaj se purane 12 month ka data chahiye,geo=geography ki konsi geography ke liye chahiye to hme saar geo ke liye chahiye esliye usko blank choda h ,gprop ka mtlv h ko shirf google pr search hua h uska data kuki google kafi other app bhi qcauipe krta h unka nai chahiye esliye esko use  kiya h

# contry wise 
region_data=pytrends.interest_by_region()
region_data=region_data.sort_values(by=keyword,ascending=False).head(15)
plt.figure(figsize=(10,8))
sns.barplot(x=region_data[keyword],y=region_data.index,palette='Blues_d')
plt.title('Top Countries')
plt.xlabel('Interest')
plt.ylabel('Country')
plt.show()

# /making world map 
region_data=region_data.reset_index()# index mtlv btayega kon kon si country m search ho rha
#choropleth ek function h plotly library ka ka jo world map bnane ke liye use hota h
fig=px.choropleth(region_data,
                  locations='geoName',
                  locationmode='country names',# world map m jha or name lekr jau bo us country ka name bta de
                  color=keyword,
                  title=f"search Interest for '{keyword}' by country",#keyword ke acoording dikhayega
                  color_continuous_scale='Reds')
fig.show()

# time wise interest
# last 12 month m kitna search hua h ye nikalna h 
time_df=pytrends.interest_over_time()
plt.figure(figsize=(14,7))
plt.plot(time_df.index,time_df[keyword],marker="o",color='green')
plt.title('Search Interest Over Time')
plt.xlabel('Date')
plt.ylabel('Interest')
plt.grid()
plt.tight_layout()
plt.show()


# comparing multiple keywords
kw_list=['cloud computing','data science','cricket']
pytrends.build_payload(kw_list,cat=0,timeframe='today 12-m',geo="",gprop="")
compare_df=pytrends.interest_over_time()
plt.figure(figsize=(10,7))
for kw in kw_list:
    plt.plot(compare_df.index,comapre_df[kw],label=kw)
    plt.title('comparison over time')
    plt.xlabel('Date')
    plt.ylabel('Interest')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    
plt.show()
    