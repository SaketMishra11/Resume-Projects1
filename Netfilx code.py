import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('netflix_titles.csv')
# -clean the data
df=df.dropna(subset=['type','release_year','rating','country','duration'])
type_counts=df['type'].value_counts()
plt.figure(figsize=(6,4))# inches m ota h
plt.bar(type_counts.index,type_counts.values,color=['skyblue','orange'])
plt.title('Number of Movies Vs Tv Shows on Netfilx')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('movies_vs_tvshow.png')
plt.show()

# to analyze the rating counts of the data se
rating_counts=df['rating'].value_counts()
plt.figure(figsize=(5,8))
plt.pie(rating_counts,labels=rating_counts.index,autopct='%1.1f%%',startangle=90)
plt.title('Percentage of Content Rating on Netfilx Data')

plt.tight_layout()
plt.savefig('ratingpie chart.png')
plt.show()

movie_df=df[df['type']=='Movie'].copy()
movie_df['duration_int']=movie_df['duration'].str.replace('min','').astype(int)


plt.figure(figsize=(7,6))
plt.hist(movie_df['duration_int'],bins=30,color='orange',edgecolor='black')
plt.title('Duration Of Movies ')
plt.xlabel('Duration in minutes')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('duration_of_movies.png')
plt.show()

# scatter plot release_year vs NUMBER OF SHOWS
release_counts=df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,8))
plt.scatter(release_counts.index,release_counts.values,color='blue')
plt.title(' Release Year vs Number of Show ')
plt.xlabel('Release Year')
plt.ylabel('Number of Show')
plt.tight_layout()
plt.savefig(' Release_Year_vs_Number_of_Show.png')
plt.show()



#Cities who produce maximum number of movies

country_counts=df['country'].value_counts().head(10)
plt.figure(figsize=(10,8))
plt.barh(country_counts.index,country_counts.values,color='violet')
plt.title(' Top 10 countries by number of shows')
plt.xlabel('Number of Show')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('top10 countries.png')
plt.show()


content_by_year = df.groupby(['release_year','type']).size().unstack().fillna(0)
fig,ax=plt.subplots(1,2,figsize=(12,5))

# first subplot:- movies
ax[0].plot(content_by_year.index,content_by_year['Movie'],color='blue')
ax[0].set_title('Movies Released By Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

# second subplot:- Tv shows
ax[1].plot(content_by_year.index,content_by_year['TV Show'],color='red')
ax[1].set_title('TV shows Released By Year')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Number of Tv Shows')

fig.suptitle('Comparsion of Movies and Tv shows Released over Year')
plt.tight_layout()
plt.savefig('comparison of movies and tv shows')
plt.show()