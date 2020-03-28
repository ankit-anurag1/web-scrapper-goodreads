#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup as bs


# In[2]:


url = "https://www.goodreads.com/"
res = requests.get(url)
soup = bs(res.text)


# In[3]:


category = soup.find(id="browseBox")
genres = category.find_all(name='a', class_='gr-hyperlink')
genre_list = [genre.text.lower() for genre in genres]
print("List of available genres: ")
for ind, genre in enumerate(genres):
    print(ind + 1, genre.text, sep="\t")


# In[4]:


url_most_read = url + "genres/most_read"
url_popular = url + "shelf/show"


# In[5]:


inp_genre = input("Enter the genre you wish to find books in: ").lower()
genre_url = ''
if inp_genre in genre_list:
    genre_url_popular = url_popular + genres[genre_list.index(inp_genre)]['href'][7:]
    genre_url_most_read = url_most_read + genres[genre_list.index(inp_genre)]['href'][7:]
else:
    print("Incorrect entry :", inp_genre)
genre_most_read = bs(requests.get(genre_url_most_read).text)
genre_popular = bs(requests.get(genre_url_popular).text)


# In[14]:


#most read : mr
book_list_mr = [(' ').join(elem.find("a")['href'][20:].split('-')).title() 
                for elem in genre_most_read.find_all(class_='coverWrapper')[:40] 
                if elem.find("a") is not None and len(elem.find("a")['href']) > 20]

#popular
book_list_popular = [ elem.find(class_="bookTitle").text.split('(')[0]  
                     for elem in genre_popular.find(class_="leftContainer").find_all(class_="elementList")[:40] 
                     if elem.find(class_="bookTitle") is not None]


# In[16]:


print("Most Read This Week in the category :", inp_genre)
for ind, elem in enumerate(book_list_mr[:20]):
    print(ind+1, elem, sep="\t")
    
    
print("\n\nPopular books in the category :", inp_genre)    
for ind, elem in enumerate(book_list_popular[:20]):
    print(ind+1, elem, sep="\t")


# In[ ]:




